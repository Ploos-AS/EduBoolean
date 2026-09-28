# 17 – Halvaddereren

En halvadder legger sammen to én-bits tall.

Innganger:

```text
A, B
```

Utganger:

```text
SUM, CARRY
```

| A | B | SUM | CARRY |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

Vi kjenner igjen:

```text
SUM   = A XOR B
CARRY = A AND B
```

Dermed kan en halvadder bygges med én XOR-port og én AND-port.

Hvorfor heter den **halv**adder? Den kan ikke ta imot carry fra en tidligere bitposisjon.

Neste: [Fulladdereren](18-fulladder.md).
