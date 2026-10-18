# Attribute axis ("what fact about the person") - draft v1

Replaces the earlier "Person" axis (minor, elderly, ...), whose values mostly belong inside these families. The attribute family says *what fact about whom*; the predicate axis says *what form the claim takes* (threshold, membership, ...).

| Family | Asserts | Examples |
|---|---|---|
| who_you_are | innate or ascribed trait | age, gender, birthplace, ethnicity |
| where_you_belong | membership, affiliation | employer, campus, residency, union, congregation, building |
| who_you_are_linked_to | relationship | guardian, spouse, dependent, owner, delegate |
| what_you_hold | possession or entitlement | ticket, licence, visa, balance, subsidy eligibility |
| what_youve_done | record or history | criminal or driving record, payments, vaccination, attendance |
| what_you_can_do | qualification | degree, professional licence, skill test |
| what_state_youre_in | current situation, vulnerability | disability, pregnancy, low income, victim status, illness, location |

Modifiers (not families): sensitivity (GDPR Art. 9/10, Taiwan PDPA Art. 6 special categories; PDPA list recalled from memory, verify), stability, attester.

## Test on the 96 pilot ideas (Sonnet and Haiku classified independently, blind to arm and cell)

- Family agreement 78/96; all 18 disagreements fall in three kinds of case: low-income subsidy rolls (hold vs state), one-per-person limits (who you are vs hold), one-vote-per-resident (who you are vs belong).
- Sensitivity agreement 93/96; attester 83/96; **stability only 48/96, so the stability labels are unusable as defined**.
- Distribution (Sonnet): what_youve_done 32, where_you_belong 25, what_state_youre_in 14, what_you_hold 12, who_you_are 12, what_you_can_do 1, who_you_are_linked_to 0.
- Family is almost fully determined by the cell: employer-fresh and univ-crossmatch are 12/12 where_you_belong, telco-unique 12/12 who_you_are, hospital-timed 12/12 what_state_youre_in. The issuer x predicate design never varied the attribute independently.
- Special categories: 21/96, all health (17) or criminal record (4). No religion, political opinion, union, sexual life, biometric, ethnicity or gender ideas appeared.
- Arms differ little by family mix (counts per family within 1-2 across arms).

## Open definitional issues

1. Uniqueness ("one per person") is a predicate form, but the attribute underneath (a real, distinct person or account holder) has no home; the two classifiers split on it.
2. Subsidy rolls: proposed rule: if what is proven is a status granted by an authority, it is an entitlement (what_you_hold); if it is the underlying condition (low income itself), it is a state.
3. Stability needs a definition (stability of the fact, or of the credential?) before it can be used.
