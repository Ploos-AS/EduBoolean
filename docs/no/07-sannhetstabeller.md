# 7 – Sannhetstabeller

En sannhetstabell viser resultatet av en boolsk funksjon for alle mulige kombinasjoner av innganger.

Med én inngang finnes 2 kombinasjoner. Med to finnes 4. Med tre finnes 8. Generelt finnes:

```text
2^n
```

kombinasjoner for `n` boolske innganger.

## Eksempel: NOT A OR B

Vi beregner først NOT A og deretter OR:

| A | B | NOT A | (NOT A) OR B |
|---:|---:|---:|---:|
| 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 1 | 0 | 1 |

Mellomkolonnen gjør det lettere å se hvert steg.

## Arbeidsmetode

1. Finn antall inngangsvariabler.
2. Skriv alle inngangskombinasjonene.
3. Lag mellomkolonner for deluttrykk.
4. Beregn én operasjon om gangen.
5. Kontroller at alle kombinasjoner er med.

## Utfordring

Lag sannhetstabellen for:

```text
(A AND B) OR C
```

Med tre variabler skal tabellen ha åtte rader.

Neste steg i kurset er å bruke disse ferdighetene til å lese og bygge sammensatte uttrykk og logiske kretser.
