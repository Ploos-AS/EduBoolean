# 25 – Gray-kode og naboskap

For større K-map er rekkefølgen **ikke** vanlig binær telling.

To bits ordnes:

```text
00, 01, 11, 10
```

Ikke:

```text
00, 01, 10, 11
```

Hvorfor? Hvert nabopar skal skille seg i nøyaktig én bit.

Dette kalles Gray-kode-rekkefølge.

## Kantene er også naboer

Et K-map «vikler seg rundt». Første og siste kolonne er naboer, og første og siste rad er naboer.

Det betyr at grupper kan gå over kanten av kartet.

## Hvorfor virker dette?

Når to celler skiller seg i bare én variabel, kan den varierende variabelen elimineres algebraisk.

K-map gjør slike muligheter synlige.

Neste: [3-variabel K-map](26-kmap-3.md).
