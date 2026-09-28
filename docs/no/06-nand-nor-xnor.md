# 6 – NAND, NOR og XNOR

Disse operasjonene kan forstås ved å kombinere operasjoner vi allerede kjenner.

## NAND

```text
A NAND B = NOT (A AND B)
```

| A | B | NAND |
|---:|---:|---:|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

## NOR

```text
A NOR B = NOT (A OR B)
```

Resultatet er 1 bare når begge inngangene er 0.

## XNOR

```text
A XNOR B = NOT (A XOR B)
```

For to innganger er resultatet 1 når inngangene er like.

## Hvorfor NAND og NOR er spesielle

NAND og NOR er universelle: hele boolske funksjoner kan bygges bare med NAND-porter eller bare med NOR-porter. Vi beviser og bygger dette senere.

Neste: [Sannhetstabeller](07-sannhetstabeller.md).
