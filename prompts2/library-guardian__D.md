You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: public library children's card (google: library)
The verifier needs to establish: is the legal guardian of a child under the card's age limit
Kind of claim (predicate type): membership
Today the verifier collects the information under this condition: consented for benefit: the person hands it over voluntarily to receive a benefit or service (discount, subsidy, access)
The fact originates in: government_admin; it is used in: civic_community
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: tw-telco-online-id-check-fraud-2021
  situation: A provider must verify that a new applicant is the named person, but its check uses identifiers that are easy to copy, so a stolen identity passes and the real person bears the consequences.
  original setting: 詐騙集團以竊取的身分證資料在電信線上平台申辦門號，電信業者僅審查身分證號與換發日期即通過認證，造成上百人受害。
  mechanism: None; online verification only checked ID number and issue date. (outcome: fails)
  evidence: "僅審查身分證號與換發日期即通過認證"
- id: an-b-attorney-client
  situation: A party must consult an advisor about a sensitive matter without the advisor, or anyone else, learning or revealing more than the matter requires, but the protection breaks as soon as an outsider is in the room unless the outsider is essential to the relationship.
  original setting: Attorney-client privilege protects confidential communications between a lawyer and client about seeking legal advice, but the confidentiality is compromised if a third party is present.
  mechanism: Evidentiary privilege over communications, lost by third-party presence except essential agents such as interpreters; no technical mechanism. (outcome: partial)
  evidence: "Attorney-client privilege protects confidential communications between a lawyer and their client that relate to the client's seeking of legal advice or services."
- id: rd-google-wallet-zkp-age-no-linkage
  situation: A gatekeeper needs one yes/no fact about a holder, and the proof it receives must not reveal the underlying birth date or let the issuer or the gatekeeper track the holder.
  original setting: Apps asking for age or identity through Google Wallet's digital ID receive shared data; the vendor says it uses zero-knowledge proofs so a verifier learns only the claim.
  mechanism: Zero-knowledge proof on ISO 18013-7 mdocs for an over-18 statement, device-bound transactions, no server-side storage of credential data. (outcome: works)
  evidence: "ZKP ensures that presentations are not identifiable or trackable by the issuer, the relying party, or Google."
- id: an-b-jury-selection
  situation: Someone must be drawn from a pool and seated for a task without the wider public learning who they are, but the default rule can flip to full publication of the identities of everyone selected, with confidentiality only as a judge-level exception.
  original setting: A federal district plan may make juror names public, but may also let a judge keep those names confidential where the interests of justice require.
  mechanism: Judge-discretionary confidentiality of juror names under a court's jury selection plan; no technical mechanism specified. (outcome: partial)
  evidence: "If the plan permits these names to be made public, it may nevertheless permit the chief judge of the district court"
- id: an-b-secret-ballot-moad
  situation: A voter must prove eligibility and cast a valid choice while the record of that choice cannot be linked back to them, but the same process must still let officials verify who voted, so the separation depends on procedure rather than on a proof.
  original setting: In the Australian secret ballot, voters keep their identity anonymous from the vote they cast, with separate voting compartments and sealed double envelopes for postal votes.
  mechanism: Separate voting compartments and two-envelope sealing for postal and absentee ballots so identity is not attached to the vote at counting; eligibility is checked separately from the ballot. (outcome: works)
  evidence: "A secret ballot is a voting method where the voter keeps their identity anonymous to provide political privacy."
- id: rd-eudi-wallet-selective-disclosure-recital
  situation: A verifier needs one attribute from a larger identity record, but the holder cannot share just that attribute from the record.
  original setting: EU law requires the Digital Identity Wallet to let users disclose only some attributes, so relying parties can get what the service needs and no more.
  mechanism: Selective disclosure of attributes from electronic attestations held in the EU Digital Identity Wallet. (outcome: partial)
  evidence: "The European Digital Identity Wallet should technically enable the selective disclosure of attributes to relying parties."

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/library-guardian__D.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
