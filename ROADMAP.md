# EduBoolean Roadmap

EduBoolean follows milestone-based development. The course is intentionally built from a zero-prerequisite foundation before adding advanced digital-logic topics.

## M0 — Foundation

Goal: establish the project, pedagogy, course architecture and first usable learning path.

- [x] Define project purpose and target audience
- [x] Define Norwegian as primary language and English as parallel language
- [x] Define top-level course structure
- [x] Define repository layout
- [x] Define licensing policy
- [x] Add contribution guidelines
- [x] Add Norwegian course index
- [x] Add English course index
- [x] Add first Norwegian lesson: what Boolean algebra is
- [x] Add starter exercises and lab structure
- [x] Reserve simulator architecture

Exit criterion: a newcomer can understand what the course will teach, start the first lesson, and see a coherent path from true/false to digital computers.

## M1 — Boolean Fundamentals

Goal: complete the beginner core.

- [x] Boolean values and variables
- [x] NOT, AND and OR
- [x] XOR, NAND, NOR and XNOR
- [x] truth tables
- [x] translating everyday statements into Boolean expressions
- [x] exercises with worked solutions
- [x] first practical half-adder lab
- [ ] English lesson parity (continues incrementally alongside later milestones)

**M1 core status: COMPLETE.** Norwegian beginner core is usable end-to-end; English translation parity remains an ongoing publishing track.

## M2 — Algebra and Simplification

Goal: teach Boolean manipulation without assuming prior algebra expertise.

- [x] identity, domination, idempotence and complement laws
- [x] commutative, associative and distributive laws
- [x] absorption
- [x] De Morgan's laws
- [x] algebraic simplification
- [x] equivalence checking using truth tables
- [x] worked exercises and circuit-simplification lab

**M2 core status: COMPLETE.**

## M3 — Logic Gates and Combinational Circuits

Goal: connect abstract expressions to circuits.

- gate symbols
- expression ↔ gate network
- propagation concepts
- half adder and full adder
- multiplexers
- decoders and encoders
- comparators

## M4 — Karnaugh Maps

Goal: provide a visual simplification method.

- 2-variable maps
- 3-variable maps
- 4-variable maps
- grouping rules
- don't-care conditions
- compare K-map and algebraic simplification

## M5 — Sequential Logic

Goal: introduce state and memory as the next conceptual step.

- why combinational logic is not enough
- latch
- flip-flop
- clock
- register
- counter
- transition from Boolean algebra toward finite state machines

EduFSM is a natural follow-on course for deeper treatment of state machines.

## M6 — From Logic to CPU

Goal: connect course concepts to computer architecture.

- n-bit adders
- ALU functions
- flags
- register selection
- control signals
- opcode decoding
- small CPU datapath examples
- bridges to EduCPU and EduK8

## M7 — Boolean Logic in Software

Goal: make the same ideas recognizable in programming.

- Boolean types
- comparisons
- `if` conditions
- logical operators
- bitwise versus logical operations
- masks
- permissions and feature flags
- practical C and Python examples

## M8 — EduLogic Simulator

Goal: make the course interactive.

Planned capabilities:

- switches and LEDs
- NOT/AND/OR/XOR/NAND/NOR/XNOR gates
- wires and signal highlighting
- automatic truth-table generation
- combinational circuit evaluation
- save/load circuit format
- deterministic core independent of UI
- later HDL export/import experiments

## M9 — Publishing

Goal: first-class multi-format release from common sources.

- static website
- EPUB
- Kindle-friendly output
- PDF
- automated build/validation
- language parity checks
- link and example validation

## Future

Possible later extensions:

- physical 74xx logic labs
- breadboard labs
- Arduino used only as test/instrumentation aid
- FPGA labs
- Verilog/VHDL bridge material
- circuit challenges
- automatic exercise generation
- teacher material and answer keys
