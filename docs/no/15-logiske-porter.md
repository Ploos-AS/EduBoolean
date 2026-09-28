# 15 – Fra boolsk uttrykk til logiske porter

En logisk port er en krets som implementerer en boolsk operasjon.

- NOT → inverter
- AND → AND-port
- OR → OR-port
- XOR → XOR-port
- NAND, NOR og XNOR → tilsvarende inverterte funksjoner

Et uttrykk som:

```text
F = (A AND B) OR C
```

kan bygges ved først å sende A og B inn i en AND-port og deretter sende resultatet og C inn i en OR-port.

## Viktig idé

Samme funksjon kan beskrives på flere måter:

```text
krav i vanlig språk
→ boolsk uttrykk
→ sannhetstabell
→ portnettverk
```

Alle beskriver den samme logiske funksjonen.

## Signalflyt

I en kombinatorisk krets bestemmes utgangen av inngangene som finnes akkurat nå. Kretsen trenger ikke å huske tidligere verdier.

Senere lærer vi sekvensiell logikk, hvor historikk og tilstand også betyr noe.

Neste: [Fra uttrykk til krets](16-uttrykk-til-krets.md).
