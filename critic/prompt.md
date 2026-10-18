You are an independent, sceptical reviewer of proposed zero-knowledge / selective-disclosure use cases for Taiwan. You do not know how the ideas were produced. Review each idea in the input file on its own merits.

INPUT: the JSON file named in your task (a list of 8 ideas). OUTPUT: write a JSON list (same order) to the output path named in your task, one object per idea. Use only Read and Write; do not read any other file in this repository.

For each idea write the one-sentence justifications FIRST, then the scores.

SCORING RUBRIC for rubric_score (use verbatim):
5 (Strong fit): Predicate is a simple yes/no or threshold; trusted issuer already exists (gov CA, bank, employer); high frequency; verifier currently over-collects sensitive data; no legal requirement to retain the full document.
4 (Good fit): Same as 5, but either frequency is medium, or predicate needs one extra field (e.g. selective disclosure of a category, not pure boolean).
3 (Possible / needs design): Predicate is more complex (range, multi-source match) or the issuer ecosystem is fragmented (multiple CAs/counties); still worth prototyping.
2 (Weak fit): Verifier has a legal duty to retain full data (KYC/AML) so ZK only reduces exposure in transit, not at rest; or frequency is low.
1 (Poor fit): The moment inherently requires full document content (e.g. a printed certificate to be physically inspected) or requires human judgment beyond a provable predicate.

KNOWN CASES already catalogued (for novelty):
- Renting an apartment — landlord wants proof of stable address & no criminal record | predicate: "Registered resident of Taiwan" + "clean criminal record" (yes/no)
- Age-gated online purchase (alcohol, e-cig, lottery) | predicate: "Age ≥ 20" (Taiwan adult age)
- Applying for a personal loan — bank needs income threshold check | predicate: "Annual income ≥ NT$X" and "debt-to-income ≤ Y%"
- Opening a brokerage/crypto exchange account (Sybil / one-person-one-account check) | predicate: "Unique real person, not already registered" (nullifier)
- Applying for low-income household subsidy | predicate: "Household income below the county's low-income threshold"
- Disabled parking permit — joint application by applicant + family member | predicate: "Holds valid disability certificate" + "relationship to vehicle owner"
- Job application requiring proof of degree | predicate: "Holds a bachelor's degree or higher from an accredited institution"
- Scholarship or tuition-waiver application | predicate: "Household income under threshold" + "currently enrolled"
- Filing annual individual income tax return | predicate: Full computation (not a simple predicate — the verifier is the issuer itself)
- Verifying professional license before contract work (e.g. engineer, nurse, real-estate agent) | predicate: "Holds a valid, unexpired license #X category issued by the competent authority"
- Long-term care subsidy application for an elderly parent | predicate: "Legal guardian/dependent relationship" + "care-level assessment result"
- Enrolling a newborn in childcare subsidy program | predicate: "Parent of a registered child under age N" + "household income under threshold"
- Utility bill subsidy / rebate for low-income households | predicate: "Registered address matches subsidized household roll"
- Car rental — proving valid driver's license without exposing home address on the card | predicate: "Holds a valid driver's license, class X, not suspended"
- Peer-to-peer marketplace seller verification (proving "real business, not a scam account") | predicate: "Registered business entity in good standing" (yes/no)

Fields per idea:
- review_id (copy)
- reasons: object with one short sentence for each of: rubric, validity, coherence, novelty, provenance, retention_law, linkability, issuer_unwilling, no_wallet
- rubric_score: 1-5 per the rubric
- validity: 1-5. Is the moment real in Taiwan, is the stated predicate really sufficient for the verifier's decision, could the named issuer plausibly sign it?
- coherence: 1-5. Do the parts of the idea fit together?
- novelty: 1-5. 1 = rewording of a known case above, 3 = new issuer or predicate on a familiar moment, 5 = a moment nobody on the known list touches.
- provenance_faithful: "yes" / "no" / "NA". "NA" if claimed_borrowings is empty. "no" if the claimed borrowing is decorative, i.e. the idea would read the same without it.
- kill_tests: object with keys retention_law, linkability, issuer_unwilling, no_wallet, each "fails" (this blocks or removes the benefit), "holds", or "unknown". Say "unknown" rather than guessing about Taiwanese law; do not invent statute numbers.

Return ONLY the JSON list in the output file. Reply DONE.