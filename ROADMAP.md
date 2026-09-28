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

- [x] gate concepts and Boolean operations
- [x] expression ↔ gate network
- [x] introductory propagation concepts
- [x] half adder and full adder
- [x] multi-bit ripple-carry addition
- [x] multiplexers
- [x] decoders and encoders
- [x] comparators
- [x] worked exercises and practical labs

**M3 core status: COMPLETE.**

## M4 — Karnaugh Maps

Goal: provide a visual simplification method.

- [x] 2-variable maps
- [x] Gray-code adjacency
- [x] 3-variable maps
- [x] 4-variable maps
- [x] grouping rules, wrap-around and overlap
- [x] don't-care conditions
- [x] translating groups into expressions
- [x] compare K-map and algebraic simplification
- [x] exercises and optimization lab

**M4 core status: COMPLETE.**

## M5 — Sequential Logic

Goal: introduce state and memory as the next conceptual step.

- [x] why combinational logic is not enough
- [x] feedback and stored state
- [x] SR latch and D latch
- [x] clock, levels and edges
- [x] edge-triggered D flip-flop
- [x] registers and shift registers
- [x] synchronous counter
- [x] current-state / next-state model
- [x] transition from Boolean algebra toward finite state machines
- [x] exercises and 2-bit counter lab

**M5 core status: COMPLETE.**

EduFSM is a natural follow-on course for deeper treatment of state machines.

## M6 — From Logic to CPU

Goal: connect course concepts to computer architecture.

- [x] n-bit adders as CPU building blocks
- [x] ALU functions and result selection
- [x] Zero, Carry, Negative and Overflow flags
- [x] register selection and write enable
- [x] opcode decoding
- [x] control signals
- [x] program counter and conditional branch
- [x] FETCH/EXECUTE control-state model
- [x] small CPU datapath example
- [x] mini-ALU and CPU trace labs
- [x] bridge to EduCPU and EduK8

**M6 core status: COMPLETE.**

## M7 — Boolean Logic in Software

Goal: make the same ideas recognizable in programming.

- [x] Boolean types
- [x] comparisons
- [x] `if` conditions and control flow
- [x] logical operators in Python and C
- [x] short-circuit evaluation and side-effect caveats
- [x] bitwise versus logical operations
- [x] masks
- [x] permissions and feature flags
- [x] De Morgan in software
- [x] truth tables as exhaustive test design
- [x] practical C and Python examples and labs

**M7 core status: COMPLETE.**

## M8 — EduLogic Simulator

Goal: make the course interactive.

Capabilities:

- [x] switches and LEDs teaching metadata
- [x] NOT/AND/OR/XOR/NAND/NOR/XNOR gates
- [x] signal introspection foundation for wire highlighting
- [x] automatic truth-table generation
- [x] combinational circuit evaluation
- [x] versioned JSON save/load circuit format
- [x] deterministic core independent of UI
- [x] headless CLI
- [x] unit tests and half-adder qualification example
- [x] reusable declarative test-vector format and CLI runner
- [ ] explicit sequential clock/state model
- [ ] later HDL export/import experiments

**M8 status: IN PROGRESS.** The deterministic combinational core is now usable; visualization, teaching metadata and sequential semantics remain.

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
