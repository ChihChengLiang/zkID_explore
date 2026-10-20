# zkID_explore

Where could zero-knowledge or selective-disclosure ID help in Taiwan? This repository holds a pipeline that looks for everyday situations where someone is asked for a whole document when the other side needed one fact, generates candidate use cases, and screens them.

**Live views:** <https://chihchengliang.github.io/zkID_explore/> — an [idea whiteboard](https://chihchengliang.github.io/zkID_explore/whiteboard.html), a [source → attribute → asker diagram](https://chihchengliang.github.io/zkID_explore/flow.html) and the [MyData worksheet](https://chihchengliang.github.io/zkID_explore/mydata.html).

## What came out

- **246 candidate use cases** from 33 scenarios (96 from 8 issuer-led scenarios, 150 from 25 setting-led ones).
- **80 pass all three tests** of a "real opportunity": today's request goes beyond the checker's purpose, a narrow proof still serves that purpose, and no legal duty is flagged as blocking.
- **Strongest scenarios:** member-only votes and tickets, lending across partner libraries, night-market stall permits, age checks at lockers and kiosks, protection-order proof, hospital status without the diagnosis. **Weakest:** banks, government counters, courts and telecoms, where the checker is entitled to the whole record.
- **Pattern:** opportunities cluster where the body that signs is the body that asks and no law makes it keep a copy.
- **Technology (37-idea sample):** about half need only an issuer-signed derived claim; the rest need real zero-knowledge (uniqueness, joins, aggregates, absence proofs); about a quarter need a credential nobody issues yet.

Details: [pilot 1](docs/pilot_results.md), [pilot 2](docs/pilot2_results.md), [triage test](docs/triage_pilot.md).

> **Treat these as hypotheses.** Candidates were generated and screened by AI models (Claude Sonnet and Haiku). A person checked only 30 pairs for duplicates. Legal verdicts are unverified (118 of 246 are marked "unclear"), nothing was tested with a real verifier, issuer or lawyer, and the certificate catalogue is partly recalled from memory. Hand labels are in [`labeling/`](labeling/).

## The idea behind the tests: contextual integrity

The screening borrows from Helen Nissenbaum's theory of **contextual integrity** ("Privacy as Contextual Integrity", 2004; *Privacy in Context*, 2010). Its core claim: privacy is not secrecy or control, it is whether information *flows* in ways that fit the norms of the setting it came from. A diagnosis moving from patient to doctor is fine; the same diagnosis moving to an employer is not.

A flow has five parts: who sends it, who receives it, who it is about, what kind of information it is, and the **transmission principle**, the condition under which it flows (consent, a legal requirement, a payment, confidentiality). A flow breaks the norms when any part departs from what the setting allows, and a norm can itself be judged by whether it serves the setting's purpose.

That gives this project its tests: does today's request ask for more than the checker's purpose needs, would a narrower proof still serve that purpose, and does a legal duty (the transmission principle) stand in the way? It also supplies the axes used to define scenarios (see [docs/contextual_integrity.md](docs/contextual_integrity.md)). The theory says nothing about whether a better flow would actually be adopted; that part is treated separately here and is mostly unmeasured.

## How the pipeline works

| Stage | What happens | Where |
|---|---|---|
| Seeds | 39 evidence-backed precedents (forms, laws, regulator decisions, standards, deployments), each with a verbatim quote checked against a fetched copy | `seeds/`, `schema/seed.schema.json`, `scripts/verify_quotes.py` |
| Scenarios | Cells defined by setting, attribute family, predicate, transmission principle and origin/use context (frame: contextual integrity) | `config/pilot_cells.yaml`, `config/pilot2_cells.yaml`, `config/axes.yaml`, [docs](docs/contextual_integrity.md) |
| Generation | Isolated agents, one per cell and arm, each given six seeds and asked for three ideas with provenance | `prompts/`, `prompts2/`, `ideas/`, `ideas2/` |
| Screening | Blind critic: norm violation, purpose-sufficiency, legal flag, aggregation, adoption | `critic/`, `critic2/`, `critic_p2/` |
| Analysis | Embeddings (Qwen3-Embedding-0.6B via LM Studio), clustering, attribute and context labels, source/asker types | `scripts/analyze*.py`, `scripts/embed_analysis.py`, `classify*/` |
| Triage test | Certificate catalogue, structured predicates, channel and signals on 37 ideas | `config/certificates.yaml`, `config/triage_schema.yaml`, `triage/` |
| Views | Whiteboard, flow diagram, MyData page | `scripts/build_whiteboard.py`, `scripts/build_flow.py`, `scripts/build_mydata_page.py` → `docs/` |

Two arms of seed selection were compared (distance-banded vs random); they did not differ measurably at this scale. The scenario definition mattered far more than the seeds.

## Layout

```
docs/        GitHub Pages site (index, whiteboard, flow, mydata) and write-ups (*.md)
data/        MyData worksheet as CSV, taxonomy pulls (Google place types, OSM, Your Europe)
config/      scenario cells, axes, certificate catalogue, schemas, type lists
seeds/  sources/  schema/     precedents, corpora to mine, JSON Schemas
ideas*/  prompts*/  critic*/  classify*/  triage/  labeling/   run outputs and inputs
scripts/     builders, validators, analysis
```

## Reproducing

Python 3 with `pyyaml` and `jsonschema`; `numpy` and `scikit-learn` for the whiteboard layout; [LM Studio](https://lmstudio.ai) serving `text-embedding-qwen3-embedding-0.6b` for embedding analysis.

```bash
python3 scripts/validate.py                # validate source registry
python3 scripts/verify_quotes.py           # check seed quotes against snapshots/
python3 scripts/analyze.py                 # pilot 1 summary (critic v1)
python3 scripts/analyze_p2.py              # pilot 2 summary
python3 scripts/build_mydata_page.py       # rebuild docs/mydata.html from data/mydata
```

Generation and review were run by Claude subagents from the committed prompts; the outputs are committed, so the analysis and views rebuild without re-running them. Fetched source pages (`snapshots/`) and embedding caches are not committed; `scripts/fetch_snapshot.py <id> <url>` recreates a snapshot.

## Data and sources

- The MyData worksheet was a spreadsheet; it is now [`data/mydata/*.csv`](data/mydata) plus the [web page](docs/mydata.html).
- Taxonomies in `data/taxonomies/` come from Google Places types, OpenStreetMap (via taginfo) and the EU Your Europe portal; see `scripts/pull_taxonomies.py`.
- The EU PID attribute list in `config/certificates.yaml` was checked against the EU wallet rulebook (fetched 2026-10-19). ISO 18013-5 elements and Taiwan certificate fields are recalled from memory and marked as such.

## License

No license file yet; until one is added, all rights are reserved by default.
