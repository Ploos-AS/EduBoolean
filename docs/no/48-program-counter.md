# 48 – Program counter

Program counter, PC, holder adressen til instruksjonen CPU-en skal hente.

En enkel normal oppdatering kan være:

```text
next_PC = PC + 1
```

Dette krever:

- et register for PC
- en adder
- kontroll for når ny verdi skal lagres

## Branch

En branch kan velge en annen neste PC.

En MUX kan konseptuelt velge:

```text
normal_next = PC + 1
branch_next = target

next_PC = MUX(normal_next, branch_next, take_branch)
```

Og `take_branch` kan være et boolsk uttrykk basert på instruksjon og flagg.

Eksempel:

```text
take_branch = BRANCH_IF_ZERO AND Z
```

Her ser vi boolsk algebra styre programflyten direkte.

Neste: [Fetch og execute](49-fetch-execute.md).
