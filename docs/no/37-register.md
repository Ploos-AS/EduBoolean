# 37 – Fra én bit til register

Én D-flip-flop kan lagre én bit.

Hvis vi plasserer flere ved siden av hverandre og lar dem dele klokke, kan vi lagre flere bits samtidig.

Et 4-bits register kan representeres:

```text
D3 D2 D1 D0
 |  |  |  |
[FF][FF][FF][FF]
 |  |  |  |
Q3 Q2 Q1 Q0
```

Ved klokkehendelsen lagres hele ordet.

## CPU-koblingen

CPU-registre som programtelleren, instruksjonsregisteret og generelle registre bygger på samme grunnidé: grupper av lagringsceller som holder binære verdier.

Virkelige registerfiler kan være langt mer avanserte, men konseptet starter her.

Neste: [Shift-register](38-shift-register.md).
