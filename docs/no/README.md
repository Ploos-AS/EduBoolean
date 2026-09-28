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


## M4 – Karnaugh-kart

23. [Hvorfor Karnaugh-kart?](23-karnaugh-intro.md)
24. [2-variabel K-map](24-kmap-2.md)
25. [Gray-kode og naboskap](25-gray-naboskap.md)
26. [3-variabel K-map](26-kmap-3.md)
27. [4-variabel K-map](27-kmap-4.md)
28. [Fra gruppe til uttrykk](28-gruppe-til-uttrykk.md)
29. [Wrap-around og overlapp](29-wrap-overlap.md)
30. [Don't-care-betingelser](30-dont-care.md)
31. [K-map kontra algebra](31-kmap-vs-algebra.md)

Praksis: [M4-oppgaver](../../exercises/m4-karnaugh.md) og [K-map-optimaliseringslab](../../labs/06-kmap-optimalisering.md).


## M5 – Sekvensiell logikk

32. [Fra logikk til minne](32-fra-logikk-til-minne.md)
33. [SR-latch](33-sr-latch.md)
34. [D-latch](34-d-latch.md)
35. [Klokke og tid](35-klokke.md)
36. [D-flip-flop](36-d-flip-flop.md)
37. [Register](37-register.md)
38. [Shift-register](38-shift-register.md)
39. [Tellere](39-tellere.md)
40. [Tilstand og FSM-broen](40-state.md)
41. [Sett sammen et sekvensielt system](41-sequential-system.md)

Praksis: [M5-oppgaver](../../exercises/m5-sequential.md) og [2-bits synkron teller](../../labs/07-2bit-teller.md).


## M6 – Fra logikk til CPU

42. [Fra byggeklosser til CPU](42-fra-byggeklosser-til-cpu.md)
43. [ALU](43-alu.md)
44. [CPU-flagg](44-flagg.md)
45. [Registre og registervalg](45-registerfil.md)
46. [Opcode-dekoding](46-opcode.md)
47. [Kontrollsignaler](47-kontrollsignaler.md)
48. [Program counter](48-program-counter.md)
49. [Fetch og execute](49-fetch-execute.md)
50. [Minimal pedagogisk datapath](50-minimal-datapath.md)
51. [Broen til EduCPU](51-broen-til-educpu.md)

Praksis: [M6-oppgaver](../../exercises/m6-cpu.md), [mini-ALU](../../labs/08-mini-alu.md) og [minimal CPU-sporing](../../labs/09-mini-cpu-spor.md).


## M7 – Boolsk logikk i programvare

52. [Bool i programmering](52-bool-i-programmering.md)
53. [Sammenligninger](53-sammenligninger.md)
54. [AND, OR og NOT i kode](54-logiske-operatorer.md)
55. [if og kontrollflyt](55-if.md)
56. [Short-circuit evaluation](56-short-circuit.md)
57. [Logiske kontra bitvise operatorer](57-logisk-vs-bitvis.md)
58. [Bitmasker](58-bitmasker.md)
59. [Flagg, features og permissions](59-flagg-permissions.md)
60. [De Morgan i kode](60-de-morgan-kode.md)
61. [Fra kode tilbake til logikk](61-kode-til-logikk.md)

Praksis: [M7-oppgaver](../../exercises/m7-software.md), [tilgangspolicy og uttømmende testing](../../labs/10-policy-test.md) og [bitmasker](../../labs/11-bitmasker.md).
