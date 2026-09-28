# 49 – Fetch og execute

En enkel CPU må gjenta en sekvens av handlinger.

En pedagogisk modell kan ha tilstandene:

```text
FETCH
EXECUTE
```

## FETCH

Konseptuelt:

```text
instruction ← memory[PC]
PC ← PC + 1
```

## EXECUTE

Opcode og operandfelt tolkes. Datapath og ALU aktiveres etter instruksjonen.

Deretter går kontrollen tilbake til FETCH.

Dette er en liten state machine:

```text
FETCH → EXECUTE → FETCH → EXECUTE ...
```

En ekte CPU kan ha langt flere faser, pipeline, cache og andre mekanismer. Men grunnideen viser hvordan register, kombinatorisk logikk og kontrolltilstand samarbeider.

Neste: [Minimal datapath](50-minimal-datapath.md).
