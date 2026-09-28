# EduBoolean

**Boolsk algebra fra null til digitale datamaskiner.**

EduBoolean er et nybegynnervennlig kurs i boolsk algebra og praktisk digital logikk. Kurset forutsetter ingen tidligere kunnskap om elektronikk, programmering eller diskret matematikk.

Målet er å bygge en sammenhengende forståelse fra `sant/usant` og `0/1`, via sannhetstabeller og logiske porter, til kombinatoriske kretser, addere, ALU-er, kontrollogikk og hvordan boolske uttrykk brukes i programmering og datamaskiner.

> Norsk er hovedspråk. Engelsk skal tilbys som sidestilt kursversjon.

## Ploos project contract

EduBoolean is the reference implementation of **PLOOS-PROJECT-1**.

Declared capabilities: `docs`, `i18n`, `software`, `simulator`, `hdl`, `publishing`, `website`.

Project-local sources and tests remain in this repository. Reusable HDL qualification is consumed from `Ploos-AS/hardware-ci@v1`; reusable publication policy and production conventions come from `Ploos-AS/publishing`.

## Målgruppe

- komplette nybegynnere
- elever og studenter som vil forstå digital logikk fra grunnen av
- hobbyelektronikere og makers
- programmerere som vil forstå hva som skjer under programvaren
- deltakere i EduCPU, EduK8 og andre Ploos-utdanningsprosjekter

## Læringsmål

Etter fullført kurs skal studenten kunne:

1. forklare binære sannhetsverdier og boolske variabler
2. bruke NOT, AND, OR, XOR, NAND, NOR og XNOR
3. lage og lese sannhetstabeller
4. oversette mellom tekst, sannhetstabell, boolsk uttrykk og logisk krets
5. bruke grunnleggende lover i boolsk algebra
6. forenkle boolske uttrykk algebraisk
7. bruke Karnaugh-kart på enkle funksjoner
8. bygge kombinatoriske kretser som multipleksere, dekodere og addere
9. forstå grunnideen bak sekvensiell logikk, latch, flip-flop, register og teller
10. forklare hvordan boolsk logikk inngår i ALU, CPU og kontrollsignaler
11. gjenkjenne boolsk logikk i C, Python og andre programmeringsspråk
12. bygge og teste logiske kretser i simulator og senere på fysisk maskinvare

## Kursløp

| Del | Tema |
|---|---|
| 0 | Hva er boolsk algebra? |
| 1 | Sant, usant, 0 og 1 |
| 2 | NOT, AND og OR |
| 3 | XOR, NAND, NOR og XNOR |
| 4 | Sannhetstabeller |
| 5 | Fra uttrykk til logiske porter |
| 6 | Lover og regler i boolsk algebra |
| 7 | Forenkling av uttrykk |
| 8 | Karnaugh-kart |
| 9 | Kombinatoriske kretser |
| 10 | Addere og binær aritmetikk |
| 11 | Multipleksere, dekodere og encodere |
| 12 | Introduksjon til sekvensiell logikk |
| 13 | Latcher, flip-flopper, registre og tellere |
| 14 | Fra logikk til ALU og CPU |
| 15 | Boolsk logikk i programmering |
| 16 | Praktiske sluttprosjekter |

## Formater

EduBoolean skal bygges fra felles kurskilder og publiseres som:

- nettside
- EPUB
- Kindle-vennlig e-bok
- PDF

Interaktive øvelser og en egen EduLogic-simulator er planlagt som en del av prosjektet.

## Repository layout

```text
EduBoolean/
├── docs/
│   ├── no/
│   └── en/
├── exercises/
├── labs/
├── examples/
├── simulator/
├── ebook/
├── images/
├── ROADMAP.md
├── CONTRIBUTING.md
├── LICENSES.md
└── README.md
```

## Pedagogiske prinsipper

- Ingen skjulte forkunnskaper.
- Intuisjon før symbolbruk.
- Ett nytt begrep om gangen.
- Mange konkrete eksempler.
- Tekst → sannhetstabell → uttrykk → krets → anvendelse.
- Oppgaver med umiddelbar, forklarende fasit.
- Repetisjon med gradvis økende vanskelighetsgrad.
- Knytt hvert abstrakt tema til hvordan ekte datamaskiner bruker det.

## Relaterte Ploos-prosjekter

EduBoolean er ment som et fundament for blant annet:

- **EduNumbers** – tallsystemer og representasjon
- **EduCPU** – pedagogisk CPU, ISA og maskinarkitektur
- **EduK8** – komplett 8-bit læringsplattform
- **K16** – demo-orientert 8/16-bit maskin
- FPGA- og digital-elektronikkprosjekter

## Status

**M8 – EduLogic: qualified; M9 publishing integration next.**

Se [ROADMAP.md](ROADMAP.md) for milepæler.

## Lisensiering

Prosjektet bruker delt lisensiering etter innholdstype. Se [LICENSES.md](LICENSES.md).

Copyright © Ploos AS and contributors.
