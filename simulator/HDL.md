# EduLogic HDL bridge

M8 provides an initial **Verilog-2001 export** path. It is intentionally conservative: EduLogic remains the source model, while generated HDL is an educational/synthesis bridge.

## CLI

```bash
python3 edulogic.py examples/half-adder.json --verilog
python3 edulogic.py examples/counter4-control.json --verilog
```

## Mapping

- NOT → `~`
- AND → `&`
- OR → `|`
- XOR → `^`
- NAND/NOR/XNOR → inversion of the corresponding expression
- DFF/REGISTER/COUNTER → `always @(posedge clk)` with nonblocking assignments

Sequential reset is synchronous, matching the EduLogic tick model. Reset has priority over enable. `initial` defines the deterministic start state of the EduLogic reference model; the Verilog bridge deliberately does not claim a portable hardware power-up state. Sequential RTL qualification must establish known state through reset when hardware-equivalent startup matters.

## Scope

The exporter is not a general HDL compiler. M8 does not yet import arbitrary Verilog, model propagation delay, tri-state buses, unknown `X/Z` values, asynchronous reset, multiple clocks or analog behavior.

Generated HDL should be treated as a transparent learning bridge that can later be qualified with an external HDL toolchain and FPGA flow.


## Automated qualification

The `EduLogic` GitHub Actions workflow:

1. runs the Python simulator unit tests
2. delegates HDL qualification to `Ploos-AS/hardware-ci`
3. regenerates the half-adder HDL and compares it with the checked-in golden output
4. compiles and simulates the half-adder testbench with Icarus
5. generates counter RTL and its testbench from the versioned EduLogic sequence oracle
6. simulates reset, enable, hold and counting behavior with Icarus
7. checks the declared HDL with Yosys and runs the EduLogic conformance commands

A green workflow therefore checks both the EduLogic reference model and an independent HDL implementation path.
