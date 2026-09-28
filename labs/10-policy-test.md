# Lab 10 – Fra tilgangspolicy til uttømmende tester

Vi har policyen:

```text
Tilgang gis hvis brukeren er administrator,
ELLER hvis brukeren både er eier og ikke er suspendert.
```

Definer:

```text
A = is_admin
O = is_owner
S = suspended
```

Uttrykket blir:

```text
ALLOW = A OR (O AND NOT S)
```

## Del 1

Lag sannhetstabellen for alle åtte kombinasjoner.

## Del 2 – Python

Implementer:

```python
def allowed(is_admin, is_owner, suspended):
    return is_admin or (is_owner and not suspended)
```

Skriv en test som går gjennom alle åtte kombinasjonene og sammenligner funksjonen med forventet sannhetstabell.

## Del 3 – C

Implementer samme policy med `bool`, `||`, `&&` og `!`.

## Del 4 – Analyse

Sammenlign med:

```text
(A OR O) AND NOT S
```

Finn kombinasjonen(e) hvor de to policyene er forskjellige.

Dette demonstrerer hvorfor parentesplassering i tilgangskontroll ikke bare er stil.
