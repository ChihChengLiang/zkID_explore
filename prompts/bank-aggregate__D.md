You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan (digital wallet, government and private issuers). Work alone; do not read any file in this repository other than what is named here, and do not look at other agents' output.

TASK CELL
Attribute source (who could sign the claim): bank
Predicate type: aggregate
Situation: A bank can sign a statistic computed over many of a person's transactions or accounts; a verifier wants only the aggregate, not the underlying records.

INSPIRATION MATERIAL (real excerpts from other settings; use any that help, ignore any that don't):
- id: an-b-hipaa-min-necessary
  situation: A holder of sensitive records must release only the subset that serves a stated purpose, but the rule leaves it to the holder to judge what is minimal and gives no mechanism that proves the released subset was minimal.
  original setting: Covered entities and business associates must limit protected health information to what a given use, disclosure or request actually needs.
  mechanism: Purpose-based minimum-necessary rule with reasonable-efforts standard, role-based access and reasonable reliance on requester representations (45 CFR 164.514(d)); no cryptographic or proof-based check. (outcome: partial)
  evidence: "must make reasonable efforts to limit protected health information to the minimum necessary to accomplish the intended purpose of the use, disclosure, or request."
- id: an-a-samesite-cookies
  situation: A stored credential should be presented only to the party that issued it in the current context, but the browser sends it on any request the context triggers, so an unrelated observer can match the holder across contexts.
  original setting: A cookie is attached to requests made from third-party sites embedded in a page, which lets those third parties recognise the same browser across unrelated websites.
  mechanism: The SameSite cookie attribute, which limits the cookie to same-site requests (Strict, Lax, or None); the IETF draft describes it as a per-cookie setting, and cross-site behaviour depends on the chosen value. (outcome: partial)
  evidence: "If the "SameSite" attribute's value is "Strict", the cookie will only be sent along with "same-site" requests."
- id: rd-aepd-hotel-no-id-copy
  situation: A registrant must prove a small set of facts to a host, but the host asks for a full copy of the identity document, which carries many extra fields the rule never needed.
  original setting: Hotels must register guests' identity data under the hospitality registration decree; the regulator says that duty does not authorise photocopying the whole ID document.
  mechanism: Inspect the identity document in person and record only the fields the registration rule requires; no copy retained. (outcome: partial)
  evidence: "esto vulneraría el principio de minimización de datos y supondría un tratamiento excesivo"
- id: rd-apple-wallet-age-request-categories
  situation: A verifier wants a single over-threshold fact, but the request category bundles the issuing authority and a face photo with it, so the verifier can receive more than the age claim.
  original setting: Apple's Verify with Wallet API lists the data an app can request for age checks, and the age category also includes the issuing authority and the ID photo.
  mechanism: Age Over N Flag as a separate requestable value under an entitlement-gated API; no shared name or address. (outcome: partial)
  evidence: "Age verification data: Age Over N Flag Age in Years Issuing Authority ID Photo"
- id: tw-pdpa-art11-3-deletion-exception
  situation: A party that has collected a person's data must delete it once the reason for holding it ends, but an open-ended exception lets it keep the data whenever it says it still needs it for its own duties.
  original setting: 個資法第11條第3項：特定目的消失或期限屆滿時應刪除，但因執行職務或業務所必須或經書面同意者不在此限。
  mechanism: Statutory deletion-on-purpose-lapse duty with exceptions for lawful duties or written consent; no technical erasure mechanism specified. (outcome: partial)
  evidence: "個人資料蒐集之特定目的消失或期限屆滿時，應主動或依當事人之請求，刪除、停止處理或利用該個人資料。但因執行職務或業務所必須或經當事人書面同意者，不在此限。"
- id: tw-platform-google-id-upload-complaint
  situation: A service needs to confirm a subscriber's payment, but it demands an identity document and address proof, and threatens suspension if the user refuses, without stating the purpose or necessity.
  original setting: 訂閱用戶付款正常卻被要求上傳身分證與含住址帳單，否則帳戶將停權；消基會認為已過度蒐集個資。
  mechanism: None; the complaint notes no stated purpose or less-intrusive alternative was offered. (outcome: fails)
  evidence: "若僅涉及訂閱付款驗證，要求提供身分證與住址資料，顯已超出合理必要範圍，恐構成過度蒐集。"

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan where a verifier today collects far more than it needs, and where a bank-signed aggregate proof would be enough. Prefer moments that are specific and not the first thing anyone would think of (avoid generic age checks, loan income checks, and diploma verification unless you can make them genuinely specific). Be honest: if a moment is weak because of law or practice, still say so in why_zk rather than hiding it.

For each idea fill inspired_by with the seed ids that actually shaped it and, for each, one sentence naming exactly what you borrowed. Use an empty list only if you truly used none.

Write the three ideas as a YAML list to ideas/bank-aggregate__D.yaml (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys per item: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (list of {seed_id, borrowed_aspect}). Use only the Write tool for that one file. Reply with the single word DONE.
