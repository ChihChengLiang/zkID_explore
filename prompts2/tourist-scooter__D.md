You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: e-scooter or SIM shop serving a visitor
The verifier needs to establish: has a valid entry status that has not expired
Kind of claim (predicate type): time-bounded
Today the verifier collects the information under this condition: required by law: a statute or regulator obliges the verifier to collect (and often keep) it (KYC/AML, tenancy, licensing)
The fact originates in: government_admin; it is used in: telecom_online
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: an-a-chaum-blind
  situation: A signer must certify that a holder has a valid token without seeing the token's content, and must later be unable to link the certified token back to the signing event.
  original setting: A ballot authority must sign a voter's ballot to certify it, but it must not learn how the voter voted, and the counted ballot must still be accepted as valid.
  mechanism: A blind signature, where the message is blinded with a random factor before signing, and the holder unblinds the signature so it verifies against the original message under the signer's public key. (outcome: works)
  evidence: "An unlinkable blind signature provides this guarantee, as the authority will not see the contents of any ballot it signs, and will be unable to link the blinded ballots it signs back to the un-blinded ballots it receives for counting."
- id: an-b-census-title13
  situation: An agency holding individual responses must release aggregate results, and the legal duty bars any output from which a particular respondent can be singled out, while the holder's staff can still see the raw records.
  original setting: Census data may be used only for statistical purposes, and no publication may allow data furnished by a particular individual or establishment to be identified.
  mechanism: Statutory use limitation and publication prohibition enforced by sworn-oath duties and penalties; statistical disclosure limitation (for example differential privacy in later census products) is a technical layer not specified in the statute. (outcome: partial)
  evidence: "make any publication whereby the data furnished by any particular establishment or individual under this title can be identified"
- id: tw-telco-online-id-check-fraud-2021
  situation: A provider must verify that a new applicant is the named person, but its check uses identifiers that are easy to copy, so a stolen identity passes and the real person bears the consequences.
  original setting: 詐騙集團以竊取的身分證資料在電信線上平台申辦門號，電信業者僅審查身分證號與換發日期即通過認證，造成上百人受害。
  mechanism: None; online verification only checked ID number and issue date. (outcome: fails)
  evidence: "僅審查身分證號與換發日期即通過認證"
- id: privacy-pass-unlinkable-proof
  situation: A gatekeeper only needs to know that the visitor already passed some check, but the proof it accepts doubles as a persistent identifier.
  original setting: Servers authorise clients with cookies, which let them track the same client across sessions.
  mechanism: Blind-signed tokens that attest prior authorisation and cannot be linked to the issuance interaction. (outcome: works)
  evidence: "Clients present unlinkable proofs that attest to this information."
- id: rd-apple-wallet-age-request-categories
  situation: A verifier wants a single over-threshold fact, but the request category bundles the issuing authority and a face photo with it, so the verifier can receive more than the age claim.
  original setting: Apple's Verify with Wallet API lists the data an app can request for age checks, and the age category also includes the issuing authority and the ID photo.
  mechanism: Age Over N Flag as a separate requestable value under an entitlement-gated API; no shared name or address. (outcome: partial)
  evidence: "Age verification data: Age Over N Flag Age in Years Issuing Authority ID Photo"
- id: rd-swiss-eid-necessary-data-only
  situation: A business needs one attribute to proceed, but the credential is issued as a whole, so the holder must rely on the wallet to release only the needed attribute.
  original setting: The Swiss e-ID is described as sharing only the data a transaction needs; the technical overview says selective disclosure and batch issuance enable this.
  mechanism: SD-JWT VC selective disclosure with OpenID4VP presentation and status-list validity check. (outcome: partial)
  evidence: "The Swiss e-ID introduces a new approach to digital identity: only the necessary data is shared."

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/tourist-scooter__D.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
