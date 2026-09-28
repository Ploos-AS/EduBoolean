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

The evaluator is combinational and deterministic. Cycles cannot settle in this model and are rejected. Sequential state will use an explicit future format/model rather than giving combinational feedback accidental timing semantics.


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
