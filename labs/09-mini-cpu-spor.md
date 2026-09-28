# Lab 9 – Spor en minimal CPU-operasjon

Vi bruker en konseptuell CPU med:

- register A
- register B
- ALU
- flagg
- PC
- instruksjonsregister
- kontrolltilstand FETCH/EXECUTE

Start:

```text
A  = 0011
B  = 0101
PC = 0000
state = FETCH
```

Minnet på adresse 0000 inneholder en instruksjon som betyr:

```text
ADD A,B
```

## Spor

Beskriv hva som skjer når systemet går gjennom:

```text
FETCH → EXECUTE → FETCH
```

For den pedagogiske modellen kan du anta:

1. FETCH laster instruksjonen og øker PC.
2. EXECUTE leser A og B.
3. ALU velges til ADD.
4. Resultatet `1000` produseres.
5. Resultat og flagg oppdateres etter modellens kontrollsignaler.
6. kontrolltilstanden går tilbake til FETCH.

## Refleksjon

Marker hvilke deler som er:

- kombinatoriske
- sekvensielle
- datapath
- control

Målet er ikke å simulere en bestemt kommersiell CPU, men å gjenkjenne kurskonseptene i ett samlet system.
