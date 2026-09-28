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
