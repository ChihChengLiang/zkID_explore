You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: alcohol or e-cigarette vending machine or locker
The verifier needs to establish: is over the legal age, with no operator staff present
Kind of claim (predicate type): threshold
Today the verifier collects the information under this condition: required by law: a statute or regulator obliges the verifier to collect (and often keep) it (KYC/AML, tenancy, licensing)
The fact originates in: government_admin; it is used in: commerce
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: an-b-hipaa-safe-harbor
  situation: A party wants to share a record set that cannot identify any person, but the test is a checklist of removable fields plus a no-actual-knowledge condition, so the holder must still judge whether leftover fields re-identify someone.
  original setting: Health information may be shared for research or trials as de-identified data only after a fixed list of identifiers of the individual and of relatives, employers or household members is removed.
  mechanism: Safe Harbor method removing 18 enumerated identifiers (with ZIP-code truncation rule and age aggregation), or an expert-determination alternative; re-identification codes allowed only if not derived from or disclosed about the individual. (outcome: works)
  evidence: "The following identifiers of the individual or of relatives, employers, or household members of the individual, are removed"
- id: an-b-hipaa-min-necessary
  situation: A holder of sensitive records must release only the subset that serves a stated purpose, but the rule leaves it to the holder to judge what is minimal and gives no mechanism that proves the released subset was minimal.
  original setting: Covered entities and business associates must limit protected health information to what a given use, disclosure or request actually needs.
  mechanism: Purpose-based minimum-necessary rule with reasonable-efforts standard, role-based access and reasonable reliance on requester representations (45 CFR 164.514(d)); no cryptographic or proof-based check. (outcome: partial)
  evidence: "must make reasonable efforts to limit protected health information to the minimum necessary to accomplish the intended purpose of the use, disclosure, or request."
- id: tw-gov-household-register-proxy-copy-discretion
  situation: A government office that holds a record may ask a proxy's requester for a copy of the principal's identity document, and the scope of what it may collect is left to the office's discretion.
  original setting: 內政部函釋：戶政事務所受理委託申請戶籍謄本時，得為蒐集委託人身分證明文件影本，並可斟酌裁量所需附繳證明。
  mechanism: None stated; collection of document copies left to agency discretion under PDPA and administrative procedure rules. (outcome: fails)
  evidence: "即得為蒐集、處理申請人之個人資料（例如繳 驗委託人身分證明文件影本）"
- id: an-a-tor-onion
  situation: A route must be relayed through intermediaries so that no single intermediary holds both the origin identity and the final destination, while the traffic still reaches the endpoint.
  original setting: A user's network path reveals both who they are and which destination they contact, because the first hop that sees their address also sees their traffic in full.
  mechanism: Onion routing, where the message is wrapped in one encryption layer per relay, and each relay peels only its own layer and passes the rest to the next hop. (outcome: partial)
  evidence: "Each intermediary generally knows only the immediately preceding and following nodes, limiting what any single relay can learn about the route."
- id: an-a-nist-dp
  situation: A releaser must answer queries about a dataset so that an observer learns almost nothing about whether any one individual contributed, and the leak must be expressed as a bound that can be checked.
  original setting: Publishing statistics about a dataset can reveal whether a particular person's record is in it, and the publisher has no quantified measure of how much that leaks.
  mechanism: Differential privacy, a randomised release mechanism with a quantified privacy-loss parameter; NIST notes that the guarantee depends on how the framework is realised in practice and lists privacy hazards that can break it. (outcome: partial)
  evidence: "This publication describes differential privacy — a mathematical framework that quantifies privacy loss to entities when their data appears in a dataset."
- id: tw-pdpa-art11-3-deletion-exception
  situation: A party that has collected a person's data must delete it once the reason for holding it ends, but an open-ended exception lets it keep the data whenever it says it still needs it for its own duties.
  original setting: 個資法第11條第3項：特定目的消失或期限屆滿時應刪除，但因執行職務或業務所必須或經書面同意者不在此限。
  mechanism: Statutory deletion-on-purpose-lapse duty with exceptions for lawful duties or written consent; no technical erasure mechanism specified. (outcome: partial)
  evidence: "個人資料蒐集之特定目的消失或期限屆滿時，應主動或依當事人之請求，刪除、停止處理或利用該個人資料。但因執行職務或業務所必須或經當事人書面同意者，不在此限。"

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/vending-age__C.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
