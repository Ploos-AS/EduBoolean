# Lab 8 – Design en mini-ALU

Design en 4-bits ALU med operasjonene:

| OP | funksjon |
|---|---|
| 00 | A AND B |
| 01 | A OR B |
| 10 | A XOR B |
| 11 | A + B |

## Byggemetode

1. Lag fire kandidatresultater.
2. Bruk en 4-til-1 MUX per resultatbit, eller tilsvarende hierarkisk MUX-logikk.
3. La OP velge resultatet.
4. Beregn Zero-flagget fra valgt resultat.
5. For ADD, observer carry-out.

## Test

Test blant annet:

```text
A=0011 B=0101
A=1111 B=0001
A=1010 B=1010
A=0000 B=0000
```

Prøv alle fire OP-verdier for hver test.

## Utfordring

Legg til en femte intern kandidat, NOT A. Hvordan må kontrollkodingen eller MUX-strukturen endres?
