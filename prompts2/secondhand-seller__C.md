You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: peer second-hand trade (OSM: second_hand)
The verifier needs to establish: has sold at least N items with no disputes
Kind of claim (predicate type): aggregate
Today the verifier collects the information under this condition: commercial convenience: the verifier collects it because it is easy or helps its business (marketing, fraud screening, habit), with no legal duty
The fact originates in: commerce; it is used in: commerce
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: an-b-attorney-client
  situation: A party must consult an advisor about a sensitive matter without the advisor, or anyone else, learning or revealing more than the matter requires, but the protection breaks as soon as an outsider is in the room unless the outsider is essential to the relationship.
  original setting: Attorney-client privilege protects confidential communications between a lawyer and client about seeking legal advice, but the confidentiality is compromised if a third party is present.
  mechanism: Evidentiary privilege over communications, lost by third-party presence except essential agents such as interpreters; no technical mechanism. (outcome: partial)
  evidence: "Attorney-client privilege protects confidential communications between a lawyer and their client that relate to the client's seeking of legal advice or services."
- id: tw-gov-id-number-reissue-misuse-2025
  situation: Once the number that identifies a person leaks, reissuing the physical card does not stop someone presenting the same number, so verifiers that check the number and a photo can be fooled.
  original setting: 身分證遺失並掛失換發新證後，同一身分證號碼仍被他人持續冒用，當事人遭罰單與討債困擾。
  mechanism: None; reissuing the card does not change the number. (outcome: fails)
  evidence: "盡管換發新的身分證，但身分證號碼不會改變"
- id: an-b-jury-selection
  situation: Someone must be drawn from a pool and seated for a task without the wider public learning who they are, but the default rule can flip to full publication of the identities of everyone selected, with confidentiality only as a judge-level exception.
  original setting: A federal district plan may make juror names public, but may also let a judge keep those names confidential where the interests of justice require.
  mechanism: Judge-discretionary confidentiality of juror names under a court's jury selection plan; no technical mechanism specified. (outcome: partial)
  evidence: "If the plan permits these names to be made public, it may nevertheless permit the chief judge of the district court"
- id: an-b-ala-library-records
  situation: A service provider must keep a record of who used what without that record becoming a readable log of a person's interests, but the duty is a recommended policy that depends on each institution adopting it and on courts or subpoenas being resisted.
  original setting: Libraries should adopt a policy that treats circulation records and other records identifying library users as confidential, and resist legal demands for them absent a proper showing of good cause.
  mechanism: Institutional confidentiality policy plus procedures for handling subpoenas and law-enforcement requests; no technical minimization of records is specified. (outcome: partial)
  evidence: "Formally adopt a policy that specifically recognizes its circulation records and other records identifying the names of library users to be confidential."
- id: tw-pdpa-art11-3-deletion-exception
  situation: A party that has collected a person's data must delete it once the reason for holding it ends, but an open-ended exception lets it keep the data whenever it says it still needs it for its own duties.
  original setting: 個資法第11條第3項：特定目的消失或期限屆滿時應刪除，但因執行職務或業務所必須或經書面同意者不在此限。
  mechanism: Statutory deletion-on-purpose-lapse duty with exceptions for lawful duties or written consent; no technical erasure mechanism specified. (outcome: partial)
  evidence: "個人資料蒐集之特定目的消失或期限屆滿時，應主動或依當事人之請求，刪除、停止處理或利用該個人資料。但因執行職務或業務所必須或經當事人書面同意者，不在此限。"
- id: an-b-secret-ballot-moad
  situation: A voter must prove eligibility and cast a valid choice while the record of that choice cannot be linked back to them, but the same process must still let officials verify who voted, so the separation depends on procedure rather than on a proof.
  original setting: In the Australian secret ballot, voters keep their identity anonymous from the vote they cast, with separate voting compartments and sealed double envelopes for postal votes.
  mechanism: Separate voting compartments and two-envelope sealing for postal and absentee ballots so identity is not attached to the vote at counting; eligibility is checked separately from the ballot. (outcome: works)
  evidence: "A secret ballot is a voting method where the voter keeps their identity anonymous to provide political privacy."

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/secondhand-seller__C.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
