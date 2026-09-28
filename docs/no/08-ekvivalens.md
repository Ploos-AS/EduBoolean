# 8 – Når to uttrykk betyr det samme

To boolske uttrykk er **ekvivalente** når de gir samme resultat for alle mulige innganger.

Vi skriver ofte:

```text
A AND 1 = A
```

Dette betyr ikke vanlig tallregning. Det betyr at venstre og høyre side alltid har samme sannhetsverdi.

## Bevis med sannhetstabell

| A | A AND 1 | A |
|---:|---:|---:|
| 0 | 0 | 0 |
| 1 | 1 | 1 |

Kolonnene er identiske. Dermed er uttrykkene ekvivalente.

Dette gir oss en viktig metode: Hvis vi er usikre på en boolsk regel, kan vi kontrollere den ved å lage sannhetstabell.

Neste: [De grunnleggende lovene](09-grunnlover.md).
