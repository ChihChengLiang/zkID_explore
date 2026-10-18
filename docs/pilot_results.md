# Pilot results (8 cells x 4 arms x 3 ideas = 96 ideas)

Run 2026-10-18. Generator: Sonnet subagents, one isolated run per cell-arm. Critic: Sonnet, blind to arm and cell, 12 shuffled batches of 8. Seed distance rated 0-10 by Haiku; idea clustering by Haiku. Seed corpus: 39 verified seeds (12 in-domain, 11 adjacent, 16 distant). Raw data: `ideas/`, `critic/`, `prompts/manifest.json`; reproduce the tables with `python3 scripts/analyze.py`.

Arms: A no seeds, B six near seeds, C six distance-banded seeds, D six random seeds from distinct domains.

## Headline

**No arm beat any other at this sample size.** Every 95% interval overlaps. (The earlier claim that seeds did not break a heavy convergence is withdrawn; see the hand-labeling addendum.)

| Arm | n | Rubric | Validity | Coherence | Novelty |
|---|---|---|---|---|---|
| A none | 24 | 2.50 ± 0.26 | 2.62 ± 0.28 | 3.29 ± 0.32 | 3.25 ± 0.48 |
| B near | 24 | 2.67 ± 0.28 | 2.71 ± 0.25 | 3.12 ± 0.30 | 2.92 ± 0.44 |
| C banded | 24 | 2.71 ± 0.19 | 2.67 ± 0.25 | 3.12 ± 0.32 | 3.42 ± 0.49 |
| D random | 24 | 2.46 ± 0.20 | 2.58 ± 0.29 | 3.04 ± 0.30 | 3.33 ± 0.40 |

Novelty is highest for C and D and lowest for B, which points the way the Liu et al. result predicts, but the gaps (0.5) are about the size of the intervals. Treat as a hint, not a finding.

## Other observations

- **(Superseded by the hand-labeling addendum below.) Haiku found strong convergence.** 96 ideas fell into 50 clusters. A cell's 12 ideas span only 4-8 distinct clusters (telco-unique 4, utility-member 5, gov-nonmember and hospital-timed 8). 17-20 of 24 ideas per arm share a cluster with an idea from another arm in the same cell (C highest at 20/24, so targeting did not diversify outputs).
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

## Addendum 2: hand-labeling 30 same-cell pairs

30 pairs sampled evenly across the embedding-similarity range (5 per cosine band, cosine and arm hidden), labeled by the project owner in `labeling/labels.csv`.

- **28 different, 1 same, 1 unsure.** The only "same" was pair 27 (cosine 0.69). Pairs at cosine 0.70, 0.71 and 0.76 were labeled different, and the most similar pair (0.88) was "unsure".
- **No cosine threshold separates them.** Every threshold misclassifies at least one pair; the 0.97 "best accuracy" of `calibrate_threshold.py` is just "call everything different" and its suggested T of 0.86 is meaningless with one positive.
- **Duplicates among same-cell pairs are rare.** The bands hold equal numbers of pairs, so the sample is close to uniform over same-cell pairs: 1 of 29 judged pairs is about 3% (a 95% interval of roughly 0.1% to 18% at this n). The Haiku clustering (26 multi-idea clusters out of 50) and the greedy cosine clusters both merged far more than a human did, so **the earlier "heavy convergence" finding does not hold**: the generated ideas are mostly different situations.
- **Consequences.** (1) Diversity metrics based on cluster counts at any threshold should not be used; use the continuous ones (mean pairwise distance, Vendi). (2) The earlier reading that seeds failed to diversify is unsupported either way; diversity here is high in all arms. (3) The arm differences in quality (rubric 2.5-2.7) and the critic's near-universal "decorative provenance" verdict are now the more interesting signals.
- **Limits:** one rater, one "same", a stratified sample of 30. This establishes that duplication is low; it does not give a calibrated threshold. Several more "same" examples would be needed for that, which the current corpus may not contain.

## Addendum 3: contextual-integrity re-score (critic v2) and context classification

Critic v2 (norm violation, purpose-sufficiency, transmission check, aggregation, adoption; see `docs/contextual_integrity.md`) re-reviewed the same 96 ideas, and Sonnet and Haiku labeled transmission principle and origin/use context. `python3 scripts/analyze_ci.py` reproduces the tables.

**Critic v2**
- Norm violated today: 69 yes, 25 unclear, 2 no. The violated parameter is `information_type` in 77 cases (retention 12, recipient 5). Almost all ideas are "asks for more than needed"; none concern consent or purpose creep.
- Purpose-sufficiency: 66 partly, 27 sufficient, 3 insufficient. The minimal flow usually serves the verifier's purpose only partly, so "what is lost" is the main filter.
- A "real opportunity" (violated yes, sufficient, not blocked) is **20 of 96, and exactly 5 per arm**. On this stricter measure the four arms are identical.
- Rubric: v1 and v2 agree exactly on 61/96 (all within 1). Arm means v2: A 2.46, B 2.75, C 2.75, D 2.67; v1: A 2.50, B 2.67, C 2.71, D 2.46. D flips from lowest to middle between critics, so arm gaps are critic-dependent noise at this size.
- **Correction:** the v1 verdict that 66 of 72 seeded ideas' borrowings were "decorative" does not survive rewording the prompt. v2 marks 38 "yes" and 34 "no". Provenance faithfulness is judge-dependent; do not cite "seeds were ignored" as a finding.
- The critic cannot judge law or adoption: `permits_minimal_flow` is unclear for 44, blocks for only 2; `issuer_willing` is unknown for 76 and "no" for 20 (never "yes"); aggregation is low or medium everywhere. These checks need local evidence (a Taiwan-law source, interviews), not a model.
- One generator output (employer-fresh A idea 0) has a title from one idea and a moment from another; the critic flagged it. Left in the data.

**Context and transmission classification (Sonnet; Haiku agrees on 91/96 origin, 77 use, 79 distance, 72 transmission)**
- Context distance: 48 different, 33 adjacent, 15 same. Transmission principle (today): 36 consented-for-benefit, 28 commercial-convenience, 21 safety/security, 10 required-by-law, 0-1 public-record. Transmission principle is the least reliable label (75% agreement).
- Origin contexts follow the cells (employment, telecom, utilities, finance, healthcare, education about 12 each). **Use contexts pile up in housing (23) and commerce (19).** Civic/community, family/social and religion are never used as origin or use; justice/security appears once. The new axes describe the gap, they do not close it; the cell design still has to force these settings.
- Same-context ideas are judged "sufficient" more often (7/15, 47%) than adjacent (8/33) or different (12/48), both about 25%. n is small, but it fits the theory that cross-context flows lose more when minimised.
- Commercial-convenience cases are legally the easiest (24 of 28 permit the minimal flow) but the verifier has little reason to change; consented-for-benefit cases carry most of the "unclear" legal verdicts (16 of 36). Hypothesis for the adoption question: the easy cases are the ones where the verifier collects for convenience, so the barrier is incentive, not law.
