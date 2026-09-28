# 36 – D-flip-flop

En edge-triggered D-flip-flop lagrer D på en bestemt klokke**flanke**.

For en positiv-flanke-triggeret variant:

```text
ved stigende klokke:
    Q ← D
ellers:
    Q beholdes
```

Dette skiller den fra en level-sensitive D-latch.

## Eksempel

Rett før stigende flanke:

```text
D = 1
Q = 0
```

Ved flanken lagres D:

```text
Q = 1
```

D kan deretter endres, men Q beholder verdien frem til neste relevante flanke.

Dette er en sentral byggestein for synkrone registre.

Neste: [Register](37-register.md).
