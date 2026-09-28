# Lab 1 – Brytere, tilstander og logikk

Denne labben krever ingen fysisk maskinvare.

## Mål

Etter labben skal du kunne:

- beskrive en virkelig situasjon med boolske variabler
- skille mellom navn, betydning og verdi
- lage en enkel logisk regel med AND

## Scenario

Vi lager en enkel nattlampe.

Lampen skal være på bare når:

1. det er mørkt
2. lampens bryter er aktivert

Definer:

```text
M = 1 når det er mørkt
B = 1 når bryteren er aktivert
L = 1 når lampen skal være på
```

Regelen er:

```text
L = M AND B
```

## Test alle muligheter

Fyll inn siste kolonne før du ser løsningen:

| M | B | L |
|---|---|---|
| 0 | 0 | ? |
| 0 | 1 | ? |
| 1 | 0 | ? |
| 1 | 1 | ? |

## Løsning

| M | B | L |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

Dette er vår første **sannhetstabell**.

## Tenk videre

Hva måtte endres dersom lampen skulle være på når *enten* det er mørkt *eller* bryteren er aktivert?

Vi har nettopp møtt forskjellen mellom AND og OR. Senere bygger vi den samme regelen med logiske porter i simulator og eventuelt fysisk maskinvare.

## Ekstraoppgave

Lag selv en regel for en alarm med disse signalene:

```text
D = døren er åpen
A = alarmen er aktivert
S = sirenen skal gå
```

Skriv regelen med ord først, og deretter som et uttrykk med `AND`.
