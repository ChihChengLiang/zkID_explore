You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan (digital wallet, government and private issuers). Work alone; do not read any file in this repository other than what is named here, and do not look at other agents' output.

TASK CELL
Attribute source (who could sign the claim): employer
Predicate type: freshness
Situation: An employer can sign that a status is true as of now and can revoke it; a verifier needs it to be current without learning who the person is beyond that.

INSPIRATION MATERIAL (real excerpts from other settings; use any that help, ignore any that don't):
- id: an-b-va-id-scanning
  situation: A venue must confirm that a person is over a threshold age from an identity document, but scanning captures the whole card, so the rule caps what is kept to a few fields and bans secondary use, while the holder still sees everything on the card at the moment of the scan.
  original setting: A merchant may scan the machine-readable zone of a driver's license for an age check, but the scan data it may collect and keep is limited to name, address, date of birth and license number, and may not be disseminated for marketing.
  mechanism: Statutory field-limit and retention ban on scan data, with a prohibition on sale or marketing dissemination; no proof-of-age mechanism that avoids reading the document. (outcome: partial)
  evidence: "Information collected by scanning an individual's driver's license or other document pursuant to this subdivision shall be limited to the individual's name, address, and date of birth and the number of the driver's license or other document;"
- id: an-b-census-title13
  situation: An agency holding individual responses must release aggregate results, and the legal duty bars any output from which a particular respondent can be singled out, while the holder's staff can still see the raw records.
  original setting: Census data may be used only for statistical purposes, and no publication may allow data furnished by a particular individual or establishment to be identified.
  mechanism: Statutory use limitation and publication prohibition enforced by sworn-oath duties and penalties; statistical disclosure limitation (for example differential privacy in later census products) is a technical layer not specified in the statute. (outcome: partial)
  evidence: "make any publication whereby the data furnished by any particular establishment or individual under this title can be identified"
- id: tw-platform-google-id-upload-complaint
  situation: A service needs to confirm a subscriber's payment, but it demands an identity document and address proof, and threatens suspension if the user refuses, without stating the purpose or necessity.
  original setting: 訂閱用戶付款正常卻被要求上傳身分證與含住址帳單，否則帳戶將停權；消基會認為已過度蒐集個資。
  mechanism: None; the complaint notes no stated purpose or less-intrusive alternative was offered. (outcome: fails)
  evidence: "若僅涉及訂閱付款驗證，要求提供身分證與住址資料，顯已超出合理必要範圍，恐構成過度蒐集。"
- id: an-b-attorney-client
  situation: A party must consult an advisor about a sensitive matter without the advisor, or anyone else, learning or revealing more than the matter requires, but the protection breaks as soon as an outsider is in the room unless the outsider is essential to the relationship.
  original setting: Attorney-client privilege protects confidential communications between a lawyer and client about seeking legal advice, but the confidentiality is compromised if a third party is present.
  mechanism: Evidentiary privilege over communications, lost by third-party presence except essential agents such as interpreters; no technical mechanism. (outcome: partial)
  evidence: "Attorney-client privilege protects confidential communications between a lawyer and their client that relate to the client's seeking of legal advice or services."
- id: tw-telco-online-id-check-fraud-2021
  situation: A provider must verify that a new applicant is the named person, but its check uses identifiers that are easy to copy, so a stolen identity passes and the real person bears the consequences.
  original setting: 詐騙集團以竊取的身分證資料在電信線上平台申辦門號，電信業者僅審查身分證號與換發日期即通過認證，造成上百人受害。
  mechanism: None; online verification only checked ID number and issue date. (outcome: fails)
  evidence: "僅審查身分證號與換發日期即通過認證"
- id: tw-platform-gym-id-card-copies-interp
  situation: A service provider signing up a customer must check identity and payment, but it asks for full front-and-back copies of identity and card documents, and the regulator leaves whether that exceeds the purpose to case-by-case fact-finding.
  original setting: 健身中心於簽立會員契約時要求消費者提供身分證正反面影本及信用卡正反面影本，是否逾越特定目的必要範圍。
  mechanism: None stated; the letter says less-intrusive alternatives must be considered but names none. (outcome: unknown)
  evidence: "健身中心業者於簽立會員契約時，要求消費者提供身分證正反面影本"

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan where a verifier today collects far more than it needs, and where a employer-signed freshness proof would be enough. Prefer moments that are specific and not the first thing anyone would think of (avoid generic age checks, loan income checks, and diploma verification unless you can make them genuinely specific). Be honest: if a moment is weak because of law or practice, still say so in why_zk rather than hiding it.

For each idea fill inspired_by with the seed ids that actually shaped it and, for each, one sentence naming exactly what you borrowed. Use an empty list only if you truly used none.

Write the three ideas as a YAML list to ideas/employer-fresh__C.yaml (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys per item: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (list of {seed_id, borrowed_aspect}). Use only the Write tool for that one file. Reply with the single word DONE.
