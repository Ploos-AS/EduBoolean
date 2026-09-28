# Lab 2 – Bygg en halvadderer med logikk

Denne labben krever ingen fysisk maskinvare. Du kan arbeide på papir eller i en valgfri logikksimulator.

## Oppgave

Vi skal legge sammen to én-bits tall, A og B.

Fyll først ut vanlig binær addisjon:

| A | B | Sum | Carry |
|---:|---:|---:|---:|
| 0 | 0 | ? | ? |
| 0 | 1 | ? | ? |
| 1 | 0 | ? | ? |
| 1 | 1 | ? | ? |

Sammenlign deretter kolonnen **Sum** med sannhetstabellen til XOR, og **Carry** med sannhetstabellen til AND.

## Løsning

```text
SUM   = A XOR B
CARRY = A AND B
```

| A | B | Sum | Carry |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

Du har nå konstruert den logiske funksjonen til en **halvadderer**.

## Tenk videre

Hvorfor trenger vi to utganger når vi beregner 1 + 1? Svaret er at resultatet binært er `10`: sumbiten er 0 og carry-biten er 1.

Dette er den første konkrete forbindelsen mellom boolsk algebra og aritmetikken i en CPU.
