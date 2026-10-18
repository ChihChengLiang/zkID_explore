You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: peer roommate or carpool matching
The verifier needs to establish: is not on a violent-offender list, shown to a stranger not an institution
Kind of claim (predicate type): non-membership
Today the verifier collects the information under this condition: consented for benefit: the person hands it over voluntarily to receive a benefit or service (discount, subsidy, access)
The fact originates in: justice_security; it is used in: family_social
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: tw-telco-online-id-check-fraud-2021
  situation: A provider must verify that a new applicant is the named person, but its check uses identifiers that are easy to copy, so a stolen identity passes and the real person bears the consequences.
  original setting: 詐騙集團以竊取的身分證資料在電信線上平台申辦門號，電信業者僅審查身分證號與換發日期即通過認證，造成上百人受害。
  mechanism: None; online verification only checked ID number and issue date. (outcome: fails)
  evidence: "僅審查身分證號與換發日期即通過認證"
- id: an-b-jury-selection
  situation: Someone must be drawn from a pool and seated for a task without the wider public learning who they are, but the default rule can flip to full publication of the identities of everyone selected, with confidentiality only as a judge-level exception.
  original setting: A federal district plan may make juror names public, but may also let a judge keep those names confidential where the interests of justice require.
  mechanism: Judge-discretionary confidentiality of juror names under a court's jury selection plan; no technical mechanism specified. (outcome: partial)
  evidence: "If the plan permits these names to be made public, it may nevertheless permit the chief judge of the district court"
- id: an-b-sealed-bid-far
  situation: A party submits a value that must stay hidden from competitors until a fixed moment, while the holder of the submissions must be able to prove later that none were seen early and must handle identifying wrappers without exposing the content.
  original setting: Federal sealed bids must stay unopened and unviewed in a locked or restricted-access box until the scheduled opening, and envelopes may be opened only to identify them by an official designated for that purpose.
  mechanism: Physical and access-control safeguarding of sealed bids with designated-official exception for envelope identification, plus a written record of any mistaken early opening. (outcome: works)
  evidence: "the bids shall not be opened or viewed, and shall remain in a locked bid box, a safe, or in a secured, restricted-access electronic bid box."
- id: an-b-attorney-client
  situation: A party must consult an advisor about a sensitive matter without the advisor, or anyone else, learning or revealing more than the matter requires, but the protection breaks as soon as an outsider is in the room unless the outsider is essential to the relationship.
  original setting: Attorney-client privilege protects confidential communications between a lawyer and client about seeking legal advice, but the confidentiality is compromised if a third party is present.
  mechanism: Evidentiary privilege over communications, lost by third-party presence except essential agents such as interpreters; no technical mechanism. (outcome: partial)
  evidence: "Attorney-client privilege protects confidential communications between a lawyer and their client that relate to the client's seeking of legal advice or services."
- id: rd-twdiw-field-selection-consent
  situation: A user must prove one eligibility fact to a counter, while the credential holds a whole identity record and the user chooses fields at presentation time with no field-level guarantee.
  original setting: Taiwan's Digital Identity Wallet lets users pick which fields to disclose in each scenario, but the official page does not say which fields an age check releases.
  mechanism: Per-scenario field selection after scanning a QR code, confirmed by biometric check, in the TW DIW sandbox. (outcome: partial)
  evidence: "Users can choose what information they consent to share in different scenarios"
- id: an-a-samesite-cookies
  situation: A stored credential should be presented only to the party that issued it in the current context, but the browser sends it on any request the context triggers, so an unrelated observer can match the holder across contexts.
  original setting: A cookie is attached to requests made from third-party sites embedded in a page, which lets those third parties recognise the same browser across unrelated websites.
  mechanism: The SameSite cookie attribute, which limits the cookie to same-site requests (Strict, Lax, or None); the IETF draft describes it as a per-cookie setting, and cross-site behaviour depends on the chosen value. (outcome: partial)
  evidence: "If the "SameSite" attribute's value is "Strict", the cookie will only be sent along with "same-site" requests."

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/roommate-peer__D.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
