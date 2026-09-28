# 50 – En minimal pedagogisk datapath

Vi kan nå skissere en liten CPU:

```text
             +-----------+
register A -->|           |
register B -->|    ALU    |----> result
             |           |
             +-----------+
                   |
                 flags

opcode ---> control logic ---> ALU select / register write / PC control

PC ---> instruction memory ---> instruction ---> control
```

Dette er forenklet, men alle hoveddelene bygger på konsepter fra kurset.

## Spor en ADD

Anta:

```text
A = 0011
B = 0101
opcode = ADD
```

1. Registerverdiene går til ALU.
2. Kontrollogikken velger ADD.
3. Adderen produserer `1000`.
4. Flagg beregnes.
5. Hvis REG_WRITE er aktiv, lagres resultatet ved riktig klokkehendelse.

Boolsk logikk bestemmer både datapath-resultater og kontrollvalg.

Neste: [Fra EduBoolean til EduCPU](51-broen-til-educpu.md).
