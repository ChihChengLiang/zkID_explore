You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan (digital wallet, government and private issuers). Work alone; do not read any file in this repository other than what is named here, and do not look at other agents' output.

TASK CELL
Attribute source (who could sign the claim): government
Predicate type: non-membership
Situation: A government authority can sign that a person does NOT appear on a particular list or register; a verifier wants only that absence.

INSPIRATION MATERIAL (real excerpts from other settings; use any that help, ignore any that don't):
- id: an-a-nist-dp
  situation: A releaser must answer queries about a dataset so that an observer learns almost nothing about whether any one individual contributed, and the leak must be expressed as a bound that can be checked.
  original setting: Publishing statistics about a dataset can reveal whether a particular person's record is in it, and the publisher has no quantified measure of how much that leaks.
  mechanism: Differential privacy, a randomised release mechanism with a quantified privacy-loss parameter; NIST notes that the guarantee depends on how the framework is realised in practice and lists privacy hazards that can break it. (outcome: partial)
  evidence: "This publication describes differential privacy — a mathematical framework that quantifies privacy loss to entities when their data appears in a dataset."
- id: an-b-witness-protection
  situation: A protected person must be able to show a new identity without revealing the old one, but the program holder keeps a discretionary exception that lets it disclose the true identity to law enforcement or by court order.
  original setting: The Attorney General may disclose or refuse to disclose the identity or location of a relocated or protected witness, weighing danger to the person against the public benefit.
  mechanism: Discretionary non-disclosure of identity and location, with a mandatory disclosure exception to State or local law enforcement on request or by court order when the person is under investigation or charged with a serious offense. (outcome: partial)
  evidence: "disclose or refuse to disclose the identity or location of the person relocated or protected"
- id: tw-pdpa-art11-3-deletion-exception
  situation: A party that has collected a person's data must delete it once the reason for holding it ends, but an open-ended exception lets it keep the data whenever it says it still needs it for its own duties.
  original setting: 個資法第11條第3項：特定目的消失或期限屆滿時應刪除，但因執行職務或業務所必須或經書面同意者不在此限。
  mechanism: Statutory deletion-on-purpose-lapse duty with exceptions for lawful duties or written consent; no technical erasure mechanism specified. (outcome: partial)
  evidence: "個人資料蒐集之特定目的消失或期限屆滿時，應主動或依當事人之請求，刪除、停止處理或利用該個人資料。但因執行職務或業務所必須或經當事人書面同意者，不在此限。"
- id: an-a-tor-onion
  situation: A route must be relayed through intermediaries so that no single intermediary holds both the origin identity and the final destination, while the traffic still reaches the endpoint.
  original setting: A user's network path reveals both who they are and which destination they contact, because the first hop that sees their address also sees their traffic in full.
  mechanism: Onion routing, where the message is wrapped in one encryption layer per relay, and each relay peels only its own layer and passes the rest to the next hop. (outcome: partial)
  evidence: "Each intermediary generally knows only the immediately preceding and following nodes, limiting what any single relay can learn about the route."
- id: tw-telco-online-id-check-fraud-2021
  situation: A provider must verify that a new applicant is the named person, but its check uses identifiers that are easy to copy, so a stolen identity passes and the real person bears the consequences.
  original setting: 詐騙集團以竊取的身分證資料在電信線上平台申辦門號，電信業者僅審查身分證號與換發日期即通過認證，造成上百人受害。
  mechanism: None; online verification only checked ID number and issue date. (outcome: fails)
  evidence: "僅審查身分證號與換發日期即通過認證"
- id: an-b-ala-library-records
  situation: A service provider must keep a record of who used what without that record becoming a readable log of a person's interests, but the duty is a recommended policy that depends on each institution adopting it and on courts or subpoenas being resisted.
  original setting: Libraries should adopt a policy that treats circulation records and other records identifying library users as confidential, and resist legal demands for them absent a proper showing of good cause.
  mechanism: Institutional confidentiality policy plus procedures for handling subpoenas and law-enforcement requests; no technical minimization of records is specified. (outcome: partial)
  evidence: "Formally adopt a policy that specifically recognizes its circulation records and other records identifying the names of library users to be confidential."

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan where a verifier today collects far more than it needs, and where a government-signed non-membership proof would be enough. Prefer moments that are specific and not the first thing anyone would think of (avoid generic age checks, loan income checks, and diploma verification unless you can make them genuinely specific). Be honest: if a moment is weak because of law or practice, still say so in why_zk rather than hiding it.

For each idea fill inspired_by with the seed ids that actually shaped it and, for each, one sentence naming exactly what you borrowed. Use an empty list only if you truly used none.

Write the three ideas as a YAML list to ideas/gov-nonmember__C.yaml (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys per item: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (list of {seed_id, borrowed_aspect}). Use only the Write tool for that one file. Reply with the single word DONE.
