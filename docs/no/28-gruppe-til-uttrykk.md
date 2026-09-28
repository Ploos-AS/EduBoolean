# 28 – Fra K-map-gruppe til uttrykk

For hver gruppe spør vi:

> Hvilke variabler har samme verdi i alle cellene?

Variabler som endrer verdi inne i gruppen fjernes.

## Eksempel

Anta at en gruppe dekker fire celler hvor:

- A alltid er 1
- B varierer
- C varierer
- D alltid er 0

Da beskrives gruppen av:

```text
A AND NOT D
```

B og C er irrelevante for denne gruppen.

Hvis flere grupper trengs, OR-er vi gruppeuttrykkene sammen.

## Hvor mye forsvinner?

For en funksjon med n variabler:

- gruppe på 1 eliminerer 0 variabler
- gruppe på 2 eliminerer 1
- gruppe på 4 eliminerer 2
- gruppe på 8 eliminerer 3

Dette forklarer hvorfor store grupper er attraktive.

Neste: [Wrap-around og overlapp](29-wrap-overlap.md).
