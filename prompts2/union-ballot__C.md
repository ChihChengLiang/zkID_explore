You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: union strike or bargaining ballot
The verifier needs to establish: is a dues-paying member and votes once, without the employer learning who voted (union membership: special category)
Kind of claim (predicate type): membership
Today the verifier collects the information under this condition: required by law: a statute or regulator obliges the verifier to collect (and often keep) it (KYC/AML, tenancy, licensing)
The fact originates in: employment; it is used in: civic_community
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: an-b-jury-selection
  situation: Someone must be drawn from a pool and seated for a task without the wider public learning who they are, but the default rule can flip to full publication of the identities of everyone selected, with confidentiality only as a judge-level exception.
  original setting: A federal district plan may make juror names public, but may also let a judge keep those names confidential where the interests of justice require.
  mechanism: Judge-discretionary confidentiality of juror names under a court's jury selection plan; no technical mechanism specified. (outcome: partial)
  evidence: "If the plan permits these names to be made public, it may nevertheless permit the chief judge of the district court"
- id: gdpr-data-minimisation
  situation: A rule obliges anyone requesting information to take only what the purpose needs, but gives no practical way to request less than a whole document.
  original setting: Controllers collect whole documents when a narrower field would serve the purpose.
  mechanism: Legal principle of data minimisation; no technical mechanism specified. (outcome: partial)
  evidence: "limited to what is necessary in relation to the purposes for which they are processed"
- id: tw-securities-foreign-agent-id-copy
  situation: A foreign investor must prove that its local agent is a real, identified person, and the agent hands over a full copy of an ID card, with no alternative verification stated.
  original setting: 境外華僑及外國人經國內代理人辦理證券開戶時，代理人須檢附國民身分證或居留證影本。
  mechanism: None stated; full ID copy required with no less-intrusive alternative given. (outcome: fails)
  evidence: "國內代理人或代表人之國民身分證、居留證影本或公司登記後之證明文件影本"
- id: tw-pdpa-art11-3-deletion-exception
  situation: A party that has collected a person's data must delete it once the reason for holding it ends, but an open-ended exception lets it keep the data whenever it says it still needs it for its own duties.
  original setting: 個資法第11條第3項：特定目的消失或期限屆滿時應刪除，但因執行職務或業務所必須或經書面同意者不在此限。
  mechanism: Statutory deletion-on-purpose-lapse duty with exceptions for lawful duties or written consent; no technical erasure mechanism specified. (outcome: partial)
  evidence: "個人資料蒐集之特定目的消失或期限屆滿時，應主動或依當事人之請求，刪除、停止處理或利用該個人資料。但因執行職務或業務所必須或經當事人書面同意者，不在此限。"
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

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/union-ballot__C.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
