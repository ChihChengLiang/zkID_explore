You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan (digital wallet, government and private issuers). Work alone; do not read any file in this repository other than what is named here, and do not look at other agents' output.

TASK CELL
Attribute source (who could sign the claim): government
Predicate type: non-membership
Situation: A government authority can sign that a person does NOT appear on a particular list or register; a verifier wants only that absence.

INSPIRATION MATERIAL (real excerpts from other settings; use any that help, ignore any that don't):
- id: tw-platform-gym-id-card-copies-interp
  situation: A service provider signing up a customer must check identity and payment, but it asks for full front-and-back copies of identity and card documents, and the regulator leaves whether that exceeds the purpose to case-by-case fact-finding.
  original setting: 健身中心於簽立會員契約時要求消費者提供身分證正反面影本及信用卡正反面影本，是否逾越特定目的必要範圍。
  mechanism: None stated; the letter says less-intrusive alternatives must be considered but names none. (outcome: unknown)
  evidence: "健身中心業者於簽立會員契約時，要求消費者提供身分證正反面影本"
- id: an-b-secret-ballot-moad
  situation: A voter must prove eligibility and cast a valid choice while the record of that choice cannot be linked back to them, but the same process must still let officials verify who voted, so the separation depends on procedure rather than on a proof.
  original setting: In the Australian secret ballot, voters keep their identity anonymous from the vote they cast, with separate voting compartments and sealed double envelopes for postal votes.
  mechanism: Separate voting compartments and two-envelope sealing for postal and absentee ballots so identity is not attached to the vote at counting; eligibility is checked separately from the ballot. (outcome: works)
  evidence: "A secret ballot is a voting method where the voter keeps their identity anonymous to provide political privacy."
- id: tw-gov-household-register-original-only
  situation: A person asking an agency for a record must prove identity; the rule specifies inspecting the original card rather than handing over a copy, and it does not say the agency retains anything.
  original setting: 請領戶籍謄本時，申請人或利害關係人親自申請須繳驗身分證明文件正本，利害關係證明亦須正本。
  mechanism: Original identity document shown for in-person inspection; the checklist states no retention or copy requirement. (outcome: works)
  evidence: "當事人、利害關係人親自申請者，應繳驗身分證明文件正本；利害關係人應併繳驗利害關係證明文件正本。"
- id: rd-korea-mdl-age-check-barcode
  situation: A shop must confirm that a buyer is above an age threshold, but the buyer's credential shows the full photo and card details to the cashier, not just the age result.
  original setting: Korea's digital driver's licence in the PASS app is used for age checks in convenience stores, but the same credential also shows the holder's photo on screen.
  mechanism: QR or barcode scan from the wallet app for age verification at the counter; the age result, not the full card, is the intended output. (outcome: partial)
  evidence: "the digital driver’s license can be used to verify age at convenient stores for the purchase of age-limited goods such as alcohol and cigarettes"
- id: an-b-jury-selection
  situation: Someone must be drawn from a pool and seated for a task without the wider public learning who they are, but the default rule can flip to full publication of the identities of everyone selected, with confidentiality only as a judge-level exception.
  original setting: A federal district plan may make juror names public, but may also let a judge keep those names confidential where the interests of justice require.
  mechanism: Judge-discretionary confidentiality of juror names under a court's jury selection plan; no technical mechanism specified. (outcome: partial)
  evidence: "If the plan permits these names to be made public, it may nevertheless permit the chief judge of the district court"
- id: tw-bank-deposit-dual-id-check
  situation: A bank must verify who a person is before opening an account, which means examining identity documents, but the cited rule does not say whether copies are kept or for how long.
  original setting: 金管會函釋：金融機構受理開立存款帳戶，應實施雙重身分證明文件查核及確認客戶身分之措施，以防制金融犯罪。
  mechanism: Dual identity-document inspection at account opening; retention and copy handling not specified in the cited text. (outcome: partial)
  evidence: "應實施雙重身分證明文件查核及確認客戶身分"

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan where a verifier today collects far more than it needs, and where a government-signed non-membership proof would be enough. Prefer moments that are specific and not the first thing anyone would think of (avoid generic age checks, loan income checks, and diploma verification unless you can make them genuinely specific). Be honest: if a moment is weak because of law or practice, still say so in why_zk rather than hiding it.

For each idea fill inspired_by with the seed ids that actually shaped it and, for each, one sentence naming exactly what you borrowed. Use an empty list only if you truly used none.

Write the three ideas as a YAML list to ideas/gov-nonmember__D.yaml (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys per item: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (list of {seed_id, borrowed_aspect}). Use only the Write tool for that one file. Reply with the single word DONE.
