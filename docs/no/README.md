# EduBoolean – norsk kurs

Velkommen til EduBoolean.

Dette kurset er skrevet for deg som aldri har studert boolsk algebra, digital elektronikk eller datamaskinarkitektur før. Vi begynner med helt vanlige ideer som **ja/nei**, **på/av** og **sant/usant**. Derfra bygger vi steg for steg mot logiske porter, digitale kretser og til slutt hvordan en datamaskin bruker den samme logikken.

## Hvordan bruke kurset

Les leksjonene i rekkefølge. Hver leksjon skal inneholde:

1. en intuitiv forklaring
2. konkrete eksempler
3. symboler og formell notasjon først når ideen er forstått
4. kontrollspørsmål
5. øvelser
6. kobling til praktisk bruk

## Kurskart

### Del A – Første møte med logikk

- [Leksjon 0: Hva er boolsk algebra?](00-hva-er-boolsk-algebra.md)
- Sant, usant, 0 og 1
- Boolsk variabel
- NOT
- AND
- OR

### Del B – Flere operatorer og sannhetstabeller

- XOR
- NAND
- NOR
- XNOR
- sannhetstabeller
- uttrykk og operatorprioritet

### Del C – Boolsk algebra

- lover og identiteter
- De Morgans lover
- forenkling
- ekvivalente uttrykk

### Del D – Digital logikk

- logiske porter
- kombinatoriske kretser
- addere
- multipleksere
- dekodere

### Del E – Minne og tilstand

- hvorfor vi trenger tilstand
- latch og flip-flop
- register og teller
- overgang til finite state machines

### Del F – Datamaskinen

- ALU
- kontrollsignaler
- dekoding
- CPU
- sammenheng med EduCPU og EduK8

### Del G – Programvare

- boolske uttrykk i kode
- `if`
- logiske operatorer
- bitvise operatorer
- masker og flagg

## Første øvelser

Se [`exercises/README.md`](../../exercises/README.md).

## Første lab

Se [`labs/01-brytere-og-logikk.md`](../../labs/01-brytere-og-logikk.md).


## M1 – Boolean Fundamentals

1. [Sant, usant, 0 og 1](01-sant-usant-0-og-1.md)
2. [NOT](02-not.md)
3. [AND](03-and.md)
4. [OR](04-or.md)
5. [XOR](05-xor.md)
6. [NAND, NOR og XNOR](06-nand-nor-xnor.md)
7. [Sannhetstabeller](07-sannhetstabeller.md)

Til M1 hører også [oppgavesettet](../../exercises/m1-fundamentals.md) og [halvadder-labben](../../labs/02-halvadderer.md).


## M2 – Algebra og forenkling

8. [Boolsk ekvivalens](08-ekvivalens.md)
9. [Grunnlovene](09-grunnlover.md)
10. [Kommutative, assosiative og distributive lover](10-kommutativ-assosiativ-distributiv.md)
11. [Absorpsjon](11-absorpsjon.md)
12. [De Morgans lover](12-de-morgan.md)
13. [Systematisk forenkling](13-forenkling.md)
14. [Ekvivalensbevis med sannhetstabeller](14-ekvivalensbevis.md)

Til M2 hører [oppgavesettet](../../exercises/m2-algebra.md) og [kretsforenklings-labben](../../labs/03-forenkle-krets.md).


## M3 – Logiske porter og kombinatoriske kretser

15. [Logiske porter](15-logiske-porter.md)
16. [Fra uttrykk til krets](16-uttrykk-til-krets.md)
17. [Halvadder](17-halvadder.md)
18. [Fulladder](18-fulladder.md)
19. [Flerbits addisjon og ripple carry](19-ripple-carry.md)
20. [Multiplexer](20-multiplexer.md)
21. [Dekodere og encodere](21-dekoder-encoder.md)
22. [Komparatorer](22-komparator.md)

Praksis: [M3-oppgaver](../../exercises/m3-combinational.md), [4-bits adderer](../../labs/04-bygg-4bit-adder.md) og [2-til-1 MUX](../../labs/05-mux.md).
