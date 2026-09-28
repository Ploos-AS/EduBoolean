# EduLogic circuit format v1

The first format is deliberately small and JSON-based.

Required top-level fields:

- `format`: must be `edulogic-1`
- `inputs`: named primary input signals
- `outputs`: named observable output signals
- `gates`: gate objects

A gate contains:

```json
{"type":"XOR","inputs":["A","B"],"output":"SUM"}
```

M8 supports `NOT`, `AND`, `OR`, `XOR`, `NAND`, `NOR` and `XNOR`.

The combinational evaluator is deterministic. Combinational cycles cannot settle in this model and are rejected. Sequential state is represented explicitly by the `state` section described below; it never acquires timing semantics from accidental combinational feedback.


## Teaching metadata

Optional UI-neutral teaching metadata maps named signals to controls or indicators:

```json
"teaching": {
  "switches": [{"signal":"A","label":"Input A"}],
  "leds": [{"signal":"SUM","label":"Sum"}]
}
```

The core validates these references but does not render them. A future CLI, web or desktop frontend can choose how switches and LEDs look.

## Test vectors

Qualification vectors use a separate versioned document:

```json
{
  "format":"edulogic-vectors-1",
  "circuit":"half-adder",
  "vectors":[
    {"inputs":{"A":1,"B":1},"expect":{"SUM":0,"CARRY":1}}
  ]
}
```

This keeps circuit design separate from expected behavior and allows the same vectors to be reused by CI and future frontends.

## Signal introspection

The core can return all settled named signals, not only primary outputs. This allows teaching tools to highlight intermediate nets without changing evaluation semantics.


## Sequential state

M8 models synchronous state explicitly. A D flip-flop is declared separately from combinational gates:

```json
"state": [
  {"type":"DFF","d":"D0","q":"Q0","initial":0}
]
```

A deterministic tick has two phases:

1. settle all combinational logic using the current Q values
2. atomically sample each D signal and replace all Q values together

There is no wall-clock, implicit propagation time or accidental update order. Repeated ticks therefore produce reproducible state traces.

The initial M8 state model intentionally supports DFF cells as the primitive. Multi-bit registers and synchronous counters can be composed from multiple DFF cells; richer components may later be added as validated convenience abstractions.


## Register and counter convenience cells

DFF remains the primitive sequential reference model. M8 also supports compact synchronous teaching components.

A register declares a width and one D signal per bit:

```json
{"type":"REGISTER","q":"Q","width":2,"d":["D0","D1"],"enable":"EN","reset":"RST"}
```

A counter can be declared as:

```json
{"type":"COUNTER","q":"Q","width":4,"enable":"EN","reset":"RST"}
```

Bits are named from least significant upward as `Q[0]`, `Q[1]`, etc.

Control priority on a tick is deliberately explicit:

1. asserted synchronous `reset` clears the component
2. deasserted `enable` holds the old state
3. otherwise REGISTER samples D or COUNTER advances

## Sequential qualification vectors

`edulogic-sequence-1` describes a deterministic list of ticks. Every step supplies input values and expected post-tick state. This allows reset, enable, counters, registers and later finite-state machines to be qualified without wall-clock timing.


## Qualification CLI

Combinational qualification:

```sh
python3 edulogic.py examples/half-adder.json --vectors examples/half-adder.vectors.json
```

Sequential qualification:

```sh
python3 edulogic.py examples/counter4-control.json --sequence examples/counter4-control.sequence.json
```

Truth tables are intentionally limited to circuits without state. Stateful behavior must be observed with deterministic ticks or a versioned sequence suite. Vector and sequence suites validate their format version and, when supplied, their target circuit name.


## M8 v1 format contract

The three M8 document identifiers are now treated as versioned compatibility contracts:

- `edulogic-1` — circuit structure and deterministic reference semantics
- `edulogic-vectors-1` — complete combinational input/output qualification
- `edulogic-sequence-1` — complete synchronous tick/state qualification

A v1 qualification suite is deliberately fail-closed. Every combinational vector must specify every primary input and every observable output. Every sequential step must specify every primary input and the complete post-tick state. Unknown names, missing names, wrong format versions and a mismatched optional `circuit` target are errors rather than partial checks.

### Compatibility rule

Once M8 is qualified, existing v1 documents must keep their meaning. Additions that would change how an existing valid v1 document evaluates require a new format version. New optional metadata may be added only when older v1 behavior remains unchanged.

The deterministic semantic order for a sequential tick is:

1. current state and primary inputs are visible
2. combinational logic settles
3. synchronous reset is evaluated
4. otherwise disabled cells hold
5. otherwise DFF/REGISTER inputs are sampled or COUNTER advances
6. all state updates become visible atomically

The reference model uses only binary 0/1 logic. HDL `X`/`Z`, propagation delay, asynchronous reset and implicit wall-clock behavior are outside the v1 contract.
