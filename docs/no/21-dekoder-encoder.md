# 21 – Dekodere og encodere

## Dekoder

En dekoder oversetter en binær kode til én av flere utganger.

En 2-til-4-dekoder har to innganger og fire utganger. For hver inngangskombinasjon aktiveres normalt én utgang.

| A | B | aktiv utgang |
|---:|---:|---|
| 0 | 0 | Y0 |
| 0 | 1 | Y1 |
| 1 | 0 | Y2 |
| 1 | 1 | Y3 |

Dette er nyttig for blant annet adressevalg og instruksjonsdekoding.

## Encoder

En encoder gjør i prinsippet motsatt: en aktiv inngang representeres som en binær kode.

Virkelige encodere trenger regler for hva som skjer hvis flere innganger er aktive samtidig. En **priority encoder** gir enkelte innganger prioritet.

Neste: [Komparatorer](22-komparator.md).
