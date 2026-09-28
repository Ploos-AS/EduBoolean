# Lab 7 – Design en 2-bits synkron teller

## Mål

Design en teller med tilstandene:

```text
00 → 01 → 10 → 11 → 00
```

Bruk to lagringsbits:

```text
Q1 Q0
```

## Del 1 – Tilstandstabell

| current Q1 | current Q0 | next Q1 | next Q0 |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |

## Del 2 – Finn neste-bit-funksjonene

Studer tabellen.

Q0 skifter ved hvert steg:

```text
next_Q0 = NOT Q0
```

For Q1:

```text
next_Q1 = Q1 XOR Q0
```

## Del 3 – Implementasjon

Bruk:

- to D-flip-flopper
- én NOT-funksjon
- én XOR-funksjon
- felles klokke

Koble neste_Q0 til D på første flip-flop og next_Q1 til D på den andre.

## Del 4 – Spor manuelt

Start i 00 og gå minst åtte klokkehendelser. Skriv tilstanden etter hver hendelse.

Du har nå bygget et komplett lite synkront sekvensielt system: kombinatorisk next-state-logikk + register.
