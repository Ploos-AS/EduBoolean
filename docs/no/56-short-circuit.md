# 56 – Short-circuit evaluation

Programmeringsspråk evaluerer ofte logisk AND og OR med **short-circuit**.

For:

```text
A AND B
```

trenger programmet ikke evaluere B hvis A allerede er false.

For:

```text
A OR B
```

trenger programmet ikke evaluere B hvis A allerede er true.

## Hvorfor betyr dette noe?

Tenk Python:

```python
if user is not None and user.is_admin:
    ...
```

Hvis `user is None`, blir høyre side ikke evaluert.

Dette er en viktig forskjell mellom et programmeringsuttrykk og en idealisert sannhetstabell: resultatlogikken kan være den samme, men **evalueringen kan ha rekkefølge og sideeffekter**.

Ikke bruk algebraiske omskrivninger blindt når uttrykk har funksjonskall eller sideeffekter.

Neste: [Logisk kontra bitvis](57-logisk-vs-bitvis.md).
