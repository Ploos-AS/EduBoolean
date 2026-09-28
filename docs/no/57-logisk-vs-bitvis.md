# 57 – Logiske og bitvise operatorer er ikke det samme

Dette skillet er svært viktig.

I C:

```text
&&  logisk AND
||  logisk OR
!   logisk NOT

&   bitvis AND
|   bitvis OR
^   bitvis XOR
~   bitvis NOT
```

Bitvise operatorer arbeider separat på bitposisjonene i heltallsverdier.

Eksempel:

```text
  1010
& 1100
------
  1000
```

## Python

Python har:

```text
and or not
```

for logiske uttrykk, og:

```text
& | ^ ~
```

for bitvise heltallsoperasjoner.

Detaljene rundt operand- og returverdier varierer mellom språk. Derfor skal vi forstå konseptet og samtidig følge reglene til språket vi bruker.

Neste: [Bitmasker](58-bitmasker.md).
