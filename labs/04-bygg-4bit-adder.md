# Lab 4 – Bygg en 4-bits adderer

## Mål

Bygg opp en større funksjon ved å gjenbruke fulladderen som komponent.

Lag fire fulladdere:

```text
FA0  bit 0
FA1  bit 1
FA2  bit 2
FA3  bit 3
```

Koble `Cout` fra FA0 til `Cin` på FA1, og fortsett tilsvarende oppover.

For den første biten bruker du `Cin = 0`.

## Testvektorer

Test minst:

```text
0000 + 0000
0001 + 0001
0101 + 0011
0111 + 0001
1111 + 0001
1111 + 1111
```

Noter både de fire sumbitene og siste Cout.

## Viktig observasjon

Fire utgangsbiter er ikke alltid nok til å representere resultatet. `1111 + 0001` produserer carry ut av den øverste biten.

Denne carry-en blir senere relevant når vi diskuterer CPU-flagg og ordstørrelse.
