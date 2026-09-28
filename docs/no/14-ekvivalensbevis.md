# 14 – Bevis ekvivalens med sannhetstabell

Algebraisk forenkling kan inneholde feil. Sannhetstabellen gir oss en uavhengig kontrollmetode.

Vi vil kontrollere:

```text
(A AND B) OR (A AND NOT B) = A
```

| A | B | A AND B | NOT B | A AND NOT B | venstre side | A |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 0 | 0 | 1 | 1 |

De to siste kolonnene er like på alle rader. Uttrykkene er derfor ekvivalente.

## To komplementære metoder

**Algebra** forklarer hvordan vi kan transformere uttrykket.

**Sannhetstabellen** kontrollerer funksjonen direkte.

Å kunne bruke begge er viktig.

## M2-sjekk

Du bør nå kunne:

- forklare hva boolsk ekvivalens betyr
- bruke grunnlovene
- bruke kommutative, assosiative og distributive lover
- bruke absorpsjon
- bruke De Morgans lover
- forenkle et uttrykk steg for steg
- kontrollere ekvivalens med sannhetstabell

Neste milepæl kobler uttrykkene direkte til fysiske/logiske porter og kombinatoriske kretser.
