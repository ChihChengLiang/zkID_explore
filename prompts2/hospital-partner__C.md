You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: hospital ward allowing visits or consenting to treatment
The verifier needs to establish: is the patient's spouse, partner or named proxy
Kind of claim (predicate type): membership
Today the verifier collects the information under this condition: safety security: collected to protect people or premises (access control, child safety, fraud/abuse prevention)
The fact originates in: family_social; it is used in: healthcare
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: tw-securities-foreign-agent-id-copy
  situation: A foreign investor must prove that its local agent is a real, identified person, and the agent hands over a full copy of an ID card, with no alternative verification stated.
  original setting: 境外華僑及外國人經國內代理人辦理證券開戶時，代理人須檢附國民身分證或居留證影本。
  mechanism: None stated; full ID copy required with no less-intrusive alternative given. (outcome: fails)
  evidence: "國內代理人或代表人之國民身分證、居留證影本或公司登記後之證明文件影本"
- id: an-a-samesite-cookies
  situation: A stored credential should be presented only to the party that issued it in the current context, but the browser sends it on any request the context triggers, so an unrelated observer can match the holder across contexts.
  original setting: A cookie is attached to requests made from third-party sites embedded in a page, which lets those third parties recognise the same browser across unrelated websites.
  mechanism: The SameSite cookie attribute, which limits the cookie to same-site requests (Strict, Lax, or None); the IETF draft describes it as a per-cookie setting, and cross-site behaviour depends on the chosen value. (outcome: partial)
  evidence: "If the "SameSite" attribute's value is "Strict", the cookie will only be sent along with "same-site" requests."
- id: an-b-census-title13
  situation: An agency holding individual responses must release aggregate results, and the legal duty bars any output from which a particular respondent can be singled out, while the holder's staff can still see the raw records.
  original setting: Census data may be used only for statistical purposes, and no publication may allow data furnished by a particular individual or establishment to be identified.
  mechanism: Statutory use limitation and publication prohibition enforced by sworn-oath duties and penalties; statistical disclosure limitation (for example differential privacy in later census products) is a technical layer not specified in the statute. (outcome: partial)
  evidence: "make any publication whereby the data furnished by any particular establishment or individual under this title can be identified"
- id: tw-pdpa-art5-purpose-limit
  situation: A rule requires anyone collecting personal data to stay within the necessary scope of its stated purpose, but it gives no concrete way to show what was necessary, so the collector decides what counts as necessary.
  original setting: 個資法第5條要求蒐集、處理或利用個人資料不得逾越特定目的之必要範圍，並應與蒐集目的具正當合理之關聯。
  mechanism: Legal purpose-limitation and proportionality principle; no technical mechanism specified. (outcome: partial)
  evidence: "個人資料之蒐集、處理或利用，應尊重當事人之權益，依誠實及信用方法為之，不得逾越特定目的之必要範圍，並應與蒐集之目的具有正當合理之關聯。"
- id: rd-swiss-eid-necessary-data-only
  situation: A business needs one attribute to proceed, but the credential is issued as a whole, so the holder must rely on the wallet to release only the needed attribute.
  original setting: The Swiss e-ID is described as sharing only the data a transaction needs; the technical overview says selective disclosure and batch issuance enable this.
  mechanism: SD-JWT VC selective disclosure with OpenID4VP presentation and status-list validity check. (outcome: partial)
  evidence: "The Swiss e-ID introduces a new approach to digital identity: only the necessary data is shared."
- id: an-b-hipaa-min-necessary
  situation: A holder of sensitive records must release only the subset that serves a stated purpose, but the rule leaves it to the holder to judge what is minimal and gives no mechanism that proves the released subset was minimal.
  original setting: Covered entities and business associates must limit protected health information to what a given use, disclosure or request actually needs.
  mechanism: Purpose-based minimum-necessary rule with reasonable-efforts standard, role-based access and reasonable reliance on requester representations (45 CFR 164.514(d)); no cryptographic or proof-based check. (outcome: partial)
  evidence: "must make reasonable efforts to limit protected health information to the minimum necessary to accomplish the intended purpose of the use, disclosure, or request."

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/hospital-partner__C.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
