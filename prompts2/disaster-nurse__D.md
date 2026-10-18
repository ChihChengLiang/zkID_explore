You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: disaster-shelter volunteer coordination
The verifier needs to establish: holds a current nursing licence in good standing
Kind of claim (predicate type): freshness
Today the verifier collects the information under this condition: safety security: collected to protect people or premises (access control, child safety, fraud/abuse prevention)
The fact originates in: healthcare; it is used in: civic_community
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: tw-bank-deposit-dual-id-check
  situation: A bank must verify who a person is before opening an account, which means examining identity documents, but the cited rule does not say whether copies are kept or for how long.
  original setting: 金管會函釋：金融機構受理開立存款帳戶，應實施雙重身分證明文件查核及確認客戶身分之措施，以防制金融犯罪。
  mechanism: Dual identity-document inspection at account opening; retention and copy handling not specified in the cited text. (outcome: partial)
  evidence: "應實施雙重身分證明文件查核及確認客戶身分"
- id: tw-platform-gym-id-card-copies-interp
  situation: A service provider signing up a customer must check identity and payment, but it asks for full front-and-back copies of identity and card documents, and the regulator leaves whether that exceeds the purpose to case-by-case fact-finding.
  original setting: 健身中心於簽立會員契約時要求消費者提供身分證正反面影本及信用卡正反面影本，是否逾越特定目的必要範圍。
  mechanism: None stated; the letter says less-intrusive alternatives must be considered but names none. (outcome: unknown)
  evidence: "健身中心業者於簽立會員契約時，要求消費者提供身分證正反面影本"
- id: an-a-samesite-cookies
  situation: A stored credential should be presented only to the party that issued it in the current context, but the browser sends it on any request the context triggers, so an unrelated observer can match the holder across contexts.
  original setting: A cookie is attached to requests made from third-party sites embedded in a page, which lets those third parties recognise the same browser across unrelated websites.
  mechanism: The SameSite cookie attribute, which limits the cookie to same-site requests (Strict, Lax, or None); the IETF draft describes it as a per-cookie setting, and cross-site behaviour depends on the chosen value. (outcome: partial)
  evidence: "If the "SameSite" attribute's value is "Strict", the cookie will only be sent along with "same-site" requests."
- id: rd-twdiw-field-selection-consent
  situation: A user must prove one eligibility fact to a counter, while the credential holds a whole identity record and the user chooses fields at presentation time with no field-level guarantee.
  original setting: Taiwan's Digital Identity Wallet lets users pick which fields to disclose in each scenario, but the official page does not say which fields an age check releases.
  mechanism: Per-scenario field selection after scanning a QR code, confirmed by biometric check, in the TW DIW sandbox. (outcome: partial)
  evidence: "Users can choose what information they consent to share in different scenarios"
- id: tw-gov-household-register-proxy-copy-discretion
  situation: A government office that holds a record may ask a proxy's requester for a copy of the principal's identity document, and the scope of what it may collect is left to the office's discretion.
  original setting: 內政部函釋：戶政事務所受理委託申請戶籍謄本時，得為蒐集委託人身分證明文件影本，並可斟酌裁量所需附繳證明。
  mechanism: None stated; collection of document copies left to agency discretion under PDPA and administrative procedure rules. (outcome: fails)
  evidence: "即得為蒐集、處理申請人之個人資料（例如繳 驗委託人身分證明文件影本）"
- id: an-b-attorney-client
  situation: A party must consult an advisor about a sensitive matter without the advisor, or anyone else, learning or revealing more than the matter requires, but the protection breaks as soon as an outsider is in the room unless the outsider is essential to the relationship.
  original setting: Attorney-client privilege protects confidential communications between a lawyer and client about seeking legal advice, but the confidentiality is compromised if a third party is present.
  mechanism: Evidentiary privilege over communications, lost by third-party presence except essential agents such as interpreters; no technical mechanism. (outcome: partial)
  evidence: "Attorney-client privilege protects confidential communications between a lawyer and their client that relate to the client's seeking of legal advice or services."

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/disaster-nurse__D.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
