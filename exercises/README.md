# EduBoolean Exercises

Oppgavene skal kunne løses uten fysisk maskinvare. De første oppgavene bruker vanlig språk før symbolsk notasjon.

## M0 – Startoppgaver

### Oppgave 1 – To tilstander

Finn fem ting fra hverdagen som kan beskrives med to tilstander.

Eksempel:

```text
lys: av / på
```

### Oppgave 2 – Lag boolske variabler

Gi hver av disse et variabelnavn og bestem hva `0` og `1` betyr:

- en dør
- en lampe
- en knapp
- en alarm

### Oppgave 3 – Sant eller usant?

Anta:

```text
D = 1   døren er åpen
L = 0   lampen er av
```

Svar:

1. Er "døren er åpen" sant eller usant?
2. Er "lampen er på" sant eller usant?

### Oppgave 4 – Fra setning til logikk

Beskriv hvilke boolske variabler du ville brukt for regelen:

> Lampen skal slå seg på når det er mørkt og bryteren er aktivert.

Du trenger ikke skrive et formelt uttrykk ennå.

### Oppgave 5 – Finn logikken i programvare

Se på denne koden:

```python
if door_open and alarm_enabled:
    print("Alarm!")
```

Forklar med egne ord hva som må være sant før teksten `Alarm!` skrives ut.

## Fasit til startoppgavene

### Oppgave 1

Mange svar er mulige, for eksempel åpen/lukket, inne/ute, tilkoblet/frakoblet og trykket/ikke trykket.

### Oppgave 2

Ett mulig svar:

```text
D: 0 = lukket, 1 = åpen
L: 0 = av,     1 = på
K: 0 = fri,    1 = trykket
A: 0 = av,     1 = aktiv
```

Andre tydelig definerte navn er like riktige.

### Oppgave 3

1. Sant.
2. Usant.

### Oppgave 4

For eksempel:

```text
M = det er mørkt
B = bryteren er aktivert
L = lampen skal være på
```

Senere lærer vi å uttrykke regelen som `L = M AND B`.

### Oppgave 5

Både `door_open` og `alarm_enabled` må være sanne.

## Prinsipp for videre oppgaver

Hver modul skal ha en blanding av:

- kontrollspørsmål
- oversetting fra hverdagsspråk til logikk
- sannhetstabeller
- uttrykksforenkling
- kretslesing
- kretsdesign
- praktiske utfordringer

Fasit skal forklare *hvorfor*, ikke bare oppgi riktig svar.
