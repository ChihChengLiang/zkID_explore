# zkID_explore

Idea discovery for zero-knowledge identity (zkID). Agents start from **seeds**, read them, and emit **ideas** (not yet defined here).

## Seed

A seed is a bounded, re-visitable source plus instructions on how to read it. Schema: [schema/seed.schema.json](schema/seed.schema.json).

| Field | Purpose |
|---|---|
| `kind` | Shape of the source; selects crawl strategy |
| `topics` | Closed taxonomy, so seeds can be sliced by theme |
| `signal.looking_for` | Idea types the source tends to produce (open-problem, unmet-need, ...) |
| `crawl` | method, cadence, queries/links to follow |
| `trust` | normative / primary / informed / speculative, used to weight what an agent finds |
| `status` | candidate -> active -> paused/retired; agents only auto-crawl `active` |
| `verified` | URL check result, written by `scripts/check_urls.py --write` |

Seeds live in `seeds/*.yaml` (a list per file). New seeds enter as `candidate`; a human promotes them to `active`.

```bash
python3 scripts/validate.py          # schema + id/related integrity
python3 scripts/check_urls.py --write  # record reachability
```

## Batch 001

20 seeds across three groups: implementers (PSE zkID, longfellow-zk, Anon Aadhaar, zkPassport, Self, ZK Email, Semaphore), standards/specs (W3C VC, BBS, SD-JWT, OpenID4VP, ISO 18013-5, ICAO 9303, WICG Digital Credentials, EUDI ARF), and research/discussion (ePrint, ethresear.ch, ZKProof).
