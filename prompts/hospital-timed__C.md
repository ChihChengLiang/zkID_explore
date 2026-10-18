You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan (digital wallet, government and private issuers). Work alone; do not read any file in this repository other than what is named here, and do not look at other agents' output.

TASK CELL
Attribute source (who could sign the claim): hospital
Predicate type: time-bounded
Situation: A hospital can sign a status that is only meaningful within a time window; a verifier needs it valid for that window without learning the clinical detail.

INSPIRATION MATERIAL (real excerpts from other settings; use any that help, ignore any that don't):
- id: rd-swiss-eid-necessary-data-only
  situation: A business needs one attribute to proceed, but the credential is issued as a whole, so the holder must rely on the wallet to release only the needed attribute.
  original setting: The Swiss e-ID is described as sharing only the data a transaction needs; the technical overview says selective disclosure and batch issuance enable this.
  mechanism: SD-JWT VC selective disclosure with OpenID4VP presentation and status-list validity check. (outcome: partial)
  evidence: "The Swiss e-ID introduces a new approach to digital identity: only the necessary data is shared."
- id: tw-telco-online-id-check-fraud-2021
  situation: A provider must verify that a new applicant is the named person, but its check uses identifiers that are easy to copy, so a stolen identity passes and the real person bears the consequences.
  original setting: 詐騙集團以竊取的身分證資料在電信線上平台申辦門號，電信業者僅審查身分證號與換發日期即通過認證，造成上百人受害。
  mechanism: None; online verification only checked ID number and issue date. (outcome: fails)
  evidence: "僅審查身分證號與換發日期即通過認證"
- id: an-a-nist-dp
  situation: A releaser must answer queries about a dataset so that an observer learns almost nothing about whether any one individual contributed, and the leak must be expressed as a bound that can be checked.
  original setting: Publishing statistics about a dataset can reveal whether a particular person's record is in it, and the publisher has no quantified measure of how much that leaks.
  mechanism: Differential privacy, a randomised release mechanism with a quantified privacy-loss parameter; NIST notes that the guarantee depends on how the framework is realised in practice and lists privacy hazards that can break it. (outcome: partial)
  evidence: "This publication describes differential privacy — a mathematical framework that quantifies privacy loss to entities when their data appears in a dataset."
- id: an-b-jury-selection
  situation: Someone must be drawn from a pool and seated for a task without the wider public learning who they are, but the default rule can flip to full publication of the identities of everyone selected, with confidentiality only as a judge-level exception.
  original setting: A federal district plan may make juror names public, but may also let a judge keep those names confidential where the interests of justice require.
  mechanism: Judge-discretionary confidentiality of juror names under a court's jury selection plan; no technical mechanism specified. (outcome: partial)
  evidence: "If the plan permits these names to be made public, it may nevertheless permit the chief judge of the district court"
- id: an-b-witness-protection
  situation: A protected person must be able to show a new identity without revealing the old one, but the program holder keeps a discretionary exception that lets it disclose the true identity to law enforcement or by court order.
  original setting: The Attorney General may disclose or refuse to disclose the identity or location of a relocated or protected witness, weighing danger to the person against the public benefit.
  mechanism: Discretionary non-disclosure of identity and location, with a mandatory disclosure exception to State or local law enforcement on request or by court order when the person is under investigation or charged with a serious offense. (outcome: partial)
  evidence: "disclose or refuse to disclose the identity or location of the person relocated or protected"
- id: tw-gov-id-number-reissue-misuse-2025
  situation: Once the number that identifies a person leaks, reissuing the physical card does not stop someone presenting the same number, so verifiers that check the number and a photo can be fooled.
  original setting: 身分證遺失並掛失換發新證後，同一身分證號碼仍被他人持續冒用，當事人遭罰單與討債困擾。
  mechanism: None; reissuing the card does not change the number. (outcome: fails)
  evidence: "盡管換發新的身分證，但身分證號碼不會改變"

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan where a verifier today collects far more than it needs, and where a hospital-signed time-bounded proof would be enough. Prefer moments that are specific and not the first thing anyone would think of (avoid generic age checks, loan income checks, and diploma verification unless you can make them genuinely specific). Be honest: if a moment is weak because of law or practice, still say so in why_zk rather than hiding it.

For each idea fill inspired_by with the seed ids that actually shaped it and, for each, one sentence naming exactly what you borrowed. Use an empty list only if you truly used none.

Write the three ideas as a YAML list to ideas/hospital-timed__C.yaml (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys per item: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (list of {seed_id, borrowed_aspect}). Use only the Write tool for that one file. Reply with the single word DONE.
