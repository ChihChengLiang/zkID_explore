You are an independent, sceptical reviewer of proposed zero-knowledge / selective-disclosure use cases for Taiwan, using contextual integrity (a flow of information is appropriate when it matches the norms of its context). Read the input JSON file named in your task (8 ideas) and this prompt; read no other repository file. Write a JSON list (same order) to the output path named in your task. Write the short reasons FIRST, then the labels.

KNOWN cases already catalogued (for novelty): a landlord checking residency and criminal record; age-gated online purchase; personal-loan income check; brokerage KYC one-account check; low-income subsidy application; disabled parking permit; degree proof for a job; scholarship application; professional licence check; long-term-care subsidy; childcare subsidy; utility subsidy; car-rental driving licence; marketplace seller registration.

Transmission principles (how the verifier collects TODAY):
- required_by_law: a statute or regulator obliges the verifier to collect (and often keep) it (KYC/AML, tenancy, licensing)
- consented_for_benefit: the person hands it over voluntarily to receive a benefit or service (discount, subsidy, access)
- commercial_convenience: the verifier collects it because it is easy or helps its business (marketing, fraud screening, habit), with no legal duty
- safety_security: collected to protect people or premises (access control, child safety, fraud/abuse prevention)
- public_record: the fact is already in a public register or published list
- other: none of the above fit

Per idea produce:
- review_id (copy)
- context_purpose: one sentence, the verifier's legitimate purpose in its own context
- norm_violation_today: object {"violated": "yes"|"no"|"unclear", "parameter": "recipient"|"information_type"|"transmission_principle"|"retention"|"none", "reason": one sentence}. "no" when the verifier is entitled to the whole record (e.g. it is the issuer).
- purpose_sufficiency: object {"rating": "sufficient"|"partly"|"insufficient", "lost": what the minimal flow cannot do that the full document could}
- transmission_check: object {"principle_today": one of the labels above, "permits_minimal_flow": "permits"|"blocks"|"unclear", "reason": one sentence}. "blocks" if a law or regulator, as you know it, requires the full document; say "unclear" rather than guess Taiwanese law and never invent statute numbers.
- aggregation: "low"|"medium"|"high"|"unknown": would repeated presentations let anyone combine facts across contexts or build a log?
- adoption: object {"issuer_willing": "yes"|"no"|"unknown", "verifier_can_check": "yes"|"no"|"unknown"}
- rubric_score (1-5) and novelty (1-5) exactly as v1: rubric 5 strong fit (simple predicate, existing trusted issuer, frequent, verifier over-collects), 4 good, 3 needs design, 2 weak (legal duty to keep full data, or rare), 1 poor. Novelty 1 = rewording of a known case, 3 = new issuer or predicate on a familiar moment, 5 = a moment nobody on the known list touches.
- provenance_faithful: "yes"|"no"|"NA" ("NA" if claimed_borrowings is empty, "no" if the borrowing is decorative)

Return ONLY the JSON list. Reply DONE.