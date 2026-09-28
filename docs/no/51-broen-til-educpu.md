# 51 – Fra EduBoolean til EduCPU

EduBoolean forklarer nå hvordan enkle logiske byggesteiner kan settes sammen til CPU-strukturer.

Men et komplett CPU-kurs trenger mer:

- instruksjonssett og ISA-design
- assembler
- adresseringsmodi
- minnekart
- stack
- interrupts
- busser
- HDL/FPGA-implementasjon
- verktøykjede

Dette er naturlige temaer for **EduCPU**.

## Det viktige resultatet

En CPU er ikke lenger en svart boks.

Studenten har sett kjeden:

```text
0/1
→ boolske operasjoner
→ porter
→ kombinatoriske kretser
→ addere/MUX/dekodere
→ flip-flopper og registre
→ state
→ ALU + kontroll + PC
→ CPU
```

## M6-sjekk

Du skal nå kunne forklare:

- hvordan en ALU kan velge mellom operasjoner
- hvorfor CPU-flagg er boolske funksjoner
- hvordan registre velges
- hvordan opcode-bits kan bli kontrollsignaler
- hvordan PC kan oppdateres eller branches
- hvorfor CPU-kontroll trenger state
- hvordan kursdelene henger sammen i en datapath
