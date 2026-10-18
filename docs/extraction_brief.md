# Seed extraction brief (for extraction agents)

Repo: /Users/liangcc/projects/repos/zkID_explore. Read schema/seed.schema.json, seeds/000-examples.yaml and config/domains.yaml first.

Goal: produce ~10 seeds. A seed = one over-disclosure problem (someone must prove a small fact but ends up revealing/retaining much more, or a design that avoids that) + the minimal-disclosure mechanism (or its absence/failure) + a verbatim evidence quote from a real page you fetched.

Procedure per seed:
1. Find a real page (WebSearch / WebFetch to find it). 
2. Save a snapshot: `python3 scripts/fetch_snapshot.py <seed-id> <url>` (writes snapshots/<seed-id>.txt). If it fails or is empty/blocked, pick another page. Never invent a source.
3. Open the snapshot and COPY a sentence or two verbatim as evidence.quote (<= 300 chars, no paraphrase, keep original language). Grep the snapshot to confirm it is there.
4. Fill every required field. `problem` in the source's vocabulary; `abstract_problem` domain-neutral ("who must prove what small fact, what extra do they end up seeing/holding"); `mechanism` and `mechanism_outcome` honestly (a failure or legal blocker is a fine seed). `evidence.snapshot` = "snapshots/<seed-id>.txt", `quote_verified: false` (a script sets it). `extraction.agent` = your batch name, `status: draft`. Use domain values from config/domains.yaml leaf names where they fit.
5. Write all seeds to the YAML file named in your assignment (a YAML list). Then run `python3 scripts/verify_quotes.py` and fix or drop any seed of yours that fails. Do not edit other files' seeds.

Rules: no fabricated URLs or quotes; spread seeds across different sub-topics (do not write 10 variants of one story); prefer sources whose content is NOT about zero-knowledge proofs unless your assignment says so. Report back in <= 100 words: how many seeds verified, and any gaps.
