You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: e-scooter or SIM shop serving a visitor
The verifier needs to establish: has a valid entry status that has not expired
Kind of claim (predicate type): time-bounded
Today the verifier collects the information under this condition: required by law: a statute or regulator obliges the verifier to collect (and often keep) it (KYC/AML, tenancy, licensing)
The fact originates in: government_admin; it is used in: telecom_online
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: tw-securities-foreign-agent-id-copy
  situation: A foreign investor must prove that its local agent is a real, identified person, and the agent hands over a full copy of an ID card, with no alternative verification stated.
  original setting: 境外華僑及外國人經國內代理人辦理證券開戶時，代理人須檢附國民身分證或居留證影本。
  mechanism: None stated; full ID copy required with no less-intrusive alternative given. (outcome: fails)
  evidence: "國內代理人或代表人之國民身分證、居留證影本或公司登記後之證明文件影本"
- id: an-a-nist-dp
  situation: A releaser must answer queries about a dataset so that an observer learns almost nothing about whether any one individual contributed, and the leak must be expressed as a bound that can be checked.
  original setting: Publishing statistics about a dataset can reveal whether a particular person's record is in it, and the publisher has no quantified measure of how much that leaks.
  mechanism: Differential privacy, a randomised release mechanism with a quantified privacy-loss parameter; NIST notes that the guarantee depends on how the framework is realised in practice and lists privacy hazards that can break it. (outcome: partial)
  evidence: "This publication describes differential privacy — a mathematical framework that quantifies privacy loss to entities when their data appears in a dataset."
- id: an-b-attorney-client
  situation: A party must consult an advisor about a sensitive matter without the advisor, or anyone else, learning or revealing more than the matter requires, but the protection breaks as soon as an outsider is in the room unless the outsider is essential to the relationship.
  original setting: Attorney-client privilege protects confidential communications between a lawyer and client about seeking legal advice, but the confidentiality is compromised if a third party is present.
  mechanism: Evidentiary privilege over communications, lost by third-party presence except essential agents such as interpreters; no technical mechanism. (outcome: partial)
  evidence: "Attorney-client privilege protects confidential communications between a lawyer and their client that relate to the client's seeking of legal advice or services."
- id: tw-gov-household-register-proxy-copy-discretion
  situation: A government office that holds a record may ask a proxy's requester for a copy of the principal's identity document, and the scope of what it may collect is left to the office's discretion.
  original setting: 內政部函釋：戶政事務所受理委託申請戶籍謄本時，得為蒐集委託人身分證明文件影本，並可斟酌裁量所需附繳證明。
  mechanism: None stated; collection of document copies left to agency discretion under PDPA and administrative procedure rules. (outcome: fails)
  evidence: "即得為蒐集、處理申請人之個人資料（例如繳 驗委託人身分證明文件影本）"
- id: an-b-ala-library-records
  situation: A service provider must keep a record of who used what without that record becoming a readable log of a person's interests, but the duty is a recommended policy that depends on each institution adopting it and on courts or subpoenas being resisted.
  original setting: Libraries should adopt a policy that treats circulation records and other records identifying library users as confidential, and resist legal demands for them absent a proper showing of good cause.
  mechanism: Institutional confidentiality policy plus procedures for handling subpoenas and law-enforcement requests; no technical minimization of records is specified. (outcome: partial)
  evidence: "Formally adopt a policy that specifically recognizes its circulation records and other records identifying the names of library users to be confidential."
- id: an-b-jury-selection
  situation: Someone must be drawn from a pool and seated for a task without the wider public learning who they are, but the default rule can flip to full publication of the identities of everyone selected, with confidentiality only as a judge-level exception.
  original setting: A federal district plan may make juror names public, but may also let a judge keep those names confidential where the interests of justice require.
  mechanism: Judge-discretionary confidentiality of juror names under a court's jury selection plan; no technical mechanism specified. (outcome: partial)
  evidence: "If the plan permits these names to be made public, it may nevertheless permit the chief judge of the district court"

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/tourist-scooter__C.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
