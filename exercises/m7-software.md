# M7 – Oppgaver: boolsk logikk i programvare

1. Hva produserer uttrykket `temperature > 30`?
2. Skriv `A AND NOT B` i Python.
3. Skriv det samme med logiske operatorer i C.
4. Hva er forskjellen på C-operatorene `&&` og `&`?
5. Hvorfor kan short-circuit gjøre `x != NULL && x->ready` nyttig i C?
6. Hva blir `1010 & 1100`?
7. Hvordan tester du masken `00000100` mot en flags-verdi?
8. Hvordan setter du bits i en maske uten å fjerne de eksisterende?
9. Oversett `is_admin or (is_owner and can_edit)` til boolsk notasjon.
10. Hvor mange kombinasjoner må testes uttømmende for fire boolske innganger?

## Fasit

1. En boolsk/sannhetsverdi.
2. `a and not b`.
3. `a && !b`.
4. `&&` er logisk AND med short-circuit; `&` er bitvis AND på heltallsbits (og har ikke samme short-circuit-semantikk).
5. Hvis `x == NULL`, evalueres ikke høyre operand, slik at medlemstilgangen unngås.
6. `1000`.
7. Test om `(flags & mask) != 0`.
8. `flags | mask`.
9. `A OR (O AND E)`.
10. `2^4 = 16`.
