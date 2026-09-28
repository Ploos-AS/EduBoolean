# M3 – Oppgaver: kombinatoriske kretser

1. Hvor mange porter trengs i en direkte implementasjon av `(A OR B) AND (NOT C)`?
2. Hvilke to porter danner en halvadder?
3. Hvorfor trenger en fulladder Cin?
4. Hva er SUM når A=1, B=1, Cin=1?
5. Hva er Cout i samme tilfelle?
6. Hva gjør en 2-til-1 multiplexer?
7. Hvor mange utganger har en 3-til-8-dekoder?
8. Hvilken port tester likhet mellom to enkeltbits på en naturlig måte?
9. Beskriv hvordan fire fulladdere kan brukes til å addere to 4-bits tall.
10. Hvorfor kan ripple-carry bli tregere når antall bits øker?

## Fasit

1. Tre: OR, NOT og AND.
2. XOR for SUM og AND for CARRY.
3. Fordi alle bitposisjoner unntatt den minst signifikante kan motta carry fra forrige posisjon.
4. 1.
5. 1.
6. Den velger én av to datainnganger ut fra et valgsignal.
7. Åtte.
8. XNOR.
9. Cout fra hver lavere bit kobles til Cin på neste høyere bit.
10. Carry-signalet må forplante seg gjennom flere trinn; fysiske porter har endelig propagasjonsforsinkelse.
