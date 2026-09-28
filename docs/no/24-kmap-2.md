# 24 – K-map med to variabler

Med A og B finnes fire inngangskombinasjoner.

Et 2-variabelkart kan tegnes:

| A \ B | 0 | 1 |
|---|---:|---:|
| 0 | m0 | m1 |
| 1 | m2 | m3 |

Vi fyller hver celle med funksjonens utgang, 0 eller 1.

## Eksempel

Funksjonen er 1 når A=1, uansett B:

| A \ B | 0 | 1 |
|---|---:|---:|
| 0 | 0 | 0 |
| 1 | 1 | 1 |

De to ettallene grupperes. B er 0 i den ene cellen og 1 i den andre, så B varierer og forsvinner. A er alltid 1.

Resultat:

```text
F = A
```

## Regel

I en gruppe beholder vi bare variablene som er konstante gjennom hele gruppen.

Neste: [Gray-kode og naboskap](25-gray-naboskap.md).
