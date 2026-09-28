#!/usr/bin/env python3
"""EduLogic: deterministic educational digital-logic simulator."""

from __future__ import annotations
import argparse, itertools, json
from pathlib import Path

GATES = {"NOT", "AND", "OR", "XOR", "NAND", "NOR", "XNOR"}

def bit(value):
    if value in (0, False): return 0
    if value in (1, True): return 1
    raise ValueError(f"not a logic bit: {value!r}")

def eval_gate(kind, values):
    kind = kind.upper()
    if kind not in GATES: raise ValueError(f"unsupported gate: {kind}")
    if kind == "NOT":
        if len(values) != 1: raise ValueError("NOT requires one input")
        return 1 - values[0]
    if len(values) < 2: raise ValueError(f"{kind} requires at least two inputs")
    if kind in ("AND", "NAND"): result = int(all(values))
    elif kind in ("OR", "NOR"): result = int(any(values))
    else: result = sum(values) & 1
    return 1 - result if kind in ("NAND", "NOR", "XNOR") else result

def validate(circuit):
    if circuit.get("format") != "edulogic-1": raise ValueError("format must be edulogic-1")
    inputs, outputs, gates = circuit.get("inputs", []), circuit.get("outputs", []), circuit.get("gates", [])
    state = circuit.get("state", [])
    if not outputs: raise ValueError("circuit needs outputs")
    names = set(inputs)
    for cell in state:
        if cell.get("type") != "DFF": raise ValueError(f"unsupported state cell: {cell.get('type')}")
        q = cell["q"]
        if q in names: raise ValueError(f"signal has multiple drivers: {q}")
        names.add(q)
    if len(names) != len(inputs): raise ValueError("duplicate input name")
    for gate in gates:
        kind, ins, out = gate["type"].upper(), gate["inputs"], gate["output"]
        if kind not in GATES: raise ValueError(f"unsupported gate: {kind}")
        if out in names: raise ValueError(f"signal has multiple drivers: {out}")
        names.add(out)
    unknown = [o for o in outputs if o not in names]
    if unknown: raise ValueError(f"undriven outputs: {unknown}")
    teaching = circuit.get("teaching", {})
    for group in ("switches", "leds"):
        for item in teaching.get(group, []):
            if item["signal"] not in names: raise ValueError(f"{group} references unknown signal: {item['signal']}")

def initial_state(circuit):
    validate(circuit)
    return {cell["q"]: bit(cell.get("initial", 0)) for cell in circuit.get("state", [])}

def evaluate_signals(circuit, input_values, state_values=None):
    """Return every settled signal, including intermediate nets and state outputs."""
    validate(circuit)
    missing = [name for name in circuit["inputs"] if name not in input_values]
    if missing: raise ValueError(f"missing input values: {missing}")
    signals = {name: bit(input_values[name]) for name in circuit["inputs"]}
    expected_state = {cell["q"] for cell in circuit.get("state", [])}
    supplied_state = initial_state(circuit) if state_values is None else state_values
    missing_state = expected_state - set(supplied_state)
    if missing_state: raise ValueError(f"missing state values: {sorted(missing_state)}")
    signals.update({name: bit(supplied_state[name]) for name in expected_state})
    pending = list(circuit["gates"])
    while pending:
        progress = False
        for gate in pending[:]:
            ins = gate["inputs"]
            if all(name in signals for name in ins):
                signals[gate["output"]] = eval_gate(gate["type"], [signals[x] for x in ins])
                pending.remove(gate); progress = True
        if not progress:
            unresolved = [g["output"] for g in pending]
            raise ValueError(f"circuit cannot settle: cycle or missing signal; unresolved={unresolved}")
    return signals

def evaluate(circuit, input_values, state_values=None):
    signals = evaluate_signals(circuit, input_values, state_values)
    return {name: signals[name] for name in circuit["outputs"]}

def tick(circuit, input_values, state_values):
    """Settle combinational logic, then atomically sample every DFF D input."""
    signals = evaluate_signals(circuit, input_values, state_values)
    next_state = {}
    for cell in circuit.get("state", []):
        d = cell["d"]
        if d not in signals: raise ValueError(f"DFF {cell['q']} references unresolved D signal: {d}")
        next_state[cell["q"]] = signals[d]
    return next_state

def run_ticks(circuit, count, input_values=None, state_values=None):
    input_values = input_values or {}
    state = initial_state(circuit) if state_values is None else dict(state_values)
    trace = [dict(state)]
    for _ in range(count):
        state = tick(circuit, input_values, state)
        trace.append(dict(state))
    return trace

def truth_table(circuit):
    validate(circuit)
    names = circuit["inputs"]
    return [(given := dict(zip(names, values)), evaluate(circuit, given))
            for values in itertools.product((0, 1), repeat=len(names))]

def run_vectors(circuit, suite):
    results = []
    for index, vector in enumerate(suite["vectors"], 1):
        actual = evaluate(circuit, vector["inputs"])
        expected = {k: bit(v) for k, v in vector["expect"].items()}
        ok = all(actual.get(k) == v for k, v in expected.items())
        results.append({"index": index, "ok": ok, "inputs": vector["inputs"],
                        "expect": expected, "actual": actual})
    return results

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def main():
    parser = argparse.ArgumentParser(prog="edulogic")
    parser.add_argument("circuit")
    parser.add_argument("--truth-table", action="store_true")
    parser.add_argument("--trace", action="store_true")
    parser.add_argument("--vectors", metavar="FILE")
    parser.add_argument("--ticks", type=int, metavar="N")
    parser.add_argument("--set", action="append", default=[], metavar="NAME=BIT")
    args = parser.parse_args()
    circuit = load(args.circuit)
    if args.truth_table:
        cols = circuit["inputs"] + circuit["outputs"]
        print(" ".join(cols))
        for given, result in truth_table(circuit):
            row = {**given, **result}; print(" ".join(str(row[c]) for c in cols))
        return
    if args.vectors:
        results = run_vectors(circuit, load(args.vectors))
        for r in results:
            print(f"{'PASS' if r['ok'] else 'FAIL'} {r['index']}: {r['inputs']} -> {r['actual']}")
        raise SystemExit(0 if all(r["ok"] for r in results) else 1)
    given = {}
    for assignment in args.set:
        name, value = assignment.split("=", 1); given[name] = bit(int(value))
    if args.ticks is not None:
        for n, state in enumerate(run_ticks(circuit, args.ticks, given)):
            print(f"{n}: " + " ".join(f"{k}={v}" for k, v in state.items()))
        return
    signals = evaluate_signals(circuit, given)
    names = list(signals) if args.trace else circuit["outputs"]
    for name in names: print(f"{name}={signals[name]}")

if __name__ == "__main__":
    main()
