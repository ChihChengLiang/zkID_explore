# Pilot 2 results (25 cells x arms C and D x 3 ideas = 150 ideas)

Run 2026-10-18. Cells from `config/pilot2_cells.yaml` (setting, attribute family, predicate, transmission principle, origin and use context fixed; issuer left open). Arm C: 6 seeds banded by Qwen3-embedding distance to the cell (nearest decile dropped, 1 mid and 5 far, mixed domains, one failure or legal-blocker seed). Arm D: 6 random seeds from distinct domains. Seed use was mandatory (at least two seeds cited, with a "In <seed>, X does Y; here Z plays that role" mapping). Generator and critic: Sonnet, critic v2 (see `docs/contextual_integrity.md`), blind to arm and cell, 19 batches. Taiwan-law checks were **not** done (13 of 25 cells flagged `check: true` stay unverified). Reproduce with `python3 scripts/analyze_p2.py`.

## C vs D: no real difference, with one signal

| | C banded | D random |
|---|---|---|
| rubric (v2) | 2.80 ± 0.14 | 2.79 ± 0.14 |
| novelty | 3.80 ± 0.20 | 3.85 ± 0.21 |
| real opportunity (norm violated, purpose-sufficient, not blocked) | 26 / 75 | 34 / 75 |
| provenance judged faithful | 14 / 75 | 35 / 75 |
| within-cell pairwise distance (embeddings) | 0.353 | 0.339 |

- Rubric, novelty and diversity are indistinguishable. Real-opportunity counts differ by 8 of 75 (z about 1.3, not significant).
- **Provenance is the one gap that looks real:** the far, embedding-banded seeds were cited faithfully 19% of the time, random seeds 47%. Caveat: provenance verdicts flip with the critic's prompt (pilot 1: v1 6 of 72 faithful, v2 38 of 72), so treat it as a hint. Plausibly, seeds that are farther from the cell are harder to map onto it.
- So there is still no evidence that targeting by distance beats random diverse seeds. The cheaper arm (D) is at least as good.

## The cells, not the seeds, set the diversity
- New ideas sit as far from pilot 1 as pilot-1 ideas sit from each other across cells: mean distance (1 - cosine) to the nearest pilot-1 idea is 0.40 (C 0.399, D 0.401), against 0.400 for pilot-1 to its own other-cell neighbours. No pair of ideas from different pilot-2 cells has cosine above 0.71.
- Within a cell, the three ideas are closer than in pilot 1 (0.35 vs 0.42-0.48), as expected when the cell fixes the fact to prove.

## What the new axes showed
- **Violated parameter** (critic v2): information_type 69, retention 42, recipient 33, transmission principle 2, none 4. Pilot 1 was 77 / 12 / 5 / 0. Adding settings with retention and recipient problems (building votes, protection orders, public registers) broadened the kinds of problem found.
- **By transmission principle** (cell-assigned), real opportunities: consented-for-benefit 23 of 42, commercial-convenience 8 of 24, required-by-law 20 of 48, safety-security 7 of 30, public-record 2 of 6. Safety-security cells are weakest (the verifier's need is tied to protection). For required-by-law the critic called the legal question unclear on 36 of 48 and "blocks" on 7, so those numbers need the law check.
- **By attribute family**, real opportunities: where_you_belong 22 of 36, what_youve_done 11 of 24, who_you_are 9 of 24, who_you_are_linked_to 6 of 30, what_you_hold 5 of 18, what_state_youre_in 5 of 6 (one cell, n=6), what_you_can_do 2 of 12. Relationship cells (guardian, next of kin, partner, delegate) rarely yield a clean opportunity: the verifier legitimately needs the relationship itself.
- **Cross-context** (origin different from use): purpose-sufficient 48 of 120 (40%) vs 16 of 30 (53%) for same-context. Direction matches pilot 1, weaker.
- **Cells with zero real opportunities:** tourist-scooter, inheritance-bank, school-pickup, roommate-peer. **Best:** party-primary 6/6, dv-lease-break 5/6, library-network 5/6, union-ballot 5/6.

## Top-rated ideas (rubric 4; 16 of 150)
Protection-order leave or lease break without handing over the order (4 ideas across both arms); age check at vending lockers and kiosks (4); indigenous-status check for aid without the household register (3); nurses' union ballot by phone (novelty 5); member-only party Q&A ticket unlinkable across events (novelty 5); partner-library borrowing without exposing loan history; fan-club presale "one real member per ticket"; night-market stall-slot lottery without copying the permit; migrant-worker lease renewal without photocopying the ARC and work permit. Several top items repeat within a cell (the same idea in C and D), so the count of distinct ideas is lower than 16.

## Caveats
- Critic and generator are the same model family; critic labels on adoption are mostly "unknown" (issuer willing: 115 of 150 unknown), and legal verdicts are unverified.
- Cell definitions bake in the predicate, so purpose-sufficiency rates are not comparable to pilot 1 (real-opportunity 40% here vs 21% there).
- Provenance verdicts are prompt-sensitive; one batch had 6 ideas, and two critics named the reasons field differently (analysis was unaffected).
- One run per arm and cell; no repeats.
