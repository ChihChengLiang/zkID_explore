You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: courthouse security desk (google: courthouse)
The verifier needs to establish: holds a summons or hearing notice for today's session
Kind of claim (predicate type): membership
Today the verifier collects the information under this condition: safety security: collected to protect people or premises (access control, child safety, fraud/abuse prevention)
The fact originates in: justice_security; it is used in: justice_security
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: an-a-chaum-blind
  situation: A signer must certify that a holder has a valid token without seeing the token's content, and must later be unable to link the certified token back to the signing event.
  original setting: A ballot authority must sign a voter's ballot to certify it, but it must not learn how the voter voted, and the counted ballot must still be accepted as valid.
  mechanism: A blind signature, where the message is blinded with a random factor before signing, and the holder unblinds the signature so it verifies against the original message under the signer's public key. (outcome: works)
  evidence: "An unlinkable blind signature provides this guarantee, as the authority will not see the contents of any ballot it signs, and will be unable to link the blinded ballots it signs back to the un-blinded ballots it receives for counting."
- id: rd-korea-mdl-age-check-barcode
  situation: A shop must confirm that a buyer is above an age threshold, but the buyer's credential shows the full photo and card details to the cashier, not just the age result.
  original setting: Korea's digital driver's licence in the PASS app is used for age checks in convenience stores, but the same credential also shows the holder's photo on screen.
  mechanism: QR or barcode scan from the wallet app for age verification at the counter; the age result, not the full card, is the intended output. (outcome: partial)
  evidence: "the digital driver’s license can be used to verify age at convenient stores for the purchase of age-limited goods such as alcohol and cigarettes"
- id: an-b-hipaa-min-necessary
  situation: A holder of sensitive records must release only the subset that serves a stated purpose, but the rule leaves it to the holder to judge what is minimal and gives no mechanism that proves the released subset was minimal.
  original setting: Covered entities and business associates must limit protected health information to what a given use, disclosure or request actually needs.
  mechanism: Purpose-based minimum-necessary rule with reasonable-efforts standard, role-based access and reasonable reliance on requester representations (45 CFR 164.514(d)); no cryptographic or proof-based check. (outcome: partial)
  evidence: "must make reasonable efforts to limit protected health information to the minimum necessary to accomplish the intended purpose of the use, disclosure, or request."
- id: rd-singpass-myinfo-minimal-request
  situation: A service provider needs a few verified fields for one purpose, but the retrieval interface returns a broad profile and the only limit is a policy rule on the partner.
  original setting: Singpass MyInfo partners retrieve citizen data on consent, and the developer rules tell partners not to over-collect beyond what a single purpose needs.
  mechanism: Consent-gated retrieval of named MyInfo fields, with a rule to request only needed data and purge unsubmitted drafts. (outcome: partial)
  evidence: "Do not over-collect data, where this is not required for business purposes or legal reasons."
- id: tw-bank-deposit-dual-id-check
  situation: A bank must verify who a person is before opening an account, which means examining identity documents, but the cited rule does not say whether copies are kept or for how long.
  original setting: 金管會函釋：金融機構受理開立存款帳戶，應實施雙重身分證明文件查核及確認客戶身分之措施，以防制金融犯罪。
  mechanism: Dual identity-document inspection at account opening; retention and copy handling not specified in the cited text. (outcome: partial)
  evidence: "應實施雙重身分證明文件查核及確認客戶身分"
- id: privacy-pass-unlinkable-proof
  situation: A gatekeeper only needs to know that the visitor already passed some check, but the proof it accepts doubles as a persistent identifier.
  original setting: Servers authorise clients with cookies, which let them track the same client across sessions.
  mechanism: Blind-signed tokens that attest prior authorisation and cannot be linked to the issuance interaction. (outcome: works)
  evidence: "Clients present unlinkable proofs that attest to this information."

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/court-witness__D.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
