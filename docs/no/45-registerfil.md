# 45 – Registre og registervalg

En CPU har vanligvis flere registre.

Tenk deg fire registre:

```text
R0 R1 R2 R3
```

To bits er nok til å velge ett av fire registre:

| select | register |
|---|---|
| 00 | R0 |
| 01 | R1 |
| 10 | R2 |
| 11 | R3 |

En MUX kan velge hvilket register som skal leses.

En dekoder kan velge hvilket register som skal skrives.

## Lesing og skriving

Konseptuelt:

```text
read_data = selected register
```

Ved aktivt write-enable og klokkehendelse:

```text
selected register ← write_data
```

Her møtes kombinatorisk og sekvensiell logikk igjen.

Neste: [Opcode-dekoding](46-opcode.md).
