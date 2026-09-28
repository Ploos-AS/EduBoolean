# 58 – Bitmasker

En bitmaske lar oss velge bestemte bits i en verdi.

Anta:

```text
flags = 10110100
mask  = 00000100
```

For å teste den markerte biten kan vi bruke bitvis AND:

```text
flags AND mask
```

Hvis resultatet ikke er null, er den aktuelle biten satt.

C:

```c
if ((flags & mask) != 0) {
    /* bit is set */
}
```

Python:

```python
if (flags & mask) != 0:
    print("bit is set")
```

## Sette og fjerne bits

Sette bits:

```text
flags = flags OR mask
```

Fjerne bits:

```text
flags = flags AND (NOT mask)
```

Her bruker programvaren nøyaktig de bitvise operasjonene vi lærte som logiske porter.

Neste: [Flagg og permissions](59-flagg-permissions.md).
