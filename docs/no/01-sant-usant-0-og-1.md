# 1 – Sant, usant, 0 og 1

## Mål

Etter denne leksjonen skal du kunne forklare hva en boolsk verdi er, hvorfor vi bruker to verdier, og hvordan `sant/usant` kan representeres som `1/0`.

## To muligheter

Mange spørsmål kan besvares med ja eller nei:

- Er bryteren på?
- Er døren åpen?
- Har brukeren skrevet riktig passord?
- Er tallet større enn 10?

I boolsk algebra representerer vi slike svar med to sannhetsverdier:

| Logisk verdi | Vanlig digital representasjon |
|---|---:|
| usant (false) | 0 |
| sant (true) | 1 |

Dette betyr **ikke** at tallet 1 alltid betyr sant i all matematikk. Her bruker vi 0 og 1 som symboler for to logiske tilstander.

## Boolsk variabel

En variabel som bare kan ha én av to sannhetsverdier kalles en boolsk variabel.

Eksempel:

```text
door_open = 1
```

betyr at påstanden «døren er åpen» er sann.

```text
door_open = 0
```

betyr at den er usann.

## Fra virkelighet til modell

En fysisk knapp kan være trykket eller ikke trykket. En digital inngang kan derfor representere dette som 1 eller 0. Det er modellen som gir biten mening.

## Viktig skille

En bit er en fysisk eller lagret binær verdi. En boolsk verdi beskriver logisk sannhet. Begge kan representeres med 0 og 1, men begrepene betyr ikke helt det samme.

## Sjekk deg selv

1. Hvilke to verdier kan en boolsk variabel ha?
2. Hva betyr `alarm = 0` hvis variabelen beskriver «alarmen er aktiv»?
3. Finn tre spørsmål fra hverdagen som kan modelleres med sant/usant.

Neste: [NOT – det motsatte](02-not.md).
