# 43 – ALU: arithmetic logic unit

ALU-en utfører aritmetiske og logiske operasjoner.

Tenk deg en enkel ALU med to 4-bits innganger:

```text
A[3:0]
B[3:0]
```

og operasjoner:

```text
ADD
AND
OR
XOR
```

Vi kan beregne alle kandidatresultatene parallelt:

```text
add_result = A + B
and_result = A AND B
or_result  = A OR B
xor_result = A XOR B
```

Deretter velger en MUX hvilket resultat som skal bli ALU-utgangen.

## Viktig idé

Kontrollsignalene gjør ikke selve regningen. De **velger hvilken datapath** resultatet skal følge.

Dette kobler MUX-kapitlet direkte til CPU-design.

Neste: [CPU-flagg](44-flagg.md).
