# 32 – Fra logikk til minne

Alle kretsene hittil har vært **kombinatoriske**:

```text
utgang = funksjon av inngangene akkurat nå
```

Hvis inngangene endres, endres utgangen etter kretsens propagasjonsforsinkelse. Kretsen husker ikke hva som skjedde før.

Men en datamaskin trenger hukommelse:

- registre må beholde verdier
- tellere må vite forrige tall
- kontrollenheten må vite hvilken tilstand den er i

Dette krever **sekvensiell logikk**.

En forenklet idé er:

```text
neste utgang = funksjon av inngang + tidligere tilstand
```

Nøkkelen er feedback: et signal fra kretsens utgang kan føres tilbake og påvirke kretsen selv.

Neste: [SR-latch](33-sr-latch.md).
