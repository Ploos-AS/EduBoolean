# 20 – Multiplexer: velg ett signal

En multiplexer, ofte forkortet **MUX**, velger hvilken av flere innganger som skal sendes til utgangen.

For en 2-til-1 MUX har vi:

- datainngang A
- datainngang B
- valgbit S
- utgang F

| S | F |
|---:|---|
| 0 | A |
| 1 | B |

Boolsk:

```text
F = ((NOT S) AND A) OR (S AND B)
```

## Hvor brukes MUX?

En CPU må stadig velge mellom signaler:

- hvilket register skal leses?
- skal ALU-en bruke et register eller en konstant?
- hvilken verdi skal skrives tilbake?

MUX-er er derfor sentrale byggeklosser i datapaths.

Neste: [Dekodere og encodere](21-dekoder-encoder.md).
