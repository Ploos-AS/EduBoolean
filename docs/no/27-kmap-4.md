# 27 – K-map med fire variabler

Fire variabler gir 16 celler.

| AB \ CD | 00 | 01 | 11 | 10 |
|---|---:|---:|---:|---:|
| 00 |  |  |  |  |
| 01 |  |  |  |  |
| 11 |  |  |  |  |
| 10 |  |  |  |  |

Både rader og kolonner bruker Gray-rekkefølge.

## Naboskap

Hver celle har logiske naboer til venstre, høyre, over og under. Kantene vikler seg rundt.

Fire hjørneceller kan derfor danne én gruppe på fire.

## Praktisk strategi

1. Fyll kartet korrekt.
2. Finn grupper med 8 først.
3. Deretter grupper med 4.
4. Så grupper med 2.
5. Bruk enkeltceller bare når nødvendig.
6. Kontroller at alle ettall er dekket.

Størst gruppe betyr flest eliminerte variabler.

Neste: [Fra gruppe til uttrykk](28-gruppe-til-uttrykk.md).
