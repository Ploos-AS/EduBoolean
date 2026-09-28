# 61 – Fra kode tilbake til boolsk logikk

Når en betingelse blir komplisert, kan vi analysere den som boolsk algebra.

Eksempel:

```python
if (is_admin or is_owner) and not suspended:
    allow()
```

Definer:

```text
A = is_admin
O = is_owner
S = suspended
```

Da blir betingelsen:

```text
(A OR O) AND (NOT S)
```

Nå kan vi:

- lage sannhetstabell
- kontrollere edge cases
- sammenligne med en policy
- bruke boolske lover
- lage tester fra kombinasjonene

## Boolsk algebra som testverktøy

Tre boolske innganger gir bare åtte kombinasjoner. For kritisk logikk kan det være realistisk å teste alle.

Dette er samme uttømmende idé som sannhetstabellen.

## M7-sjekk

Du skal nå kunne:

- bruke boolske verdier i Python og C
- forstå sammenligninger
- bruke logisk AND/OR/NOT
- forklare short-circuit
- skille logiske og bitvise operatorer
- bruke enkle bitmasker
- analysere permissions og feature flags
- oversette programbetingelser til boolske uttrykk
- bruke sannhetstabeller til å designe tester
