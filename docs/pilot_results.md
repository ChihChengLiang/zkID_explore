# Pilot results (8 cells x 4 arms x 3 ideas = 96 ideas)

Run 2026-10-18. Generator: Sonnet subagents, one isolated run per cell-arm. Critic: Sonnet, blind to arm and cell, 12 shuffled batches of 8. Seed distance rated 0-10 by Haiku; idea clustering by Haiku. Seed corpus: 39 verified seeds (12 in-domain, 11 adjacent, 16 distant). Raw data: `ideas/`, `critic/`, `prompts/manifest.json`; reproduce the tables with `python3 scripts/analyze.py`.

Arms: A no seeds, B six near seeds, C six distance-banded seeds, D six random seeds from distinct domains.

## Headline

**No arm beat any other at this sample size.** Every 95% interval overlaps. Seeds did not break convergence.

| Arm | n | Rubric | Validity | Coherence | Novelty |
|---|---|---|---|---|---|
| A none | 24 | 2.50 ± 0.26 | 2.62 ± 0.28 | 3.29 ± 0.32 | 3.25 ± 0.48 |
| B near | 24 | 2.67 ± 0.28 | 2.71 ± 0.25 | 3.12 ± 0.30 | 2.92 ± 0.44 |
| C banded | 24 | 2.71 ± 0.19 | 2.67 ± 0.25 | 3.12 ± 0.32 | 3.42 ± 0.49 |
| D random | 24 | 2.46 ± 0.20 | 2.58 ± 0.29 | 3.04 ± 0.30 | 3.33 ± 0.40 |

Novelty is highest for C and D and lowest for B, which points the way the Liu et al. result predicts, but the gaps (0.5) are about the size of the intervals. Treat as a hint, not a finding.

## Other observations

- **Convergence is strong regardless of seeds.** 96 ideas fell into 50 clusters. A cell's 12 ideas span only 4-8 distinct clusters (telco-unique 4, utility-member 5, gov-nonmember and hospital-timed 8). 17-20 of 24 ideas per arm share a cluster with an idea from another arm in the same cell (C highest at 20/24, so targeting did not diversify outputs).
- **Quality is low overall.** Rubric scores: 45 twos, 46 threes, 5 fours, no fives. The five fours came from arms A (2) and B (3); none from C or D.
- **Provenance is mostly decorative.** The critic judged 66 of 72 seeded ideas' borrowings unfaithful (B 19/24, C 24/24, D 23/24); six were faithful. Either the generators ignored the seeds ("use any that help" invited this) or the critic is harsh. Both are plausible; I have not checked which.
- **Kill tests barely discriminate.** `issuer_unwilling` and `no_wallet` fail in 40-79% of ideas in every arm, so survival is 4-25% across arms. D has the lowest survival (1 of 24). These look like properties of the cell setup (non-government issuers, no wallet) more than of the seeds.
- **Cells differ more than arms.** Cell effects on cluster count dwarf arm effects.

## Caveats

- n = 24 per arm, one run, no repeats. This can rule out large effects, not small ones.
- Generator and critic are the same model family. You chose that deliberately; it still means shared blind spots.
- Critic batches contain 8 ideas, so scores are not fully independent. No human spot-check has been done yet (the design called for 20 blind).
- Retention-law and issuer-willingness verdicts are the critic's judgement without a Taiwan-law source. Treat `fails` as hypotheses.
- Distance scores come from Haiku ratings, not embeddings. Clusters come from one Haiku pass.
- The seed corpus has gaps (no India, Estonia, CNIL/ICO decision; some vendor-doc seeds).
- Clustering is within-moment; cross-cell duplicates were 0, so cell identity dominates.

## What this suggests, and what it does not

It does not support "diverse seeds break the homogeneity" at this scale, and it matches PaperGym's finding that targeting ties with random. Arm A (no seeds) is already as good as the seeded arms by rubric, so the cell definition itself may be doing most of the steering. The cheapest next experiments, in order: (1) make seed use mandatory and check it (a "must borrow structure from at least 2 seeds, state the mapping" prompt) rather than optional; (2) score 20 ideas by hand to calibrate the critic; (3) repeat the same 32 runs to see run-to-run variance before reading anything into arm gaps.

## Addendum: re-run with real embeddings (Qwen3-Embedding-0.6B via LM Studio)

`PYTHONPATH=<openpyxl dir> python3 scripts/embed_analysis.py` (needs LM Studio on :1234; about 10 texts/s, vectors cached in `cache/`, gitignored).

- **Haiku distance ratings are only moderately reliable.** Spearman against embedding distance per cell: 0.33-0.59, mean 0.46. The arm C/D draws were built on those ratings.
- **Distance enforcement did work in embedding space.** Mean distance (1 - cos) from seed set to cell target: B 0.41, C 0.51, D 0.49. C and D are close, so C was barely farther than random.
- **Within-cell spread of the 3 ideas per arm** (pairwise distance, mean over 8 cells): A 0.446, B 0.478, C 0.466, D 0.423 (intervals about ±0.04). Paired by cell: C-D = +0.044 (C higher in 7/8 cells), B-A = +0.032 (6/8), C-A = +0.020 (5/8), D-A = -0.024 (2/8). Direction: D (random) is the least varied and C/B the most, the opposite of "random is as good". With 8 cells a 7/8 split is p about 0.07, so this is a weak hint, not a result.
- **Novelty vs the 15 workbook rows** (1 - max cos): A 0.435, B 0.452, C 0.430, D 0.452. No difference. Distance of ideas to the cell target: 0.45-0.46 for all arms.
- **Convergence is threshold-dependent.** Greedy clustering inside each cell gives 9.5 / 10.6 / 11.6 distinct clusters of 12 at cosine 0.80 / 0.85 / 0.90, versus 4-8 from the Haiku pass. The Haiku pass judged "same moment and verifier"; raw embeddings of long text are stricter. Neither threshold is calibrated against human labels, so "heavy convergence" from the main results should be read as unconfirmed. Same-cell pairs have median cosine 0.57, p90 0.73.
- **Bottom line unchanged:** no arm clearly beats another. The embedding metrics add a faint ordering (B, C above A, D below) that the earlier judge-based numbers did not show.
