# 59 – Flagg, features og permissions

Bitmasker brukes ofte når flere uavhengige ja/nei-egenskaper skal pakkes i én verdi.

Eksempel:

```text
READ    = 0001
WRITE   = 0010
EXECUTE = 0100
ADMIN   = 1000
```

En verdi:

```text
0111
```

kan da representere READ + WRITE + EXECUTE.

## Feature flags

På et høyere programvarenivå kan boolske variabler brukes direkte:

```python
dark_mode_enabled = True
new_parser_enabled = False
```

## Viktig sikkerhetspoeng

En boolsk tilgangstest er bare korrekt hvis hele policyen er korrekt modellert.

For eksempel:

```text
is_admin OR (is_owner AND can_edit)
```

betyr noe annet enn:

```text
(is_admin OR is_owner) AND can_edit
```

Parenteser og presis logikk kan derfor være sikkerhetskritisk.

Neste: [De Morgan i kode](60-de-morgan-kode.md).
