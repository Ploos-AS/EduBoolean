# 47 – Kontrollsignaler

Datapathen flytter og behandler data. Kontrollsignalene bestemmer hva datapathen skal gjøre.

Eksempler:

```text
ALU_OP
REG_WRITE
SRC_SELECT
PC_LOAD
MEM_READ
MEM_WRITE
```

Disse er i bunn og grunn boolske eller små binære signaler.

## Eksempel

En ADD-instruksjon kan kreve:

```text
ALU_OP    = ADD
REG_WRITE = 1
```

mens en sammenligningsoperasjon kanskje oppdaterer flagg uten å skrive ALU-resultatet til et generelt register.

## Kontroll som logisk funksjon

Kontrollsignaler kan beregnes fra:

```text
opcode + current_state + flags
```

Dermed møter vi igjen både boolsk kombinatorikk og sekvensiell state.

Neste: [Program counter](48-program-counter.md).
