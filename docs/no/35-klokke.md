# 35 – Klokke og tid

Mange digitale systemer organiserer tilstandsendringer rundt et periodisk signal: **klokken**.

```text
0 → 1 → 0 → 1 → 0 ...
```

En overgang fra 0 til 1 kalles stigende flanke. Fra 1 til 0 kalles fallende flanke.

Klokken gir systemet avtalte tidspunkter for når tilstand kan oppdateres.

## Hvorfor er dette nyttig?

Tenk deg mange registre og logiske blokker. Hvis alle lagrede verdier oppdateres etter samme klokkeprinsipp, blir det enklere å organisere dataflyten.

## Men klokken er ikke magi

Virkelig maskinvare har blant annet:

- propagasjonsforsinkelse
- setup-tid
- hold-tid
- clock skew

Vi introduserer begrepene her, men detaljert timinganalyse ligger utenfor grunnkurset.

Neste: [D-flip-flop](36-d-flip-flop.md).
