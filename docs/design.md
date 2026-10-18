# Diverse-seed zkID use-case discovery: design proposal

Status: proposal. Nothing here has been run. Items marked **[cost]** need your go-ahead.

## 0. Corrections to my earlier batch

My first commit treated a "seed" as a *place to look* (a URL plus crawl cadence). Your handoff defines a seed as an *extracted, verified triple* (problem, mechanism, domain, source, evidence). So there are now two layers:

| Layer | File | What it is |
|---|---|---|
| Source | `schema/source.schema.json`, `sources/*.yaml` | A corpus to mine (the 20 entries from batch 001). Mostly zkID-internal, so these only cover the near/in-domain end. |
| Seed | `schema/seed.schema.json`, `seeds/*.yaml` | One verified extraction. This is the unit agents are fed. |

Batch 001 stays as a registry of in-domain sources. The distant sources in section 1 are what batch 001 lacks.

One thing about the workbook: its Discovery Matrix is not empty. Every cell has a one-line hint. They read as placeholders rather than researched cases, so I treat all 40 cells as open.

## 1. (a) Seed schema and source types

Fields are in `schema/seed.schema.json`. The parts that matter:

- `problem` is in the source's own vocabulary. `abstract_problem` is the same problem stated domain-neutrally ("a gatekeeper needs one small fact but the proof doubles as an identifier"). Retrieval embeds and paraphrases `abstract_problem`, which is the PaperGym stage-2 move.
- `mechanism_outcome` (works / partial / fails / blocked-by-law) lets failures and legal blockers be seeds too, which feeds the kill test.
- `distance_class` is fixed at extraction. Per-cell distance is computed later (section 2).
- `evidence.quote` must be verbatim, and `quote_verified` is only set by a script that greps the stored snapshot. The two seeds in `seeds/000-examples.yaml` were verified this way against the live RFC 9576 and GDPR Art. 5 pages.
- `axes` (issuer, predicate, regime, harm) are coverage tags for stratified sampling, not retrieval keys.

### Ten seed source types

| # | Type | Distance | Where to get it | What it yields |
|---|---|---|---|---|
| 1 | Over-collection artifacts: application forms, 應備文件 checklists, counter practices | in-domain | Agency service pages on gov.tw and MyData's service list; bank account-opening forms; 內政部 lease templates; telco and real-estate counter forms | The "data disclosed today" side, with concrete over-asks |
| 2 | Harm cases: breaches, doxxing, stalking, scams from retained ID scans | in-domain | Taiwan 165 anti-fraud notices, news archives for 個資外洩, HIBP and Privacy Rights Clearinghouse, PTT/Dcard threads | `harm` axis; the stakes |
| 3 | Regulations | adjacent | law.moj.gov.tw (個資法, 洗錢防制法), FSC KYC rules, GDPR Art. 5 and 25, eIDAS 2.0 | Whether ZK helps at all (retention duties); kill-test inputs |
| 4 | Enforcement decisions on over-collection | adjacent | CNIL / EDPB decisions on ID-copy retention, Taiwan 司法院 judgments citing 個資法, FTC orders | Real cases where "too much was asked" was ruled on |
| 5 | Deployments | adjacent | TWDIW wallet docs, EUDI ARF, Google and Apple wallet age verification, Swiss e-ID | What actually shipped and which constraints bit |
| 6 | Papers | adjacent | Batch 001 sources (ePrint, ZKProof), citation chains from them | Mechanisms |
| 7 | Foreign portals | adjacent | Korea NPKI service lists, EU SDG life events, India DigiLocker, Estonia X-Road | Other countries' "moments" and issuer structures |
| 8 | Practitioner complaints | in-domain | PTT / Dcard / Reddit / HN threads on "why do you need a photocopy of my ID", 消保官 case summaries | Unfiltered friction |
| 9 | KYC process docs | in-domain | Regulator guidance, bank and exchange KYC checklists, NCC SIM-registration rules | Retention duties by sector |
| 10 | Distant analogs of minimum disclosure | distant | Privacy Pass (RFC 9576-9578), Chaum blind signatures, OAuth scopes, PCI tokenization, HIPAA "minimum necessary", secret-ballot literature, library patron-record rules, bouncer age checks | The far end. Where cross-domain novelty is expected to come from |

Types 3, 4 and 9 are the ones with a built-in answer to "does ZK help here", so they double as the kill-test corpus.

**Targets for a first corpus:** about 120 seeds, roughly 20% in-domain, 40% adjacent, 40% distant, with every `axes` value appearing at least 3 times. **[cost]** Extraction is an LLM-plus-fetch job. I'd estimate low hundreds of fetches and one extraction call per source.

## 2. (b) Cell-by-cell agent plan

### Cells

Rows are the 8 attribute sources; columns are the 5 workbook predicates plus the 3 you named (non-membership, time-bounded, aggregate). That is 8 x 8 = 64 cells. I suggest running the original 40 first.

### Per-cell procedure

1. **Target descriptor.** Write the cell as an abstract problem in the same style as `abstract_problem`: "a [issuer type] can attest [predicate type]; a verifier wants only the predicate."
2. **Paraphrase into k domains.** For each of the 7 domain groups in `config/domains.yaml`, rewrite the descriptor in that domain's vocabulary. Embed each paraphrase.
3. **Candidate pool.** For every verified seed, take the cosine distance from its `abstract_problem` embedding to the target descriptor.
4. **Distance enforcement:**
   - Drop the nearest decile (near-duplicates of the target teach nothing).
   - Draw from bands: 1 seed from the 40-60th percentile of distance, 3 from above the 70th, so most seeds are far.
   - Hard constraints: no two seeds share a `domain`; at least 2 seeds from domain groups outside {government, finance, identity}; at least 1 seed with `mechanism_outcome` in {fails, blocked-by-law}; `distance_class = distant-analog` for at least 2.
   - A hand-defined domain-tree distance is a sanity check on the embedding distance, since embeddings can rate two analogs as close because of shared surface words.
5. **Generate.** An isolated agent gets the cell, its 6 seeds and the idea schema. Three ideas per cell. No cross-cell visibility.
6. **Provenance.** Each idea lists `inspired_by: [{seed_id, borrowed_aspect}]`. A critic later checks that the borrowed aspect actually appears.

### Arms (this is what separates "targeting" from "just diverse")

| Arm | Seeds given | Tests |
|---|---|---|
| A | None | Baseline |
| B | 6 near seeds (in-domain, same issuer type) | Does near material help? Your Liu et al. finding says no |
| C | 6 selected by the paraphrase-and-distance procedure above | The proposed method |
| D | 6 random draws, distinct domains, no targeting | **Control.** PaperGym found C tied D |

Same model, same prompt template, same number of ideas, for all arms. If C does not beat D here either, the cheaper pipeline is D plus provenance plus the kill test.

### Late merge

Embed each idea (moment + predicate + issuer). Cluster at a fixed threshold (start at cosine 0.85 and calibrate on a hand-labelled sample of 30 pairs). Keep one representative per cluster, with all provenance unioned. Mark clusters that span multiple cells or arms.

### Kill-test pass (every surviving idea)

Four checks with a yes/no and a one-line reason each: (1) retention law applies and removes the benefit; (2) linkability defeats the point (stable identifier or issuer sees every presentation); (3) the issuer has no incentive or ability to sign; (4) the user has no wallet or the verifier has no integration path today. An idea with a failed check is kept but tagged, not deleted, so the failure pattern is data.

### Cost sketch **[cost]**

40 cells x 4 arms x 1 generation call (3 ideas) = 160 generation calls, about 480 ideas, then one critic call per idea plus pairwise arm comparisons. A **pilot of 8 cells** (one per attribute source, predicate varied) is 32 generation calls, which is enough to see whether the arms differ at all. I recommend running the pilot first.

## 3. (c) Critic and metrics

### Independence

The critic must be a different model family from the generator, and must not see arm labels, seed contents or cell names. Run each idea twice with the rubric order shuffled. Human spot-check: you score 20 ideas blind, and I report critic-vs-you agreement before trusting any arm comparison.

### Critic prompt (draft)

```
You are reviewing a proposed zero-knowledge / selective-disclosure use case for Taiwan.
You will see ONE idea. You do not know how it was produced. Be sceptical.

IDEA
{title}
Everyday moment: {moment}
Verifier: {verifier}
Predicate actually needed: {predicate}
Data disclosed today: {disclosed_today}
Attribute source (issuer): {issuer}
Claimed borrowed mechanism: {borrowed_aspect}   (omit if none)

Score each item, with a one-sentence justification FIRST, then the score.

1. rubric_score (1-5), using this rubric verbatim:
{paste Scoring Rubric tab}
2. validity (1-5): is the moment real in Taiwan, is the predicate really sufficient for the verifier's decision, and could the named issuer plausibly sign it?
3. coherence (1-5): are the parts of the idea consistent with each other?
4. novelty (1-5): compared with this list of already-known cases, is it a different moment, predicate or issuer, or just a rewording?
   KNOWN: {the 15 workbook rows, one line each}
5. provenance_faithful (yes/no/NA): does the idea actually use the claimed borrowed mechanism, or is the attribution decorative?
6. kill_tests: for each of retention-law, linkability, issuer-unwilling, no-wallet answer {fails | holds | unknown} with one line of reasoning. Cite the specific law or practice if you claim retention applies; say "unknown" rather than guess.

Return JSON only:
{"rubric_score":n,"validity":n,"coherence":n,"novelty":n,"provenance_faithful":"yes|no|NA","kill_tests":{...},"reasons":{...}}
```

Why the justification comes before the score, and why `unknown` is allowed: it reduces confident invention of legal claims. Taiwan retention claims should be checked by you or a Taiwan-law source before they are treated as facts.

Arm comparisons use a second, pairwise prompt (idea X vs idea Y, same cell, both orders) to cancel position bias.

### Dedupe and diversity metrics (computed per arm, per cell and overall)

| Metric | Definition | Tells you |
|---|---|---|
| Distinct clusters | Number of clusters after the merge step, per 100 ideas | Raw repetition |
| Mean pairwise distance | Mean cosine distance between idea embeddings within an arm | Spread |
| Vendi score | Effective number of distinct items from the similarity matrix | Spread, less threshold-sensitive |
| Novelty vs workbook | 1 minus max cosine to the 15 existing rows | Whether we got past the single-seed workbook |
| Cell coverage | Share of cells with at least 1 idea passing validity >= 3 | Whether the matrix actually filled |
| Seed utilisation | Share of seeds cited at least once | Whether the pool is used or ignored |
| Abandonment | Share of attributions the critic marks `provenance_faithful = no` | PaperGym's 1/30 vs 8/30 signal |
| Survival rate | Share of ideas holding all four kill tests | Practical value, not just novelty |
| Critic reliability | Agreement (weighted kappa) between the two shuffled critic runs, and with your 20 spot-checks | Whether any of this is believable |

Report effect sizes with intervals. With 8 pilot cells and 3 ideas per arm the sample is small, so the pilot can rule out large differences but cannot prove C beats D.

## 4. Open questions for you

1. Embedding model for distance and dedupe: local (cheap, fine for a pilot) or an API one?
2. Generator and critic families. I'm a Claude model, so the critic should be non-Claude. Which do you have access to?
3. Is 8 pilot cells then 40 the right ramp, or do you want all 64 at once?
4. Taiwan-law claims in kill tests: do you have a trusted source or person for spot-checks?
