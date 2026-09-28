#!/usr/bin/env python3
"""EduLogic: deterministic educational digital-logic simulator."""

from __future__ import annotations
import argparse, itertools, json, re
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
    if len(set(inputs)) != len(inputs): raise ValueError("duplicate input name")
    if len(set(outputs)) != len(outputs): raise ValueError("duplicate output name")
    names = set(inputs)
    state_cells = []
    for cell in state:
        kind = cell.get("type")
        if kind == "DFF":
            qs = [cell["q"]]
        elif kind in ("REGISTER", "COUNTER"):
            width = int(cell["width"])
            if width < 1: raise ValueError(f"{kind} width must be positive")
            if kind == "COUNTER":
                step = int(cell.get("step", 1))
                if step < 0 or step >= (1 << width): raise ValueError("COUNTER step must fit width and be non-negative")
            qs = [f"{cell['q']}[{i}]" for i in range(width)]
        else:
            raise ValueError(f"unsupported state cell: {kind}")
        initial = int(cell.get("initial", 0))
        if initial < 0 or initial >= (1 << len(qs)): raise ValueError("initial state does not fit width")
        for q in qs:
            if q in names: raise ValueError(f"signal has multiple drivers: {q}")
            names.add(q)
        state_cells.append((cell, qs))
    for gate in gates:
        kind, ins, out = gate["type"].upper(), gate["inputs"], gate["output"]
        if kind not in GATES: raise ValueError(f"unsupported gate: {kind}")
        if kind == "NOT" and len(ins) != 1: raise ValueError("NOT requires one input")
        if kind != "NOT" and len(ins) < 2: raise ValueError(f"{kind} requires at least two inputs")
        if out in names: raise ValueError(f"signal has multiple drivers: {out}")
        names.add(out)
    for gate in gates:
        unknown = [name for name in gate["inputs"] if name not in names]
        if unknown: raise ValueError(f"gate {gate['output']} references unknown signals: {unknown}")
    for cell, qs in state_cells:
        kind = cell["type"]
        if kind == "DFF":
            refs = [cell["d"]]
        elif kind == "REGISTER":
            refs = list(cell["d"])
            if len(refs) != len(qs): raise ValueError("REGISTER d width mismatch")
        else:
            refs = []
        for key in ("enable", "reset"):
            if cell.get(key): refs.append(cell[key])
        unknown = [name for name in refs if name not in names]
        if unknown: raise ValueError(f"{kind} references unknown signals: {unknown}")
    unknown = [o for o in outputs if o not in names]
    if unknown: raise ValueError(f"undriven outputs: {unknown}")
    teaching = circuit.get("teaching", {})
    for group in ("switches", "leds"):
        for item in teaching.get(group, []):
            if item["signal"] not in names: raise ValueError(f"{group} references unknown signal: {item['signal']}")

def state_names(cell):
    if cell["type"] == "DFF": return [cell["q"]]
    return [f"{cell['q']}[{i}]" for i in range(int(cell["width"]))]

def initial_state(circuit):
    validate(circuit)
    state = {}
    for cell in circuit.get("state", []):
        if cell["type"] == "DFF":
            state[cell["q"]] = bit(cell.get("initial", 0))
        else:
            value = int(cell.get("initial", 0))
            width = int(cell["width"])
            if value < 0 or value >= (1 << width): raise ValueError("initial state does not fit width")
            for i, name in enumerate(state_names(cell)): state[name] = (value >> i) & 1
    return state

def evaluate_signals(circuit, input_values, state_values=None):
    """Return every settled signal, including intermediate nets and state outputs."""
    validate(circuit)
    missing = [name for name in circuit["inputs"] if name not in input_values]
    if missing: raise ValueError(f"missing input values: {missing}")
    signals = {name: bit(input_values[name]) for name in circuit["inputs"]}
    expected_state = {name for cell in circuit.get("state", []) for name in state_names(cell)}
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
        kind = cell["type"]
        names = state_names(cell)
        reset = signals.get(cell.get("reset"), 0) if cell.get("reset") else 0
        enable = signals.get(cell.get("enable"), 1) if cell.get("enable") else 1
        if reset:
            for name in names: next_state[name] = 0
        elif not enable:
            for name in names: next_state[name] = state_values[name]
        elif kind == "DFF":
            d = cell["d"]
            if d not in signals: raise ValueError(f"DFF {cell['q']} references unresolved D signal: {d}")
            next_state[cell["q"]] = signals[d]
        elif kind == "REGISTER":
            ds = cell["d"]
            if len(ds) != len(names): raise ValueError("REGISTER d width mismatch")
            for name, d in zip(names, ds):
                if d not in signals: raise ValueError(f"REGISTER references unresolved D signal: {d}")
                next_state[name] = signals[d]
        elif kind == "COUNTER":
            value = sum(state_values[name] << i for i, name in enumerate(names))
            value = (value + int(cell.get("step", 1))) % (1 << len(names))
            for i, name in enumerate(names): next_state[name] = (value >> i) & 1
    return next_state

def run_sequence(circuit, suite):
    if suite.get("format") != "edulogic-sequence-1": raise ValueError("sequence format must be edulogic-sequence-1")
    if suite.get("circuit") and suite["circuit"] != circuit.get("name"): raise ValueError("sequence targets a different circuit")
    state = initial_state(circuit)
    state_set = set(state)
    input_set = set(circuit["inputs"])
    results = []
    for index, step in enumerate(suite["steps"], 1):
        inputs = step.get("inputs", {})
        missing_inputs = input_set - set(inputs)
        unknown_inputs = set(inputs) - input_set
        if missing_inputs: raise ValueError(f"sequence step {index} missing inputs: {sorted(missing_inputs)}")
        if unknown_inputs: raise ValueError(f"sequence step {index} has unknown inputs: {sorted(unknown_inputs)}")
        if "expect_state" not in step: raise ValueError(f"sequence step {index} needs expect_state")
        expected = {k: bit(v) for k, v in step["expect_state"].items()}
        unknown_state = set(expected) - state_set
        if unknown_state: raise ValueError(f"sequence step {index} expects unknown state: {sorted(unknown_state)}")
        missing_state = state_set - set(expected)
        if missing_state: raise ValueError(f"sequence step {index} must specify complete state: {sorted(missing_state)}")
        state = tick(circuit, inputs, state)
        ok = state == expected
        results.append({"index":index,"ok":ok,"inputs":inputs,"expect":expected,"state":dict(state)})
    return results

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
    if circuit.get("state"): raise ValueError("truth tables require a combinational circuit; use ticks or a sequence for stateful circuits")
    names = circuit["inputs"]
    return [(given := dict(zip(names, values)), evaluate(circuit, given))
            for values in itertools.product((0, 1), repeat=len(names))]

def run_vectors(circuit, suite):
    if suite.get("format") != "edulogic-vectors-1": raise ValueError("vector format must be edulogic-vectors-1")
    if suite.get("circuit") and suite["circuit"] != circuit.get("name"): raise ValueError("vectors target a different circuit")
    if circuit.get("state"): raise ValueError("vectors require a combinational circuit; use a sequence for stateful circuits")
    results = []
    input_set, output_set = set(circuit["inputs"]), set(circuit["outputs"])
    for index, vector in enumerate(suite["vectors"], 1):
        inputs = vector.get("inputs", {})
        missing_inputs = input_set - set(inputs)
        unknown_inputs = set(inputs) - input_set
        if missing_inputs: raise ValueError(f"vector {index} missing inputs: {sorted(missing_inputs)}")
        if unknown_inputs: raise ValueError(f"vector {index} has unknown inputs: {sorted(unknown_inputs)}")
        actual = evaluate(circuit, inputs)
        if "expect" not in vector: raise ValueError(f"vector {index} needs expect")
        expected = {k: bit(v) for k, v in vector["expect"].items()}
        unknown = set(expected) - output_set
        if unknown: raise ValueError(f"vector {index} expects unknown outputs: {sorted(unknown)}")
        missing_outputs = output_set - set(expected)
        if missing_outputs: raise ValueError(f"vector {index} must specify complete outputs: {sorted(missing_outputs)}")
        ok = actual == expected
        results.append({"index": index, "ok": ok, "inputs": vector["inputs"],
                        "expect": expected, "actual": actual})
    return results


def verilog_name(name):
    """Map an EduLogic name to a conservative Verilog identifier."""
    mapped = re.sub(r"[^A-Za-z0-9_$]", "_", str(name))
    if not mapped or not re.match(r"[A-Za-z_]", mapped[0]): mapped = "_" + mapped
    return mapped

def verilog_names(circuit):
    """Return and validate the complete EduLogic-to-Verilog identifier map."""
    names = list(circuit.get("inputs", [])) + list(circuit.get("outputs", []))
    names += [g["output"] for g in circuit.get("gates", [])]
    names += [n for cell in circuit.get("state", []) for n in state_names(cell)]
    unique = list(dict.fromkeys(names))
    mapping = {name: verilog_name(name) for name in unique}
    reverse = {}
    for source, target in mapping.items():
        if target in reverse and reverse[target] != source:
            raise ValueError(f"Verilog identifier collision: {reverse[target]!r} and {source!r} -> {target!r}")
        reverse[target] = source
    return mapping

def verilog_module_name(name):
    mapped = verilog_name(name)
    if mapped in {"module","endmodule","input","output","wire","reg","always","assign","begin","end","if","else"}:
        mapped = "_" + mapped
    return mapped

def export_verilog(circuit, module_name=None):
    """Export supported EduLogic circuits as synthesizable Verilog-2001."""
    validate(circuit)
    names_map = verilog_names(circuit)
    module_name = verilog_module_name(module_name or circuit.get("name", "edulogic"))
    sequential = bool(circuit.get("state"))
    ports = (["clk"] if sequential else []) + circuit["inputs"] + circuit["outputs"]
    lines = [f"module {module_name}({', '.join(verilog_name(x) for x in ports)});"]
    if sequential: lines.append("  input clk;")
    for name in circuit["inputs"]: lines.append(f"  input {verilog_name(name)};")
    state_set = {n for cell in circuit.get("state", []) for n in state_names(cell)}
    gate_outputs = {g["output"] for g in circuit["gates"]}
    for name in circuit["outputs"]:
        decl = "output reg" if name in state_set else "output"
        lines.append(f"  {decl} {verilog_name(name)};")
    internal_state = state_set - set(circuit["outputs"])
    for name in sorted(internal_state): lines.append(f"  reg {verilog_name(name)};")
    internal_wires = gate_outputs - set(circuit["outputs"]) - state_set
    for name in sorted(internal_wires): lines.append(f"  wire {verilog_name(name)};")
    op = {"AND":" & ","OR":" | ","XOR":" ^ "}
    for gate in circuit["gates"]:
        kind=gate["type"].upper(); ins=[verilog_name(x) for x in gate["inputs"]]; out=verilog_name(gate["output"])
        if kind=="NOT": expr=f"~{ins[0]}"
        elif kind in ("AND","OR","XOR"): expr=op[kind].join(ins)
        elif kind in ("NAND","NOR","XNOR"):
            base={"NAND":"AND","NOR":"OR","XNOR":"XOR"}[kind]; expr=f"~({op[base].join(ins)})"
        lines.append(f"  assign {out} = {expr};")
    for cell in circuit.get("state", []):
        names=state_names(cell); reset=cell.get("reset"); enable=cell.get("enable")
        lines.append("  always @(posedge clk) begin")
        prefix = "    "
        if reset:
            lines.append(f"    if ({verilog_name(reset)}) begin")
            for q in names: lines.append(f"      {verilog_name(q)} <= 1'b0;")
            lines.append("    end" + (" else begin" if enable else " else begin"))
            prefix="      "
        if enable:
            lines.append(f"{prefix}if ({verilog_name(enable)}) begin")
            prefix += "  "
        if cell["type"]=="DFF":
            lines.append(f"{prefix}{verilog_name(cell['q'])} <= {verilog_name(cell['d'])};")
        elif cell["type"]=="REGISTER":
            for q,d in zip(names,cell["d"]): lines.append(f"{prefix}{verilog_name(q)} <= {verilog_name(d)};")
        else:
            width=len(names); lhs="{" + ", ".join(verilog_name(q) for q in reversed(names)) + "}"
            lines.append(f"{prefix}{lhs} <= {lhs} + {width}'d{int(cell.get('step',1))};")
        if enable:
            prefix=prefix[:-2]; lines.append(f"{prefix}end")
        if reset: lines.append("    end")
        lines.append("  end")
    lines.append("endmodule")
    return "\n".join(lines) + "\n"

def export_sequence_testbench(circuit, suite, module_name=None):
    """Generate an Icarus/SystemVerilog testbench from edulogic-sequence-1."""
    validate(circuit)
    if not circuit.get("state"): raise ValueError("sequence testbench requires a stateful circuit")
    if suite.get("format") != "edulogic-sequence-1": raise ValueError("sequence format must be edulogic-sequence-1")
    if suite.get("circuit") and suite["circuit"] != circuit.get("name"): raise ValueError("sequence targets a different circuit")
    verilog_names(circuit)
    module_name = verilog_module_name(module_name or circuit.get("name", "edulogic"))
    tb_name = module_name + "_sequence_tb"
    ins = circuit["inputs"]
    outs = circuit["outputs"]
    lines = [f"module {tb_name};", "  reg clk=0;"]
    for name in ins: lines.append(f"  reg {verilog_name(name)}=0;")
    for name in outs: lines.append(f"  wire {verilog_name(name)};")
    lines.append("  integer errors=0;")
    ports = ["clk"] + [verilog_name(x) for x in ins + outs]
    lines.append(f"  {module_name} dut({', '.join(ports)});")
    lines.append("  task pulse; begin #1 clk=1; #1 clk=0; end endtask")
    lines.append("  initial begin")
    for index, step in enumerate(suite["steps"], 1):
        for name in ins:
            if name not in step.get("inputs", {}): raise ValueError(f"sequence step {index} missing input: {name}")
            lines.append(f"    {verilog_name(name)}={bit(step['inputs'][name])};")
        lines.append("    pulse;")
        expected = {k: bit(v) for k, v in step["expect_state"].items()}
        unknown = set(expected) - set(outs)
        if unknown: raise ValueError(f"sequence RTL oracle requires expected state to be observable outputs: {sorted(unknown)}")
        for name, value in expected.items():
            vn = verilog_name(name)
            lines.append(f"    if({vn} !== 1'b{value}) begin $display(\"FAIL step {index} {vn}\"); errors=errors+1; end")
    lines.append('    if(errors) $fatal(1,"%0d failures",errors);')
    lines.append('    $display("PASS generated sequence");')
    lines.append("    $finish;")
    lines.append("  end")
    lines.append("endmodule")
    return "\n".join(lines) + "\n"

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def main():
    parser = argparse.ArgumentParser(prog="edulogic")
    parser.add_argument("circuit")
    parser.add_argument("--truth-table", action="store_true")
    parser.add_argument("--trace", action="store_true")
    parser.add_argument("--vectors", metavar="FILE")
    parser.add_argument("--sequence", metavar="FILE")
    parser.add_argument("--ticks", type=int, metavar="N")
    parser.add_argument("--verilog", action="store_true")
    parser.add_argument("--sequence-testbench", metavar="FILE")
    parser.add_argument("--set", action="append", default=[], metavar="NAME=BIT")
    args = parser.parse_args()
    circuit = load(args.circuit)
    if args.verilog:
        print(export_verilog(circuit), end="")
        return
    if args.sequence_testbench:
        print(export_sequence_testbench(circuit, load(args.sequence_testbench)), end="")
        return
    if args.truth_table:
        cols = circuit["inputs"] + circuit["outputs"]
        print(" ".join(cols))
        for given, result in truth_table(circuit):
            row = {**given, **result}; print(" ".join(str(row[c]) for c in cols))
        return
    if args.sequence:
        results = run_sequence(circuit, load(args.sequence))
        for r in results:
            print(f"{'PASS' if r['ok'] else 'FAIL'} {r['index']}: {r['inputs']} -> {r['state']}")
        raise SystemExit(0 if all(r["ok"] for r in results) else 1)
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
