# 52 – Boolsk logikk i programmering

Boolsk algebra finnes ikke bare i digitale porter. Programmer bruker de samme idéene for å ta beslutninger.

En boolsk verdi har to mulige sannhetsverdier:

```text
true
false
```

I Python:

```python
door_open = True
```

I C:

```c
#include <stdbool.h>
bool door_open = true;
```

## Samme idé, ny representasjon

I maskinvare snakket vi om signaler 0 og 1. I programmering arbeider vi ofte med navnene false og true.

Men ikke bland sammen:

- boolsk sannhetsverdi
- heltallet 0 eller 1
- et helt bitmønster

Språk har egne regler for konvertering mellom disse.

Neste: [Sammenligninger](53-sammenligninger.md).
