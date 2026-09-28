# Lab 11 – Bitmasker i praksis

Definer fire rettigheter:

```text
READ    = 0001
WRITE   = 0010
EXECUTE = 0100
ADMIN   = 1000
```

Start med:

```text
permissions = 0000
```

## Oppgaver

1. Sett READ.
2. Sett WRITE uten å fjerne READ.
3. Test om EXECUTE er satt.
4. Sett EXECUTE.
5. Fjern WRITE.
6. Kontroller sluttverdien bit for bit.

Bruk operasjonene:

```text
set:    value OR mask
test:   value AND mask
clear:  value AND (NOT mask)
```

Implementer først på papir, deretter i Python eller C.

## Koblingen tilbake til maskinvare

Bitvis AND, OR og NOT utfører samme sannhetstabell per bitposisjon som portene tidligere i kurset. Programvaren bruker CPU-instruksjoner som til slutt implementeres av digital logikk.
