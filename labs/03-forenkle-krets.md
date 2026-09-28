# Lab 3 – Samme funksjon, færre porter

Vi starter med funksjonen:

```text
F = (A AND B) OR (A AND NOT B)
```

## Del 1 – Original krets

Tegn eller bygg kretsen med:

- én NOT-port
- to AND-porter
- én OR-port

Lag sannhetstabellen.

## Del 2 – Forenkle

Bruk boolsk algebra:

```text
(A AND B) OR (A AND NOT B)
= A AND (B OR NOT B)
= A AND 1
= A
```

## Del 3 – Ny krets

Den forenklede «kretsen» trenger ingen logisk port: utgangen F følger A direkte.

Kontroller at begge variantene har samme sannhetstabell.

## Hva lærte vi?

Boolsk algebra er ikke bare symbolmanipulasjon. Den kan vise at en hel gruppe porter er overflødig. Dette er den direkte broen fra algebra til kretsoptimalisering.
