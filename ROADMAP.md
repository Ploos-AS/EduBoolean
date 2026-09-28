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

- Boolean values and variables
- NOT, AND and OR
- XOR, NAND, NOR and XNOR
- truth tables
- translating everyday statements into Boolean expressions
- exercises with worked solutions
- Norwegian complete, English parity started

## M2 — Algebra and Simplification

Goal: teach Boolean manipulation without assuming prior algebra expertise.

- identity, domination, idempotence and complement laws
- commutative, associative and distributive laws
- absorption
- De Morgan's laws
- algebraic simplification
- equivalence checking using truth tables

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
