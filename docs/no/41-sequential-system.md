# 41 – Sett sammen et sekvensielt system

Et typisk synkront digitalt system kan deles i to:

```text
             +----------------------+
current ---->| kombinatorisk logikk |----> next
inputs  ---->|                      |
             +----------------------+
                         |
                         v
                    +---------+
clock ------------->| register |
                    +---------+
                         |
                         +----> current
```

Registeret lagrer tilstanden. Kombinatorisk logikk beregner neste tilstand.

Dette mønsteret dukker opp igjen i:

- tellere
- kontrollenheter
- protokollmaskiner
- CPU-er
- FSM-er

## M5-sjekk

Du skal nå kunne forklare forskjellen mellom:

- kombinatorisk og sekvensiell logikk
- latch og flip-flop
- nivå og flanke
- én bit og et register
- register og shift-register
- nåværende og neste tilstand

Og viktigst: du skal kunne forklare hvorfor **hukommelse** endrer hva en logisk krets er i stand til å gjøre.
