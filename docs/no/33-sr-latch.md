# 33 – SR-latch: vår første hukommelse

En latch kan beholde en tilstand selv etter at inngangssignalet som satte den, er borte.

En klassisk SR-latch har innganger:

- S – Set
- R – Reset

og en lagret utgang Q.

Konseptuelt ønsker vi:

| S | R | handling |
|---:|---:|---|
| 0 | 0 | behold tidligere Q |
| 1 | 0 | set Q |
| 0 | 1 | reset Q |
| 1 | 1 | avhenger av implementasjonen / uønsket kombinasjon i grunnmodellen |

## Det nye

Raden `S=0, R=0` kan ikke beskrives uten å kjenne **tidligere Q**.

Dette er fundamentalt forskjellig fra en ren AND- eller OR-port.

## Viktig presisering

SR-latcher kan bygges med krysskoblede NOR- eller NAND-porter, men inngangspolariteten og tabellen er forskjellig mellom variantene. Kurset skiller derfor mellom den abstrakte funksjonen og den konkrete portimplementasjonen.

Neste: [D-latch](34-d-latch.md).
