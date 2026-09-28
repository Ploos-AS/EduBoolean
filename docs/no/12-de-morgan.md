# 12 – De Morgans lover

De Morgans lover forteller hva som skjer når vi inverterer en hel AND- eller OR-operasjon.

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

## Huskeregel

Når NOT flyttes inn gjennom parentesen:

1. AND byttes til OR, eller OR byttes til AND.
2. Hver inngang inverteres.

## Eksempel

```text
NOT (door_open OR window_open)
```

betyr at verken døren eller vinduet er åpent:

```text
(NOT door_open) AND (NOT window_open)
```

## Verifiser den første loven

| A | B | NOT(A AND B) | (NOT A) OR (NOT B) |
|---:|---:|---:|---:|
| 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |

Kolonnene er identiske.

De Morgan er viktig både i kretsdesign og programmering.

Neste: [Systematisk forenkling](13-forenkling.md).
