# Triage pilot: structured predicate, channel and signals on 37 ideas

Sample: 37 ideas (17 from pilot 1, 20 from pilot 2, one idea per sampled cell), labeled by Sonnet and Haiku independently against `config/certificates.yaml` and `config/triage_schema.yaml`. Reproduce with `python3 scripts/analyze_triage.py`. Labels are model judgements; none were checked by a person yet.

## The catalogue
43 certificates, 274 claims. Provenance: 1 verified (EU PID rulebook, fetched 2026-10-19), 27 recalled from memory (including the ISO 18013-5 mDL elements, because the standard is paywalled and the EU mDL rulebook only references it), 15 hypothetical. TWDIW schemas were not checked (the site returned 403 to automated fetches). Taiwan field lists are approximations.

## Findings
- **About half need no real ZK, but need issuer cooperation.** zk_need: issuer_precomputed 20 (54%), zk_nullifier 5, zk_join 4, zk_aggregate 3, zk_derived 3, zk_nonmembership 2. "Precomputed" means the issuer signs the derived claim (as mDL does with age_over_NN). ZK is the way to get the same result when the issuer will not.
- **Most ideas slice one certificate.** 22 of 37 use one certificate, 5 use two, 1 uses three; mean 1.4 claims per idea. Joins are about one in six.
- **10 of 37 need an attribute no catalogued certificate carries** (a credential-gap list): card spend by merchant category, unpaid traffic fines register, animal-keeping ban register, ride-platform trip count and tenure, delivery-platform count and rating, peer-trade sales and dispute record, school guest pass, court guardianship order, temple or association membership, hospital visitor authorisation. They are platform-derived data, negative registers and community-issued credentials.
- **Channel:** 16 of 37 are in-person with no device (43%); evidence today is paper copy in 17 and digital upload in 11. Only 1 of 37 verifiers is judged able to read a wallet presentation today; 19 would need a tool, 17 unknown.
- **Signals:** harm per incident is mostly 3 (19) or 2 (13); verifier incentive is weak (1) for 26 and moderate (2) for 11, never strong; reach is 10^4 for 14, 10^5 for 13. `split_incentive` is true for 34 of 37, so as a binary it carries almost no information.
- **Orthogonal to the critic's "real opportunity":** channel, evidence type and reach show no clear relation to it at n=37 (in-person-no-device 5 of 16, remote-online 2 of 8). Issuer-precomputed ideas score a little higher on rubric (2.80) than ZK-needing ones (2.35), real 7 of 20 vs 4 of 17. Too few to conclude anything.

## Reliability (Sonnet vs Haiku, of 37)
operator 35, zk_need 31, verifier incentive 30, harm 24, interaction mode 23, unlinkability 22, current evidence 20, **verifier_reader 13**; reach within one order of magnitude 37 (exact 15); same set of certificates 18. Channel and verifier-tooling labels are the least reliable and are exactly the ones that depend on Taiwanese practice, so they need a person's check before use. Haiku also used the catalogue's `precomputable` names as if they were claims (26 non-catalogue references); Sonnet followed the claim list. Whether a precomputable claim counts as an input is a schema decision still open.

## Open
- Replace `split_incentive` with something that varies (who pays, who gains).
- Decide whether precomputable claims are valid inputs.
- A person should check the channel and tooling labels on these 37 before they are applied to all 246.
- Possibly out of date: earlier artefacts treat age 20 as the Taiwan adult age; the legal age of majority was lowered to 18 in 2023 (recalled, not verified), which would change age-threshold predicates.
