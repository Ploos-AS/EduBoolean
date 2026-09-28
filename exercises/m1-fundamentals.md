# M1 – Oppgaver: Boolean Fundamentals

Forsøk selv før du ser fasiten.

## A – Grunnverdier

1. Hva er de to boolske sannhetsverdiene?
2. Hvis `door_open = 0`, er påstanden «døren er åpen» sann eller usann?
3. Hva blir NOT 0 og NOT 1?

## B – AND og OR

4. Beregn `1 AND 1`.
5. Beregn `1 AND 0`.
6. Beregn `0 OR 1`.
7. Beregn `1 OR 1`.

## C – XOR

8. Beregn `0 XOR 0`.
9. Beregn `0 XOR 1`.
10. Beregn `1 XOR 1`.
11. Forklar med egne ord forskjellen mellom OR og XOR for to innganger.

## D – Sammensatte uttrykk

12. Beregn `NOT 1 OR 0`.
13. Beregn `NOT (1 AND 0)`.
14. Beregn `(1 XOR 0) AND 1`.
15. Lag sannhetstabell for `A AND (NOT B)`.

## Fasit

1. Sant og usant, ofte representert som 1 og 0.
2. Usann.
3. 1 og 0.
4. 1.
5. 0.
6. 1.
7. 1.
8. 0.
9. 1.
10. 0.
11. OR er sann når minst én inngang er sann; XOR er for to innganger sann når nøyaktig én er sann.
12. 0.
13. 1.
14. 1.
15.

| A | B | NOT B | A AND (NOT B) |
|---:|---:|---:|---:|
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |

Hvis et svar var feil, gå tilbake til operasjonen som ga problemet og bygg tabellen steg for steg.
