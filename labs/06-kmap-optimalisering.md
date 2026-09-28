# Lab 6 – Fra sannhetstabell til mindre krets

## Mål

Bruk hele arbeidsflyten:

```text
sannhetstabell → K-map → grupper → uttrykk → portnettverk
```

Bruk tre innganger A, B og C med funksjonen:

| A | B | C | F |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

1. Plasser verdiene i et 3-variabel K-map.
2. Finn størst mulig gruppe.
3. Finn hvilke variabler som varierer.
4. Skriv det forenklede uttrykket.
5. Bygg eller tegn kretsen.
6. Kontroller mot originaltabellen.

## Resultat

Alle cellene med B=1 har F=1, uansett A og C.

Dermed:

```text
F = B
```

En funksjon som kunne vært presentert som mange minterms reduseres til én enkelt variabel.
