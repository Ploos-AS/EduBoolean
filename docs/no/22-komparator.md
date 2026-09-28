# 22 – Komparatorer

En komparator sammenligner binære verdier.

For to én-bits innganger kan vi blant annet spørre:

```text
A = B?
A > B?
A < B?
```

Likhet kan uttrykkes med XNOR:

```text
EQ = A XNOR B
```

For flere bits må alle tilsvarende bitpar være like for at hele tallene skal være like.

En enkel to-bits likhetstest kan derfor bygges som:

```text
EQ = (A1 XNOR B1) AND (A0 XNOR B0)
```

Komparatorer brukes i CPU-er, kontrollogikk, tellere og mange andre digitale systemer.

## M3-sjekk

Du skal nå kunne forklare og analysere:

- logiske porter
- portnettverk
- halvadder
- fulladder
- ripple-carry-adder
- multiplexer
- dekoder og encoder
- enkel komparator

Vi har dermed gått fra boolske uttrykk til sentrale byggeblokker i en datamaskin.
