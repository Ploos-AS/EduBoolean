# Leksjon 0 – Hva er boolsk algebra?

## Før vi begynner

Du trenger ikke kunne algebra fra før.

Ordet *algebra* kan høres matematisk og vanskelig ut, men ideen vi skal starte med er svært enkel: noen spørsmål har bare to mulige svar.

Eksempler:

- Er lyset på?
- Er døren åpen?
- Er knappen trykket inn?
- Er alarmen aktiv?

Vi kan svare **ja** eller **nei**.

I boolsk algebra bruker vi ofte ordene:

- **sant**
- **usant**

Og i digitale systemer representerer vi dem ofte med:

- `1` = sant
- `0` = usant

Det betyr ikke at tallet 1 alltid "er" sant i vanlig matematikk. Her bruker vi bare 1 og 0 som praktiske symboler for to mulige tilstander.

## En boolsk variabel

En variabel er et navn på noe som kan ha en verdi.

La oss kalle tilstanden til en lampe for `L`.

Da kan vi skrive:

```text
L = 0   lampen er av
L = 1   lampen er på
```

`L` er nå en **boolsk variabel**, fordi den bare kan ha to sannhetsverdier.

Et annet eksempel:

```text
D = 0   døren er lukket
D = 1   døren er åpen
```

## Hvorfor trenger vi dette?

Digitale datamaskiner arbeider med enorme mengder tilstander som kan beskrives med bits.

En bit kan ha verdien:

```text
0 eller 1
```

Boolsk algebra gir oss et språk og et sett med regler for å beskrive hvordan slike verdier skal behandles.

Det lar oss svare på spørsmål som:

- Skal denne lampen være på?
- Skal alarmen utløses?
- Skal CPU-en addere eller sammenligne?
- Skal programmet gå inn i denne `if`-blokken?

## Et første logisk uttrykk

Tenk deg en enkel sikkerhetsregel:

> Alarmen skal gå når døren er åpen og alarmen er aktivert.

Vi kan gi navn til de to betingelsene:

```text
D = døren er åpen
A = alarmen er aktivert
```

Alarmen skal bare gå når **begge** er sanne.

Dette kalles **AND**.

Vi kommer tilbake til AND i detalj senere. Foreløpig er poenget bare å se at en setning fra virkeligheten kan gjøres om til logikk.

## Fra virkelighet til datamaskin

Vi kan tenke oss denne kjeden:

```text
virkelig situasjon
      ↓
ja/nei-spørsmål
      ↓
sant/usant
      ↓
0/1
      ↓
boolsk uttrykk
      ↓
logiske porter eller programkode
```

Dette er en av de viktigste ideene i hele kurset.

## Boolsk algebra er ikke bare elektronikk

De samme ideene dukker opp i programmering.

Eksempel i Python:

```python
door_open = True
alarm_enabled = True

if door_open and alarm_enabled:
    print("Alarm!")
```

Ordet `and` her uttrykker den samme logiske ideen som en fysisk AND-port i digital elektronikk.

Implementasjonen er forskjellig, men logikken er den samme.

## Hva skal du lære videre?

I de neste leksjonene lærer du først de tre viktigste logiske operasjonene:

1. **NOT** – snu sannhetsverdien
2. **AND** – begge må være sanne
3. **OR** – minst én må være sann

Deretter bygger vi videre med sannhetstabeller, flere operatorer og ekte digitale kretser.

## Kontrollspørsmål

Prøv å svare uten å se tilbake.

1. Hvilke to verdier kan en boolsk variabel ha?
2. Hvilket siffer bruker vi vanligvis for sant?
3. Hvilket siffer bruker vi vanligvis for usant?
4. Er `L = 1` nok til å vite hva `L` betyr uten at vi først har definert variabelen?
5. Nevn ett eksempel fra hverdagen som kan beskrives som sant/usant.

## Viktig å huske

> Boolsk algebra handler om verdier med to mulige sannhetstilstander og reglene for å kombinere dem.

Når du forstår dette, har du allerede tatt det første steget fra vanlig språk mot hvordan digitale datamaskiner beskriver beslutninger.

## Neste

Neste leksjon: **Sant, usant, 0 og 1**.
