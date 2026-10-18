You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: pilgrimage or temple tour group (insurance, group fare)
The verifier needs to establish: belongs to a given congregation (religion: special category)
Kind of claim (predicate type): membership
Today the verifier collects the information under this condition: commercial convenience: the verifier collects it because it is easy or helps its business (marketing, fraud screening, habit), with no legal duty
The fact originates in: religion; it is used in: leisure_events
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: an-a-tor-onion
  situation: A route must be relayed through intermediaries so that no single intermediary holds both the origin identity and the final destination, while the traffic still reaches the endpoint.
  original setting: A user's network path reveals both who they are and which destination they contact, because the first hop that sees their address also sees their traffic in full.
  mechanism: Onion routing, where the message is wrapped in one encryption layer per relay, and each relay peels only its own layer and passes the rest to the next hop. (outcome: partial)
  evidence: "Each intermediary generally knows only the immediately preceding and following nodes, limiting what any single relay can learn about the route."
- id: tw-gov-household-register-proxy-copy-discretion
  situation: A government office that holds a record may ask a proxy's requester for a copy of the principal's identity document, and the scope of what it may collect is left to the office's discretion.
  original setting: 內政部函釋：戶政事務所受理委託申請戶籍謄本時，得為蒐集委託人身分證明文件影本，並可斟酌裁量所需附繳證明。
  mechanism: None stated; collection of document copies left to agency discretion under PDPA and administrative procedure rules. (outcome: fails)
  evidence: "即得為蒐集、處理申請人之個人資料（例如繳 驗委託人身分證明文件影本）"
- id: rd-swiss-eid-necessary-data-only
  situation: A business needs one attribute to proceed, but the credential is issued as a whole, so the holder must rely on the wallet to release only the needed attribute.
  original setting: The Swiss e-ID is described as sharing only the data a transaction needs; the technical overview says selective disclosure and batch issuance enable this.
  mechanism: SD-JWT VC selective disclosure with OpenID4VP presentation and status-list validity check. (outcome: partial)
  evidence: "The Swiss e-ID introduces a new approach to digital identity: only the necessary data is shared."
- id: tw-pdpa-art11-3-deletion-exception
  situation: A party that has collected a person's data must delete it once the reason for holding it ends, but an open-ended exception lets it keep the data whenever it says it still needs it for its own duties.
  original setting: 個資法第11條第3項：特定目的消失或期限屆滿時應刪除，但因執行職務或業務所必須或經書面同意者不在此限。
  mechanism: Statutory deletion-on-purpose-lapse duty with exceptions for lawful duties or written consent; no technical erasure mechanism specified. (outcome: partial)
  evidence: "個人資料蒐集之特定目的消失或期限屆滿時，應主動或依當事人之請求，刪除、停止處理或利用該個人資料。但因執行職務或業務所必須或經當事人書面同意者，不在此限。"
- id: an-b-jury-selection
  situation: Someone must be drawn from a pool and seated for a task without the wider public learning who they are, but the default rule can flip to full publication of the identities of everyone selected, with confidentiality only as a judge-level exception.
  original setting: A federal district plan may make juror names public, but may also let a judge keep those names confidential where the interests of justice require.
  mechanism: Judge-discretionary confidentiality of juror names under a court's jury selection plan; no technical mechanism specified. (outcome: partial)
  evidence: "If the plan permits these names to be made public, it may nevertheless permit the chief judge of the district court"
- id: an-a-samesite-cookies
  situation: A stored credential should be presented only to the party that issued it in the current context, but the browser sends it on any request the context triggers, so an unrelated observer can match the holder across contexts.
  original setting: A cookie is attached to requests made from third-party sites embedded in a page, which lets those third parties recognise the same browser across unrelated websites.
  mechanism: The SameSite cookie attribute, which limits the cookie to same-site requests (Strict, Lax, or None); the IETF draft describes it as a per-cookie setting, and cross-site behaviour depends on the chosen value. (outcome: partial)
  evidence: "If the "SameSite" attribute's value is "Strict", the cookie will only be sent along with "same-site" requests."

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/pilgrimage-group__C.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
