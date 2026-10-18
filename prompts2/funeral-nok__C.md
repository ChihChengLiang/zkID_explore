You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: funeral home arranging cremation (google: funeral_home)
The verifier needs to establish: is a next of kin of the deceased, in the right order of priority
Kind of claim (predicate type): membership
Today the verifier collects the information under this condition: required by law: a statute or regulator obliges the verifier to collect (and often keep) it (KYC/AML, tenancy, licensing)
The fact originates in: government_admin; it is used in: family_social
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: an-b-jury-selection
  situation: Someone must be drawn from a pool and seated for a task without the wider public learning who they are, but the default rule can flip to full publication of the identities of everyone selected, with confidentiality only as a judge-level exception.
  original setting: A federal district plan may make juror names public, but may also let a judge keep those names confidential where the interests of justice require.
  mechanism: Judge-discretionary confidentiality of juror names under a court's jury selection plan; no technical mechanism specified. (outcome: partial)
  evidence: "If the plan permits these names to be made public, it may nevertheless permit the chief judge of the district court"
- id: rd-swiss-eid-necessary-data-only
  situation: A business needs one attribute to proceed, but the credential is issued as a whole, so the holder must rely on the wallet to release only the needed attribute.
  original setting: The Swiss e-ID is described as sharing only the data a transaction needs; the technical overview says selective disclosure and batch issuance enable this.
  mechanism: SD-JWT VC selective disclosure with OpenID4VP presentation and status-list validity check. (outcome: partial)
  evidence: "The Swiss e-ID introduces a new approach to digital identity: only the necessary data is shared."
- id: rd-singpass-myinfo-minimal-request
  situation: A service provider needs a few verified fields for one purpose, but the retrieval interface returns a broad profile and the only limit is a policy rule on the partner.
  original setting: Singpass MyInfo partners retrieve citizen data on consent, and the developer rules tell partners not to over-collect beyond what a single purpose needs.
  mechanism: Consent-gated retrieval of named MyInfo fields, with a rule to request only needed data and purge unsubmitted drafts. (outcome: partial)
  evidence: "Do not over-collect data, where this is not required for business purposes or legal reasons."
- id: an-a-samesite-cookies
  situation: A stored credential should be presented only to the party that issued it in the current context, but the browser sends it on any request the context triggers, so an unrelated observer can match the holder across contexts.
  original setting: A cookie is attached to requests made from third-party sites embedded in a page, which lets those third parties recognise the same browser across unrelated websites.
  mechanism: The SameSite cookie attribute, which limits the cookie to same-site requests (Strict, Lax, or None); the IETF draft describes it as a per-cookie setting, and cross-site behaviour depends on the chosen value. (outcome: partial)
  evidence: "If the "SameSite" attribute's value is "Strict", the cookie will only be sent along with "same-site" requests."
- id: tw-securities-foreign-agent-id-copy
  situation: A foreign investor must prove that its local agent is a real, identified person, and the agent hands over a full copy of an ID card, with no alternative verification stated.
  original setting: 境外華僑及外國人經國內代理人辦理證券開戶時，代理人須檢附國民身分證或居留證影本。
  mechanism: None stated; full ID copy required with no less-intrusive alternative given. (outcome: fails)
  evidence: "國內代理人或代表人之國民身分證、居留證影本或公司登記後之證明文件影本"
- id: an-b-va-id-scanning
  situation: A venue must confirm that a person is over a threshold age from an identity document, but scanning captures the whole card, so the rule caps what is kept to a few fields and bans secondary use, while the holder still sees everything on the card at the moment of the scan.
  original setting: A merchant may scan the machine-readable zone of a driver's license for an age check, but the scan data it may collect and keep is limited to name, address, date of birth and license number, and may not be disseminated for marketing.
  mechanism: Statutory field-limit and retention ban on scan data, with a prohibition on sale or marketing dissemination; no proof-of-age mechanism that avoids reading the document. (outcome: partial)
  evidence: "Information collected by scanning an individual's driver's license or other document pursuant to this subdivision shall be limited to the individual's name, address, and date of birth and the number of the driver's license or other document;"

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/funeral-nok__C.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
