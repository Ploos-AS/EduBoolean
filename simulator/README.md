# EduLogic Simulator

This directory is reserved for EduBoolean's interactive logic simulator.

## M0 architecture direction

The simulator should be split into a deterministic logic core and one or more frontends.

```text
course exercises / UI / CLI
           |
           v
     simulator API
           |
           v
   deterministic core
           |
           +-- gates
           +-- wires/nets
           +-- circuit graph
           +-- evaluation
           +-- truth tables
           +-- serialization
```

## Core requirements

The core should:

- have no dependency on wall-clock time for combinational evaluation
- be usable without a GUI
- support deterministic tests
- represent 0 and 1 explicitly
- support NOT, AND, OR, XOR, NAND, NOR and XNOR
- allow circuits to be constructed programmatically
- generate truth tables for suitable combinational circuits
- expose enough state for teaching tools to highlight signal flow
- use a documented, versioned save format

## Later extensions

After the combinational core is stable, possible extensions include:

- switches, LEDs and interactive wiring
- propagation visualization
- sequential components and clocks
- circuit challenges
- import/export
- HDL generation experiments
- browser frontend
- desktop frontend
- CLI/headless qualification

## Non-goal for M0

M0 does not implement the simulator. It freezes enough architectural direction to prevent course content and future software from growing in incompatible directions.
