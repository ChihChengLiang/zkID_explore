You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan (digital wallet, government and private issuers). Work alone; do not read any file in this repository other than what is named here, and do not look at other agents' output.

TASK CELL
Attribute source (who could sign the claim): utility
Predicate type: membership
Situation: A utility can sign that an account belongs to a set (a subsidised roll); a verifier wants set membership without learning the address or usage.

INSPIRATION MATERIAL (real excerpts from other settings; use any that help, ignore any that don't):
- id: tw-securities-foreign-agent-id-copy
  situation: A foreign investor must prove that its local agent is a real, identified person, and the agent hands over a full copy of an ID card, with no alternative verification stated.
  original setting: 境外華僑及外國人經國內代理人辦理證券開戶時，代理人須檢附國民身分證或居留證影本。
  mechanism: None stated; full ID copy required with no less-intrusive alternative given. (outcome: fails)
  evidence: "國內代理人或代表人之國民身分證、居留證影本或公司登記後之證明文件影本"
- id: rd-cnpd-lu-tourist-inspect-not-copy
  situation: A host must confirm a visitor's identity and eligibility, but the usual practice is to keep a copy of the whole identity document; the regulator says looking at it is enough.
  original setting: Tourist accommodation operators in Luxembourg ask to see guests' identity documents and some make copies; the regulator reminds them that inspection is allowed and copying is not.
  mechanism: Visual inspection of the identity document with no copy taken; the statutory duty is met by checking, not retaining. (outcome: works)
  evidence: "they may inspect their customers’ identity documents but must not under any circumstances make a copy of them"
- id: an-b-witness-protection
  situation: A protected person must be able to show a new identity without revealing the old one, but the program holder keeps a discretionary exception that lets it disclose the true identity to law enforcement or by court order.
  original setting: The Attorney General may disclose or refuse to disclose the identity or location of a relocated or protected witness, weighing danger to the person against the public benefit.
  mechanism: Discretionary non-disclosure of identity and location, with a mandatory disclosure exception to State or local law enforcement on request or by court order when the person is under investigation or charged with a serious offense. (outcome: partial)
  evidence: "disclose or refuse to disclose the identity or location of the person relocated or protected"
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
- id: an-b-ala-library-records
  situation: A service provider must keep a record of who used what without that record becoming a readable log of a person's interests, but the duty is a recommended policy that depends on each institution adopting it and on courts or subpoenas being resisted.
  original setting: Libraries should adopt a policy that treats circulation records and other records identifying library users as confidential, and resist legal demands for them absent a proper showing of good cause.
  mechanism: Institutional confidentiality policy plus procedures for handling subpoenas and law-enforcement requests; no technical minimization of records is specified. (outcome: partial)
  evidence: "Formally adopt a policy that specifically recognizes its circulation records and other records identifying the names of library users to be confidential."

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan where a verifier today collects far more than it needs, and where a utility-signed membership proof would be enough. Prefer moments that are specific and not the first thing anyone would think of (avoid generic age checks, loan income checks, and diploma verification unless you can make them genuinely specific). Be honest: if a moment is weak because of law or practice, still say so in why_zk rather than hiding it.

For each idea fill inspired_by with the seed ids that actually shaped it and, for each, one sentence naming exactly what you borrowed. Use an empty list only if you truly used none.

Write the three ideas as a YAML list to ideas/utility-member__D.yaml (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys per item: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (list of {seed_id, borrowed_aspect}). Use only the Write tool for that one file. Reply with the single word DONE.
