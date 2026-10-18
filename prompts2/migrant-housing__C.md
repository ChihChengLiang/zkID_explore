You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: dormitory or landlord renting to migrant workers (外籍移工)
The verifier needs to establish: is legally working for a sponsoring employer right now
Kind of claim (predicate type): freshness
Today the verifier collects the information under this condition: consented for benefit: the person hands it over voluntarily to receive a benefit or service (discount, subsidy, access)
The fact originates in: employment; it is used in: housing
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: tw-gov-household-register-proxy-copy-discretion
  situation: A government office that holds a record may ask a proxy's requester for a copy of the principal's identity document, and the scope of what it may collect is left to the office's discretion.
  original setting: 內政部函釋：戶政事務所受理委託申請戶籍謄本時，得為蒐集委託人身分證明文件影本，並可斟酌裁量所需附繳證明。
  mechanism: None stated; collection of document copies left to agency discretion under PDPA and administrative procedure rules. (outcome: fails)
  evidence: "即得為蒐集、處理申請人之個人資料（例如繳 驗委託人身分證明文件影本）"
- id: an-b-hipaa-min-necessary
  situation: A holder of sensitive records must release only the subset that serves a stated purpose, but the rule leaves it to the holder to judge what is minimal and gives no mechanism that proves the released subset was minimal.
  original setting: Covered entities and business associates must limit protected health information to what a given use, disclosure or request actually needs.
  mechanism: Purpose-based minimum-necessary rule with reasonable-efforts standard, role-based access and reasonable reliance on requester representations (45 CFR 164.514(d)); no cryptographic or proof-based check. (outcome: partial)
  evidence: "must make reasonable efforts to limit protected health information to the minimum necessary to accomplish the intended purpose of the use, disclosure, or request."
- id: an-b-attorney-client
  situation: A party must consult an advisor about a sensitive matter without the advisor, or anyone else, learning or revealing more than the matter requires, but the protection breaks as soon as an outsider is in the room unless the outsider is essential to the relationship.
  original setting: Attorney-client privilege protects confidential communications between a lawyer and client about seeking legal advice, but the confidentiality is compromised if a third party is present.
  mechanism: Evidentiary privilege over communications, lost by third-party presence except essential agents such as interpreters; no technical mechanism. (outcome: partial)
  evidence: "Attorney-client privilege protects confidential communications between a lawyer and their client that relate to the client's seeking of legal advice or services."
- id: an-b-sealed-bid-far
  situation: A party submits a value that must stay hidden from competitors until a fixed moment, while the holder of the submissions must be able to prove later that none were seen early and must handle identifying wrappers without exposing the content.
  original setting: Federal sealed bids must stay unopened and unviewed in a locked or restricted-access box until the scheduled opening, and envelopes may be opened only to identify them by an official designated for that purpose.
  mechanism: Physical and access-control safeguarding of sealed bids with designated-official exception for envelope identification, plus a written record of any mistaken early opening. (outcome: works)
  evidence: "the bids shall not be opened or viewed, and shall remain in a locked bid box, a safe, or in a secured, restricted-access electronic bid box."
- id: an-a-samesite-cookies
  situation: A stored credential should be presented only to the party that issued it in the current context, but the browser sends it on any request the context triggers, so an unrelated observer can match the holder across contexts.
  original setting: A cookie is attached to requests made from third-party sites embedded in a page, which lets those third parties recognise the same browser across unrelated websites.
  mechanism: The SameSite cookie attribute, which limits the cookie to same-site requests (Strict, Lax, or None); the IETF draft describes it as a per-cookie setting, and cross-site behaviour depends on the chosen value. (outcome: partial)
  evidence: "If the "SameSite" attribute's value is "Strict", the cookie will only be sent along with "same-site" requests."
- id: gdpr-data-minimisation
  situation: A rule obliges anyone requesting information to take only what the purpose needs, but gives no practical way to request less than a whole document.
  original setting: Controllers collect whole documents when a narrower field would serve the purpose.
  mechanism: Legal principle of data minimisation; no technical mechanism specified. (outcome: partial)
  evidence: "limited to what is necessary in relation to the purposes for which they are processed"

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/migrant-housing__C.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
