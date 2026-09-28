# 60 – De Morgan i kode

Lovene fra M2 dukker opp igjen:

```text
NOT (A AND B)
=
(NOT A) OR (NOT B)
```

og:

```text
NOT (A OR B)
=
(NOT A) AND (NOT B)
```

Python:

```python
not (a and b)
```

har samme sannhetstabell som:

```python
(not a) or (not b)
```

for boolske verdier.

## Lesbarhet

Algebraisk ekvivalens betyr ikke nødvendigvis at begge formene er like lette for mennesker å lese.

Velg gjerne formen som uttrykker intensjonen tydeligst.

Og husk short-circuit og sideeffekter: ren boolsk ekvivalens alene beskriver ikke nødvendigvis all observerbar programoppførsel når operandene gjør arbeid.

Neste: [Fra kode tilbake til logikk](61-kode-til-logikk.md).
