# 46 – Opcode: binære bits blir en handling

En instruksjon inneholder bits som CPU-en tolker.

Anta en svært liten 2-bits opcode:

| opcode | operasjon |
|---|---|
| 00 | ADD |
| 01 | AND |
| 10 | OR |
| 11 | XOR |

En dekoder eller annen kontrollogikk kan oversette opcode til kontrollsignaler.

For eksempel:

```text
opcode = 10
→ velg OR-resultatet fra ALU
```

## Instruksjonen er data

For maskinvaren er opcode bare bits. Betydningen oppstår fordi kontrollogikken er designet til å reagere på bestemte bitmønstre.

Dette er en viktig kobling mellom boolsk algebra og en instruksjonsarkitektur.

Neste: [Kontrollsignaler](47-kontrollsignaler.md).
