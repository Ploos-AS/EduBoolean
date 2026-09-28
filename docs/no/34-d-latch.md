# 34 – D-latch

SR-latchens separate Set/Reset-innganger er ikke alltid praktiske.

En D-latch har:

- D – data
- Enable – når lagringen kan oppdateres
- Q – lagret verdi

For en aktiv-høy D-latch:

- når Enable=1, følger Q inngangen D
- når Enable=0, beholder Q siste verdi

Dette kalles **level-sensitive** oppførsel.

## Eksempel

Hvis D blir 1 mens Enable er 1, blir Q 1. Når Enable deretter blir 0, kan D endres uten at Q følger etter.

Vi har altså en enkel én-bits lagringscelle.

Neste: [Klokke og tid](35-klokke.md).
