# EduLogic Simulator

EduLogic is EduBoolean's deterministic, headless logic simulator.

## M8 implementation

The first implementation deliberately starts with a small dependency-free Python core. The core has no GUI, wall-clock or real-time dependency.

Supported gates:

- NOT
- AND
- OR
- XOR
- NAND
- NOR
- XNOR

It supports versioned JSON circuits, deterministic combinational evaluation and automatic truth-table generation.

## Quick start

```bash
cd simulator
python3 edulogic.py examples/half-adder.json --truth-table
python3 edulogic.py examples/half-adder.json --set A=1 --set B=1
python3 edulogic.py examples/counter2.json --ticks 8
python3 -m unittest -v test_edulogic.py
```

Expected half-adder truth table:

```text
A B SUM CARRY
0 0 0 0
0 1 1 0
1 0 1 0
1 1 0 1
```

See [FORMAT.md](FORMAT.md) for the circuit format.

## Architecture

```text
course exercises / future UI / CLI
             |
             v
       EduLogic core
             |
     +-------+--------+
     |       |        |
   gates   graph   truth tables
```

The combinational evaluator repeatedly evaluates gates whose inputs are known. This makes the result independent of gate ordering in the JSON file.

A circuit that cannot settle because of a cycle or missing dependency is rejected. Sequential logic will later get explicit clock/state semantics rather than abusing the combinational evaluator.

## Next M8 increments

- richer validation and diagnostics
- named switches/LEDs as teaching metadata
- signal trace/introspection
- reusable test-vector format
- deterministic DFF/tick state model (implemented)
- register/counter convenience components
- optional browser/desktop frontend
- HDL bridge experiments
