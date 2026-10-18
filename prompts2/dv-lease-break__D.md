You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: landlord or employer receiving a protection-order claim
The verifier needs to establish: is covered by an active protection order, for the lease-break or leave window
Kind of claim (predicate type): time-bounded
Today the verifier collects the information under this condition: consented for benefit: the person hands it over voluntarily to receive a benefit or service (discount, subsidy, access)
The fact originates in: justice_security; it is used in: housing
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: an-b-attorney-client
  situation: A party must consult an advisor about a sensitive matter without the advisor, or anyone else, learning or revealing more than the matter requires, but the protection breaks as soon as an outsider is in the room unless the outsider is essential to the relationship.
  original setting: Attorney-client privilege protects confidential communications between a lawyer and client about seeking legal advice, but the confidentiality is compromised if a third party is present.
  mechanism: Evidentiary privilege over communications, lost by third-party presence except essential agents such as interpreters; no technical mechanism. (outcome: partial)
  evidence: "Attorney-client privilege protects confidential communications between a lawyer and their client that relate to the client's seeking of legal advice or services."
- id: tw-telco-online-id-check-fraud-2021
  situation: A provider must verify that a new applicant is the named person, but its check uses identifiers that are easy to copy, so a stolen identity passes and the real person bears the consequences.
  original setting: 詐騙集團以竊取的身分證資料在電信線上平台申辦門號，電信業者僅審查身分證號與換發日期即通過認證，造成上百人受害。
  mechanism: None; online verification only checked ID number and issue date. (outcome: fails)
  evidence: "僅審查身分證號與換發日期即通過認證"
- id: tw-gov-uid-duplicate-minimal-disclosure
  situation: A party asks a registry for identity-number information to settle a dispute; the registry could disclose the full reassigned value, but a narrower answer, whether a duplicate exists, is enough to settle it.
  original setting: 金融機構因國民身分證統一編號重複申請網路銀行而生爭議，欲索取重配後統號；內政部函釋戶政僅可告知有無重複。
  mechanism: Registry reports only whether the number is duplicated, not the reassigned number; the bank marks its own internal record instead. (outcome: works)
  evidence: "戶政事務所得僅告知國民身分證統一編號有無重複，而不提供 其變更之統號"
- id: rd-korea-mdl-age-check-barcode
  situation: A shop must confirm that a buyer is above an age threshold, but the buyer's credential shows the full photo and card details to the cashier, not just the age result.
  original setting: Korea's digital driver's licence in the PASS app is used for age checks in convenience stores, but the same credential also shows the holder's photo on screen.
  mechanism: QR or barcode scan from the wallet app for age verification at the counter; the age result, not the full card, is the intended output. (outcome: partial)
  evidence: "the digital driver’s license can be used to verify age at convenient stores for the purchase of age-limited goods such as alcohol and cigarettes"
- id: an-b-sealed-bid-far
  situation: A party submits a value that must stay hidden from competitors until a fixed moment, while the holder of the submissions must be able to prove later that none were seen early and must handle identifying wrappers without exposing the content.
  original setting: Federal sealed bids must stay unopened and unviewed in a locked or restricted-access box until the scheduled opening, and envelopes may be opened only to identify them by an official designated for that purpose.
  mechanism: Physical and access-control safeguarding of sealed bids with designated-official exception for envelope identification, plus a written record of any mistaken early opening. (outcome: works)
  evidence: "the bids shall not be opened or viewed, and shall remain in a locked bid box, a safe, or in a secured, restricted-access electronic bid box."
- id: rd-eudi-wallet-selective-disclosure-recital
  situation: A verifier needs one attribute from a larger identity record, but the holder cannot share just that attribute from the record.
  original setting: EU law requires the Digital Identity Wallet to let users disclose only some attributes, so relying parties can get what the service needs and no more.
  mechanism: Selective disclosure of attributes from electronic attestations held in the EU Digital Identity Wallet. (outcome: partial)
  evidence: "The European Digital Identity Wallet should technically enable the selective disclosure of attributes to relying parties."

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/dv-lease-break__D.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
