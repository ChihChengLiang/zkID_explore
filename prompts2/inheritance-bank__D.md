You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: bank releasing a deceased person's deposits
The verifier needs to establish: is an heir entitled to at least a stated share, without exposing the whole family tree
Kind of claim (predicate type): threshold
Today the verifier collects the information under this condition: required by law: a statute or regulator obliges the verifier to collect (and often keep) it (KYC/AML, tenancy, licensing)
The fact originates in: government_admin; it is used in: finance
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: an-b-hipaa-min-necessary
  situation: A holder of sensitive records must release only the subset that serves a stated purpose, but the rule leaves it to the holder to judge what is minimal and gives no mechanism that proves the released subset was minimal.
  original setting: Covered entities and business associates must limit protected health information to what a given use, disclosure or request actually needs.
  mechanism: Purpose-based minimum-necessary rule with reasonable-efforts standard, role-based access and reasonable reliance on requester representations (45 CFR 164.514(d)); no cryptographic or proof-based check. (outcome: partial)
  evidence: "must make reasonable efforts to limit protected health information to the minimum necessary to accomplish the intended purpose of the use, disclosure, or request."
- id: rd-eudi-wallet-selective-disclosure-recital
  situation: A verifier needs one attribute from a larger identity record, but the holder cannot share just that attribute from the record.
  original setting: EU law requires the Digital Identity Wallet to let users disclose only some attributes, so relying parties can get what the service needs and no more.
  mechanism: Selective disclosure of attributes from electronic attestations held in the EU Digital Identity Wallet. (outcome: partial)
  evidence: "The European Digital Identity Wallet should technically enable the selective disclosure of attributes to relying parties."
- id: an-b-hipaa-safe-harbor
  situation: A party wants to share a record set that cannot identify any person, but the test is a checklist of removable fields plus a no-actual-knowledge condition, so the holder must still judge whether leftover fields re-identify someone.
  original setting: Health information may be shared for research or trials as de-identified data only after a fixed list of identifiers of the individual and of relatives, employers or household members is removed.
  mechanism: Safe Harbor method removing 18 enumerated identifiers (with ZIP-code truncation rule and age aggregation), or an expert-determination alternative; re-identification codes allowed only if not derived from or disclosed about the individual. (outcome: works)
  evidence: "The following identifiers of the individual or of relatives, employers, or household members of the individual, are removed"
- id: rd-singpass-myinfo-minimal-request
  situation: A service provider needs a few verified fields for one purpose, but the retrieval interface returns a broad profile and the only limit is a policy rule on the partner.
  original setting: Singpass MyInfo partners retrieve citizen data on consent, and the developer rules tell partners not to over-collect beyond what a single purpose needs.
  mechanism: Consent-gated retrieval of named MyInfo fields, with a rule to request only needed data and purge unsubmitted drafts. (outcome: partial)
  evidence: "Do not over-collect data, where this is not required for business purposes or legal reasons."
- id: an-b-jury-selection
  situation: Someone must be drawn from a pool and seated for a task without the wider public learning who they are, but the default rule can flip to full publication of the identities of everyone selected, with confidentiality only as a judge-level exception.
  original setting: A federal district plan may make juror names public, but may also let a judge keep those names confidential where the interests of justice require.
  mechanism: Judge-discretionary confidentiality of juror names under a court's jury selection plan; no technical mechanism specified. (outcome: partial)
  evidence: "If the plan permits these names to be made public, it may nevertheless permit the chief judge of the district court"
- id: tw-securities-foreign-agent-id-copy
  situation: A foreign investor must prove that its local agent is a real, identified person, and the agent hands over a full copy of an ID card, with no alternative verification stated.
  original setting: 境外華僑及外國人經國內代理人辦理證券開戶時，代理人須檢附國民身分證或居留證影本。
  mechanism: None stated; full ID copy required with no less-intrusive alternative given. (outcome: fails)
  evidence: "國內代理人或代表人之國民身分證、居留證影本或公司登記後之證明文件影本"

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/inheritance-bank__D.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
