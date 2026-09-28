# Lab 5 – Bygg en 2-til-1 multiplexer

Implementer:

```text
F = ((NOT S) AND A) OR (S AND B)
```

Bruk bare NOT, AND og OR.

## Test

Prøv alle kombinasjoner av A, B og S. Kontroller spesielt:

- når S=0 skal F alltid følge A
- når S=1 skal F alltid følge B

## Ekstra

Bygg samme funksjon med en ferdig MUX-komponent i simulatoren din og sammenlign sannhetstabellene.

## Kobling til CPU

Tenk deg at A er et register og B er en konstant. S kan da være et kontrollsignal som bestemmer hvilken verdi ALU-en mottar.
