# 19 – Flerbits addisjon og ripple carry

For å legge sammen flerbits tall kobler vi flere fulladdere etter hverandre.

Carry-out fra én bitposisjon blir carry-in til den neste:

```text
bit 0 → carry → bit 1 → carry → bit 2 → carry → bit 3
```

For eksempel kan fire fulladdere danne en 4-bits adderer.

## Eksempel

```text
  0101   (5)
+ 0011   (3)
------
  1000   (8)
```

Hver bitposisjon gjør bare lokal én-bits addisjon, men carry-signalet binder dem sammen.

## Hvorfor «ripple»?

Carry må forplante seg gjennom kjeden. I virkelig maskinvare tar signalendringer litt tid. En lang carry-kjede kan derfor begrense hvor raskt en krets kan arbeide.

Her får vi vårt første møte med forskjellen mellom en logisk funksjon og dens fysiske timing.

Neste: [Multiplexeren](20-multiplexer.md).
