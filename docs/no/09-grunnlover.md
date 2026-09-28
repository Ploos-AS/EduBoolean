# 9 – Grunnlovene i boolsk algebra

Vi lærer lovene som mønstre, ikke som en liste som må pugges.

## Identitet

```text
A OR 0  = A
A AND 1 = A
```

Å OR-e med usant eller AND-e med sant endrer ingenting.

## Dominasjon

```text
A OR 1  = 1
A AND 0 = 0
```

## Idempotens

```text
A OR A  = A
A AND A = A
```

Å kombinere en påstand med seg selv gir ingen ny informasjon.

## Komplement

```text
A OR NOT A  = 1
A AND NOT A = 0
```

Enten er A sann eller så er A ikke sann. Begge kan ikke være sanne samtidig.

## Dobbel negasjon

```text
NOT (NOT A) = A
```

To inverteringer bringer oss tilbake til utgangspunktet.

Prøv å verifisere hver regel med en sannhetstabell.

Neste: [Rekkefølge og gruppering](10-kommutativ-assosiativ-distributiv.md).
