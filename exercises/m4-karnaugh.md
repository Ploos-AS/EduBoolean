# M4 – Oppgaver: Karnaugh-kart

## 1 – Gray-kode

Sett disse i riktig K-map-rekkefølge:

```text
00, 10, 11, 01
```

## 2 – Gruppestørrelser

Hvilke er gyldige K-map-gruppestørrelser?

```text
1, 2, 3, 4, 6, 8
```

## 3 – To variabler

| A \ B | 0 | 1 |
|---|---:|---:|
| 0 | 0 | 0 |
| 1 | 1 | 1 |

Hva er det forenklede uttrykket?

## 4 – Eliminering

I en gruppe er A alltid 0, B varierer og C alltid 1. Hvilket produktledd beskriver gruppen?

## 5 – Konsepter

Forklar:

- hvorfor kantene kan være naboer
- hvorfor diagonaler ikke er naboer
- hvorfor grupper kan overlappe
- hva X betyr i et K-map

## Fasit

1. `00, 01, 11, 10`.
2. 1, 2, 4 og 8.
3. `A`.
4. `(NOT A) AND C`; B elimineres.
5. Kantene følger fortsatt én-bits Gray-naboskap; diagonaler gjør normalt ikke det. Overlapp er tillatt fordi hver gruppe representerer et gyldig implicant. X er en don't-care som kan brukes som 0 eller 1 når spesifikasjonen tillater det.
