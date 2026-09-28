# M5 – Oppgaver: sekvensiell logikk

1. Hva mangler en kombinatorisk krets for å kunne huske fortiden?
2. Hva betyr «behold tidligere Q»?
3. Hva er hovedforskjellen mellom en D-latch og en edge-triggered D-flip-flop?
4. Hvor mange bits lagrer åtte én-bits flip-flopper?
5. Hva skjer med en positiv-flanke-triggeret D-flip-flop ved stigende klokke?
6. Hva gjør et shift-register?
7. Skriv de fire tilstandene i en 2-bits binærteller.
8. Hva betyr `current_state`?
9. Hvorfor trenger en teller både kombinatorisk logikk og lagring?
10. Nevn to reelle timingbegreper som idealisert boolsk algebra ikke beskriver.

## Fasit

1. En lagret tilstand/minne.
2. At utgangen avhenger av en tidligere lagret verdi og ikke bare av inngangene akkurat nå.
3. Latchen er nivåfølsom mens den er enabled; den edge-triggerede flip-floppen sampler på en bestemt flanke.
4. Åtte bits.
5. D samples/lagres i Q, forutsatt at timingkravene er oppfylt.
6. Det lagrer bits og flytter dem mellom posisjoner ved kontrollerte hendelser.
7. 00, 01, 10, 11.
8. Systemets lagrede tilstand akkurat nå.
9. Logikken beregner neste verdi; lagringen beholder nåværende verdi mellom oppdateringer.
10. For eksempel propagasjonsforsinkelse, setup-tid, hold-tid eller clock skew.
