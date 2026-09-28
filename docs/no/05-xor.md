# 5 – XOR: nøyaktig én

XOR betyr exclusive OR. For to innganger er resultatet sant når inngangene er forskjellige.

| A | B | A XOR B |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

XOR er viktig i blant annet addere, paritetsberegning og bitoperasjoner.

## Første møte med en adderer

Når vi legger sammen én bit A og én bit B uten innkommende carry, er selve sumbiten:

```text
SUM = A XOR B
```

Carry-biten er:

```text
CARRY = A AND B
```

Dermed har vi allerede nok logikk til å bygge en **halvadderer** senere i kurset.

Neste: [NAND, NOR og XNOR](06-nand-nor-xnor.md).
