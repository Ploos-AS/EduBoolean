# 16 – Fra uttrykk til krets

Vi bygger:

```text
F = (A OR B) AND (NOT C)
```

Del uttrykket opp:

```text
X = A OR B
Y = NOT C
F = X AND Y
```

Nå trenger vi én OR-port, én NOT-port og én AND-port.

## Fra krets tilbake til uttrykk

Metoden virker også motsatt:

1. Finn utgangen.
2. Se hvilken port som driver den.
3. Skriv operasjonen.
4. Følg hver inngang bakover.
5. Erstatt mellomresultatene til hele uttrykket er skrevet.

Dette gjør det mulig å analysere en ukjent logisk krets.

## Kontroll

Lag sannhetstabellen både fra uttrykket og kretsen. Hvis de beskriver samme funksjon, skal resultatkolonnene være identiske.

Neste: [Halvaddereren](17-halvadder.md).
