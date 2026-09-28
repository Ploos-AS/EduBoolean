# 11 – Absorpsjon

To svært nyttige regler er:

```text
A OR (A AND B) = A
A AND (A OR B) = A
```

## Hvorfor?

Se på den første:

Hvis A er 1, er hele OR-uttrykket allerede 1. Hvis A er 0, blir `A AND B` også 0. B kan derfor aldri endre sluttresultatet.

Dermed kan:

```text
A OR (A AND B)
```

forenkles til bare:

```text
A
```

Dette kalles **absorpsjonsloven**.

I digitale kretser kan slik forenkling bety færre porter.

Neste: [De Morgans lover](12-de-morgan.md).
