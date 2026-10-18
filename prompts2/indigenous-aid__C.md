You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: scholarship or land programme for indigenous people (原住民身分)
The verifier needs to establish: holds recognised indigenous status (ethnicity: special category)
Kind of claim (predicate type): membership
Today the verifier collects the information under this condition: consented for benefit: the person hands it over voluntarily to receive a benefit or service (discount, subsidy, access)
The fact originates in: government_admin; it is used in: education
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: tw-telco-sim-live-photo-retention
  situation: A provider must confirm a new subscriber's identity before activating a service; the rule requires capturing a live photo of the person at point of sale, with no stated limit on retention.
  original setting: 依NCC指引，初次申辦行動門號者必須即時拍照留存，不願配合者門市應拒絕辦理。
  mechanism: None minimal; in-store photo capture required, no retention limit or less-intrusive alternative stated. (outcome: fails)
  evidence: "要求初次申辦行動通信門號者必須即時拍照留存"
- id: gdpr-data-minimisation
  situation: A rule obliges anyone requesting information to take only what the purpose needs, but gives no practical way to request less than a whole document.
  original setting: Controllers collect whole documents when a narrower field would serve the purpose.
  mechanism: Legal principle of data minimisation; no technical mechanism specified. (outcome: partial)
  evidence: "limited to what is necessary in relation to the purposes for which they are processed"
- id: an-b-ala-library-records
  situation: A service provider must keep a record of who used what without that record becoming a readable log of a person's interests, but the duty is a recommended policy that depends on each institution adopting it and on courts or subpoenas being resisted.
  original setting: Libraries should adopt a policy that treats circulation records and other records identifying library users as confidential, and resist legal demands for them absent a proper showing of good cause.
  mechanism: Institutional confidentiality policy plus procedures for handling subpoenas and law-enforcement requests; no technical minimization of records is specified. (outcome: partial)
  evidence: "Formally adopt a policy that specifically recognizes its circulation records and other records identifying the names of library users to be confidential."
- id: an-b-attorney-client
  situation: A party must consult an advisor about a sensitive matter without the advisor, or anyone else, learning or revealing more than the matter requires, but the protection breaks as soon as an outsider is in the room unless the outsider is essential to the relationship.
  original setting: Attorney-client privilege protects confidential communications between a lawyer and client about seeking legal advice, but the confidentiality is compromised if a third party is present.
  mechanism: Evidentiary privilege over communications, lost by third-party presence except essential agents such as interpreters; no technical mechanism. (outcome: partial)
  evidence: "Attorney-client privilege protects confidential communications between a lawyer and their client that relate to the client's seeking of legal advice or services."
- id: an-b-census-title13
  situation: An agency holding individual responses must release aggregate results, and the legal duty bars any output from which a particular respondent can be singled out, while the holder's staff can still see the raw records.
  original setting: Census data may be used only for statistical purposes, and no publication may allow data furnished by a particular individual or establishment to be identified.
  mechanism: Statutory use limitation and publication prohibition enforced by sworn-oath duties and penalties; statistical disclosure limitation (for example differential privacy in later census products) is a technical layer not specified in the statute. (outcome: partial)
  evidence: "make any publication whereby the data furnished by any particular establishment or individual under this title can be identified"
- id: an-a-tor-onion
  situation: A route must be relayed through intermediaries so that no single intermediary holds both the origin identity and the final destination, while the traffic still reaches the endpoint.
  original setting: A user's network path reveals both who they are and which destination they contact, because the first hop that sees their address also sees their traffic in full.
  mechanism: Onion routing, where the message is wrapped in one encryption layer per relay, and each relay peels only its own layer and passes the rest to the next hop. (outcome: partial)
  evidence: "Each intermediary generally knows only the immediately preceding and following nodes, limiting what any single relay can learn about the route."

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/indigenous-aid__C.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
