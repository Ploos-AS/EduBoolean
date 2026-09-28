# 44 – Flagg: informasjon om resultatet

En CPU trenger ofte mer informasjon enn selve resultatbitenes verdi.

Vanlige flagg inkluderer:

- Z – Zero
- C – Carry
- N – Negative
- V – signed Overflow

## Zero

Zero er 1 når alle resultatbitene er 0.

For et 4-bits resultat R:

```text
Z = NOT (R3 OR R2 OR R1 OR R0)
```

## Carry

Carry kan komme fra carry-out på den mest signifikante biten i en usignert adder.

## Negative

I to-komplement-representasjon brukes normalt mest signifikante bit som fortegnsbit:

```text
N = R3
```

for et 4-bits resultat.

## Overflow

Signed overflow er **ikke det samme som carry**.

Ved addisjon kan signed overflow oppstå når to operander med samme fortegn gir et resultat med motsatt fortegn.

For en n-bits adder kan overflow også uttrykkes via carry inn og ut av fortegnsbiten.

Flagg er boolske signaler. Senere instruksjoner kan bruke dem til å ta beslutninger.

Neste: [Registerfil](45-registerfil.md).
