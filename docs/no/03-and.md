# 3 – AND: begge må være sanne

AND gir sant bare når **begge** inngangene er sanne.

| A | B | A AND B |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

## Eksempel

En maskin får bare starte når sikkerhetsdekselet er lukket **og** startknappen er trykket:

```text
start = cover_closed AND button_pressed
```

Hvis én av betingelsene er 0, blir `start` 0.

## Symboler

Du kan møte `A AND B`, `A ∧ B`, `A · B` eller ganske enkelt `AB`. Vi begynner med `AND` fordi betydningen er tydeligst.

## Programmering

I mange programmeringsspråk finnes samme idé. I C brukes for eksempel `&&` for logisk AND.

Neste: [OR](04-or.md).
