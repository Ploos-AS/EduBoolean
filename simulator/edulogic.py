#!/usr/bin/env python3
"""EduLogic: deterministic combinational logic simulator."""

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
    else:
        result = sum(values) & 1
    return 1 - result if kind in ("NAND", "NOR", "XNOR") else result

def validate(circuit):
    if circuit.get("format") != "edulogic-1": raise ValueError("format must be edulogic-1")
    inputs = circuit.get("inputs", [])
    outputs = circuit.get("outputs", [])
    gates = circuit.get("gates", [])
    if not inputs or not outputs: raise ValueError("circuit needs inputs and outputs")
    names = set(inputs)
    for gate in gates:
        out = gate["output"]
        if out in names: raise ValueError(f"signal has multiple drivers: {out}")
        names.add(out)
    unknown = [o for o in outputs if o not in names]
    if unknown: raise ValueError(f"undriven outputs: {unknown}")

def evaluate(circuit, input_values):
    validate(circuit)
    signals = {name: bit(input_values[name]) for name in circuit["inputs"]}
    pending = list(circuit["gates"])
    while pending:
        progress = False
        for gate in pending[:]:
            ins = gate["inputs"]
            if all(name in signals for name in ins):
                signals[gate["output"]] = eval_gate(gate["type"], [signals[x] for x in ins])
                pending.remove(gate); progress = True
        if not progress:
            raise ValueError("circuit cannot settle: cycle or missing signal")
    return {name: signals[name] for name in circuit["outputs"]}

def truth_table(circuit):
    validate(circuit)
    names = circuit["inputs"]
    rows = []
    for values in itertools.product((0, 1), repeat=len(names)):
        given = dict(zip(names, values))
        rows.append((given, evaluate(circuit, given)))
    return rows

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def main():
    parser = argparse.ArgumentParser(prog="edulogic")
    parser.add_argument("circuit")
    parser.add_argument("--truth-table", action="store_true")
    parser.add_argument("--set", action="append", default=[], metavar="NAME=BIT")
    args = parser.parse_args()
    circuit = load(args.circuit)
    if args.truth_table:
        cols = circuit["inputs"] + circuit["outputs"]
        print(" ".join(cols))
        for given, result in truth_table(circuit):
            row = {**given, **result}
            print(" ".join(str(row[c]) for c in cols))
        return
    given = {}
    for assignment in args.set:
        name, value = assignment.split("=", 1)
        given[name] = bit(int(value))
    result = evaluate(circuit, given)
    for name in circuit["outputs"]:
        print(f"{name}={result[name]}")

if __name__ == "__main__":
    main()
