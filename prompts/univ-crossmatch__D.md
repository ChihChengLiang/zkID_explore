You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan (digital wallet, government and private issuers). Work alone; do not read any file in this repository other than what is named here, and do not look at other agents' output.

TASK CELL
Attribute source (who could sign the claim): university
Predicate type: cross-source-match
Situation: A university can sign a claim that must be shown to refer to the same person as a claim from a second, unrelated issuer, without revealing the person's identifier to the verifier.

INSPIRATION MATERIAL (real excerpts from other settings; use any that help, ignore any that don't):
- id: rd-aepd-hotel-no-id-copy
  situation: A registrant must prove a small set of facts to a host, but the host asks for a full copy of the identity document, which carries many extra fields the rule never needed.
  original setting: Hotels must register guests' identity data under the hospitality registration decree; the regulator says that duty does not authorise photocopying the whole ID document.
  mechanism: Inspect the identity document in person and record only the fields the registration rule requires; no copy retained. (outcome: partial)
  evidence: "esto vulneraría el principio de minimización de datos y supondría un tratamiento excesivo"
- id: an-b-witness-protection
  situation: A protected person must be able to show a new identity without revealing the old one, but the program holder keeps a discretionary exception that lets it disclose the true identity to law enforcement or by court order.
  original setting: The Attorney General may disclose or refuse to disclose the identity or location of a relocated or protected witness, weighing danger to the person against the public benefit.
  mechanism: Discretionary non-disclosure of identity and location, with a mandatory disclosure exception to State or local law enforcement on request or by court order when the person is under investigation or charged with a serious offense. (outcome: partial)
  evidence: "disclose or refuse to disclose the identity or location of the person relocated or protected"
- id: an-b-va-id-scanning
  situation: A venue must confirm that a person is over a threshold age from an identity document, but scanning captures the whole card, so the rule caps what is kept to a few fields and bans secondary use, while the holder still sees everything on the card at the moment of the scan.
  original setting: A merchant may scan the machine-readable zone of a driver's license for an age check, but the scan data it may collect and keep is limited to name, address, date of birth and license number, and may not be disseminated for marketing.
  mechanism: Statutory field-limit and retention ban on scan data, with a prohibition on sale or marketing dissemination; no proof-of-age mechanism that avoids reading the document. (outcome: partial)
  evidence: "Information collected by scanning an individual's driver's license or other document pursuant to this subdivision shall be limited to the individual's name, address, and date of birth and the number of the driver's license or other document;"
- id: an-b-hipaa-safe-harbor
  situation: A party wants to share a record set that cannot identify any person, but the test is a checklist of removable fields plus a no-actual-knowledge condition, so the holder must still judge whether leftover fields re-identify someone.
  original setting: Health information may be shared for research or trials as de-identified data only after a fixed list of identifiers of the individual and of relatives, employers or household members is removed.
  mechanism: Safe Harbor method removing 18 enumerated identifiers (with ZIP-code truncation rule and age aggregation), or an expert-determination alternative; re-identification codes allowed only if not derived from or disclosed about the individual. (outcome: works)
  evidence: "The following identifiers of the individual or of relatives, employers, or household members of the individual, are removed"
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

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan where a verifier today collects far more than it needs, and where a university-signed cross-source-match proof would be enough. Prefer moments that are specific and not the first thing anyone would think of (avoid generic age checks, loan income checks, and diploma verification unless you can make them genuinely specific). Be honest: if a moment is weak because of law or practice, still say so in why_zk rather than hiding it.

For each idea fill inspired_by with the seed ids that actually shaped it and, for each, one sentence naming exactly what you borrowed. Use an empty list only if you truly used none.

Write the three ideas as a YAML list to ideas/univ-crossmatch__D.yaml (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys per item: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (list of {seed_id, borrowed_aspect}). Use only the Write tool for that one file. Reply with the single word DONE.
