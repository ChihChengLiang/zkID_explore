You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: temple handling donations or running a children's programme (google: place_of_worship)
The verifier needs to establish: has no fraud or child-related conviction
Kind of claim (predicate type): non-membership
Today the verifier collects the information under this condition: safety security: collected to protect people or premises (access control, child safety, fraud/abuse prevention)
The fact originates in: justice_security; it is used in: religion
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: an-b-attorney-client
  situation: A party must consult an advisor about a sensitive matter without the advisor, or anyone else, learning or revealing more than the matter requires, but the protection breaks as soon as an outsider is in the room unless the outsider is essential to the relationship.
  original setting: Attorney-client privilege protects confidential communications between a lawyer and client about seeking legal advice, but the confidentiality is compromised if a third party is present.
  mechanism: Evidentiary privilege over communications, lost by third-party presence except essential agents such as interpreters; no technical mechanism. (outcome: partial)
  evidence: "Attorney-client privilege protects confidential communications between a lawyer and their client that relate to the client's seeking of legal advice or services."
- id: gdpr-data-minimisation
  situation: A rule obliges anyone requesting information to take only what the purpose needs, but gives no practical way to request less than a whole document.
  original setting: Controllers collect whole documents when a narrower field would serve the purpose.
  mechanism: Legal principle of data minimisation; no technical mechanism specified. (outcome: partial)
  evidence: "limited to what is necessary in relation to the purposes for which they are processed"
- id: tw-gov-id-number-reissue-misuse-2025
  situation: Once the number that identifies a person leaks, reissuing the physical card does not stop someone presenting the same number, so verifiers that check the number and a photo can be fooled.
  original setting: 身分證遺失並掛失換發新證後，同一身分證號碼仍被他人持續冒用，當事人遭罰單與討債困擾。
  mechanism: None; reissuing the card does not change the number. (outcome: fails)
  evidence: "盡管換發新的身分證，但身分證號碼不會改變"
- id: an-b-hipaa-min-necessary
  situation: A holder of sensitive records must release only the subset that serves a stated purpose, but the rule leaves it to the holder to judge what is minimal and gives no mechanism that proves the released subset was minimal.
  original setting: Covered entities and business associates must limit protected health information to what a given use, disclosure or request actually needs.
  mechanism: Purpose-based minimum-necessary rule with reasonable-efforts standard, role-based access and reasonable reliance on requester representations (45 CFR 164.514(d)); no cryptographic or proof-based check. (outcome: partial)
  evidence: "must make reasonable efforts to limit protected health information to the minimum necessary to accomplish the intended purpose of the use, disclosure, or request."
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

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/temple-volunteer__C.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
