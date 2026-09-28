# 39 – Tellere

En teller er sekvensiell logikk som går gjennom en bestemt serie tilstander.

En 2-bits binærteller kan gå:

```text
00
01
10
11
00
...
```

Hver klokkehendelse fører til neste tilstand.

## Hvorfor er dette annerledes enn en adder?

En kombinatorisk adder beregner et resultat fra inngangene. Telleren må i tillegg **huske nåværende verdi**, beregne neste verdi og lagre den.

Konseptuelt:

```text
next = current + 1
current ← next ved klokke
```

Tellere brukes til blant annet tidsmåling, adressering, frekvensdeling og sekvensering.

Neste: [Tilstand](40-state.md).
