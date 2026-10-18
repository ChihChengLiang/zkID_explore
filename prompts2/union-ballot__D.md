You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: union strike or bargaining ballot
The verifier needs to establish: is a dues-paying member and votes once, without the employer learning who voted (union membership: special category)
Kind of claim (predicate type): membership
Today the verifier collects the information under this condition: required by law: a statute or regulator obliges the verifier to collect (and often keep) it (KYC/AML, tenancy, licensing)
The fact originates in: employment; it is used in: civic_community
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: tw-pdpa-art11-3-deletion-exception
  situation: A party that has collected a person's data must delete it once the reason for holding it ends, but an open-ended exception lets it keep the data whenever it says it still needs it for its own duties.
  original setting: 個資法第11條第3項：特定目的消失或期限屆滿時應刪除，但因執行職務或業務所必須或經書面同意者不在此限。
  mechanism: Statutory deletion-on-purpose-lapse duty with exceptions for lawful duties or written consent; no technical erasure mechanism specified. (outcome: partial)
  evidence: "個人資料蒐集之特定目的消失或期限屆滿時，應主動或依當事人之請求，刪除、停止處理或利用該個人資料。但因執行職務或業務所必須或經當事人書面同意者，不在此限。"
- id: rd-singpass-myinfo-minimal-request
  situation: A service provider needs a few verified fields for one purpose, but the retrieval interface returns a broad profile and the only limit is a policy rule on the partner.
  original setting: Singpass MyInfo partners retrieve citizen data on consent, and the developer rules tell partners not to over-collect beyond what a single purpose needs.
  mechanism: Consent-gated retrieval of named MyInfo fields, with a rule to request only needed data and purge unsubmitted drafts. (outcome: partial)
  evidence: "Do not over-collect data, where this is not required for business purposes or legal reasons."
- id: rd-twdiw-field-selection-consent
  situation: A user must prove one eligibility fact to a counter, while the credential holds a whole identity record and the user chooses fields at presentation time with no field-level guarantee.
  original setting: Taiwan's Digital Identity Wallet lets users pick which fields to disclose in each scenario, but the official page does not say which fields an age check releases.
  mechanism: Per-scenario field selection after scanning a QR code, confirmed by biometric check, in the TW DIW sandbox. (outcome: partial)
  evidence: "Users can choose what information they consent to share in different scenarios"
- id: an-a-oauth-scopes
  situation: A holder asks a verifier for a credential covering more attributes than the single fact the relying party needs, and the issuer has no obligation to honour a narrower request.
  original setting: A client asks for broad access scopes to a resource server when it needs only one narrow permission, and the user approves the broader grant.
  mechanism: The client states a scope parameter in the request, and the authorization server returns the granted scope in the token response; the server may grant less than requested. (outcome: partial)
  evidence: "The authorization server MAY fully or partially ignore the scope requested by the client, based on the authorization server policy or the resource owner's instructions."
- id: an-b-hipaa-safe-harbor
  situation: A party wants to share a record set that cannot identify any person, but the test is a checklist of removable fields plus a no-actual-knowledge condition, so the holder must still judge whether leftover fields re-identify someone.
  original setting: Health information may be shared for research or trials as de-identified data only after a fixed list of identifiers of the individual and of relatives, employers or household members is removed.
  mechanism: Safe Harbor method removing 18 enumerated identifiers (with ZIP-code truncation rule and age aggregation), or an expert-determination alternative; re-identification codes allowed only if not derived from or disclosed about the individual. (outcome: works)
  evidence: "The following identifiers of the individual or of relatives, employers, or household members of the individual, are removed"
- id: an-b-va-id-scanning
  situation: A venue must confirm that a person is over a threshold age from an identity document, but scanning captures the whole card, so the rule caps what is kept to a few fields and bans secondary use, while the holder still sees everything on the card at the moment of the scan.
  original setting: A merchant may scan the machine-readable zone of a driver's license for an age check, but the scan data it may collect and keep is limited to name, address, date of birth and license number, and may not be disseminated for marketing.
  mechanism: Statutory field-limit and retention ban on scan data, with a prohibition on sale or marketing dissemination; no proof-of-age mechanism that avoids reading the document. (outcome: partial)
  evidence: "Information collected by scanning an individual's driver's license or other document pursuant to this subdivision shall be limited to the individual's name, address, and date of birth and the number of the driver's license or other document;"

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/union-ballot__D.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
