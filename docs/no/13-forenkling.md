# 13 – Systematisk forenkling

Nå bruker vi lovene som verktøy.

## Eksempel 1

```text
(A AND B) OR (A AND NOT B)
```

Faktoriser A:

```text
A AND (B OR NOT B)
```

Komplementloven gir:

```text
A AND 1
```

Identitetsloven gir:

```text
A
```

## Eksempel 2

```text
A OR (A AND B)
```

Absorpsjon:

```text
A
```

## Arbeidsmetode

1. Se etter komplementer: `A` og `NOT A`.
2. Se etter identitet eller dominans med 0 og 1.
3. Se etter gjentakelser.
4. Se etter felles faktorer.
5. Se etter absorpsjon.
6. Bruk De Morgan når en hel parentes er invertert.
7. Kontroller resultatet med sannhetstabell hvis du er usikker.

Målet er ikke å gjøre uttrykket «pent», men å finne et enklere ekvivalent uttrykk.

Neste: [Bevis med sannhetstabeller](14-ekvivalensbevis.md).
