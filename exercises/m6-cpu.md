# M6 – Oppgaver: fra logikk til CPU

1. Hva gjør ALU-en?
2. Hvordan kan én ALU velge mellom ADD, AND, OR og XOR?
3. Skriv et boolsk uttrykk for Zero-flagget til et 4-bits resultat.
4. Er Carry og signed Overflow alltid det samme?
5. Hvor mange select-bits trengs for å velge ett av fire registre?
6. Hva kan en dekoder brukes til i en registerfil?
7. Hva er en opcode?
8. Hva gjør `REG_WRITE` konseptuelt?
9. Hva lagrer PC?
10. Skriv et uttrykk for «branch hvis Zero» med signalene BRANCH_IF_ZERO og Z.
11. Hvorfor trenger en FETCH/EXECUTE-modell sekvensiell logikk?
12. Forklar datapath kontra control med egne ord.

## Fasit

1. Den utfører aritmetiske og logiske operasjoner.
2. Beregn kandidatfunksjoner og velg resultat med MUX/kontrollogikk.
3. `NOT(R3 OR R2 OR R1 OR R0)`.
4. Nei.
5. To.
6. Å velge hvilket av fire registre som skal motta en skriveoperasjon.
7. Et binært felt som kontrollogikken tolker som en bestemt instruksjonsoperasjon.
8. Det tillater at valgt register lagrer write-data ved riktig hendelse.
9. Adressen til instruksjonen som skal hentes, etter den valgte CPU-modellen.
10. `BRANCH_IF_ZERO AND Z`.
11. CPU-en må huske hvilken kontrolltilstand den befinner seg i og lagrede arkitekturverdier.
12. Datapath flytter/bearbeider data; control genererer signalene som bestemmer hvilke operasjoner og dataflyter som aktiveres.
