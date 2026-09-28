# 40 – Tilstand: kretsens hukommelse om fortiden

**State**, eller tilstand, er informasjon fra fortiden som fortsatt påvirker hva systemet gjør.

For en teller er nåværende tall tilstanden.

For en trafikklyskontroller kan tilstanden være:

```text
GRØNN
GUL
RØD
```

Innganger og nåværende tilstand bestemmer neste tilstand og eventuelle utganger.

En vanlig modell er:

```text
next_state = f(current_state, inputs)
outputs    = g(current_state, inputs)
```

eller i enkelte maskintyper avhenger utgangen bare av tilstanden.

## Broen til finite state machines

Når vi systematisk beskriver:

- mulige tilstander
- overganger
- hendelser/betingelser
- utganger

har vi beveget oss inn i **finite state machines (FSM)**.

EduBoolean gir grunnlaget. EduFSM kan gå mye dypere i selve modelleringen av state machines.

Neste: [Kombinatorisk + sekvensiell logikk](41-sequential-system.md).
