# 30 – Don't-care-betingelser

Noen inngangskombinasjoner forekommer aldri, eller resultatet deres spiller ingen rolle.

Disse kan markeres som **don't-care**, ofte med:

```text
X
```

En X kan behandles som 0 eller 1, avhengig av hva som gir enklest uttrykk.

## Viktig

Du **må ikke** inkludere en don't-care i en gruppe.

Du **kan** bruke den hvis den lar deg lage en større og bedre gruppe.

## Eksempel

Hvis en gruppe med to ettall kan utvides til fire celler ved å inkludere to X-er, kan det eliminere en ekstra variabel.

Don't-care betyr altså ikke «ukjent». Det betyr at funksjonens spesifikasjon ikke krever en bestemt verdi for denne inngangskombinasjonen.

Neste: [K-map kontra algebra](31-kmap-vs-algebra.md).
