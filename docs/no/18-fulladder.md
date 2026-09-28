# 18 – Fulladdereren

En fulladder legger sammen tre én-bits verdier:

- A
- B
- carry-in, skrevet Cin

og produserer:

- SUM
- carry-out, skrevet Cout

## Sannhetstabell

| A | B | Cin | SUM | Cout |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

Sumbiten kan skrives:

```text
SUM = A XOR B XOR Cin
```

Carry kan blant annet skrives:

```text
Cout = (A AND B) OR (Cin AND (A XOR B))
```

En fulladder kan også bygges av **to halvadderere og én OR-port**. Dette viser et viktig prinsipp: små logiske blokker kan brukes som byggeklosser for større blokker.

Neste: [Flerbits addisjon](19-ripple-carry.md).
