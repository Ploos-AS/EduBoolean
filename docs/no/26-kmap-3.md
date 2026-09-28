# 26 – K-map med tre variabler

Med A, B og C finnes åtte kombinasjoner.

Vi kan bruke A som rad og BC som kolonner:

| A \ BC | 00 | 01 | 11 | 10 |
|---|---:|---:|---:|---:|
| 0 |  |  |  |  |
| 1 |  |  |  |  |

Kolonnene står i Gray-rekkefølge.

## Grupper

Gyldige gruppestørrelser er potenser av to:

```text
1, 2, 4, 8, ...
```

Vi ønsker vanligvis størst mulige grupper.

En gruppe på fire celler i et trevariabelkart kan eliminere to variabler og etterlate bare én.

## Overlapp er lov

En celle med 1 kan brukes i mer enn én gruppe hvis det gir en enklere total løsning.

Målet er å dekke alle nødvendige ettall, ikke å dele kartet i separate territorier.

Neste: [4-variabel K-map](27-kmap-4.md).
