# 23 – Hvorfor Karnaugh-kart?

Vi kan allerede forenkle boolske uttrykk algebraisk. Et **Karnaugh-kart**, ofte kalt K-map, gir en visuell metode for små funksjoner.

Målet er det samme:

- færre ledd
- færre variabler i leddene
- ofte færre porter

Et K-map organiserer radene fra en sannhetstabell slik at logisk nærliggende kombinasjoner også ligger ved siden av hverandre.

## Hovedideen

Hvis to ledd bare skiller seg i én variabel:

```text
(A AND B) OR (A AND NOT B)
```

kan B elimineres:

```text
A
```

I et K-map vises dette som to naboceller som kan grupperes.

Neste: [2-variabel K-map](24-kmap-2.md).
