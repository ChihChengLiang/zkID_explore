You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan (digital wallet, government and private issuers). Work alone; do not read any file in this repository other than what is named here, and do not look at other agents' output.

TASK CELL
Attribute source (who could sign the claim): university
Predicate type: cross-source-match
Situation: A university can sign a claim that must be shown to refer to the same person as a claim from a second, unrelated issuer, without revealing the person's identifier to the verifier.

INSPIRATION MATERIAL (real excerpts from other settings; use any that help, ignore any that don't):
- id: rd-cnpd-lu-tourist-inspect-not-copy
  situation: A host must confirm a visitor's identity and eligibility, but the usual practice is to keep a copy of the whole identity document; the regulator says looking at it is enough.
  original setting: Tourist accommodation operators in Luxembourg ask to see guests' identity documents and some make copies; the regulator reminds them that inspection is allowed and copying is not.
  mechanism: Visual inspection of the identity document with no copy taken; the statutory duty is met by checking, not retaining. (outcome: works)
  evidence: "they may inspect their customers’ identity documents but must not under any circumstances make a copy of them"
- id: tw-telco-sim-live-photo-retention
  situation: A provider must confirm a new subscriber's identity before activating a service; the rule requires capturing a live photo of the person at point of sale, with no stated limit on retention.
  original setting: 依NCC指引，初次申辦行動門號者必須即時拍照留存，不願配合者門市應拒絕辦理。
  mechanism: None minimal; in-store photo capture required, no retention limit or less-intrusive alternative stated. (outcome: fails)
  evidence: "要求初次申辦行動通信門號者必須即時拍照留存"
- id: an-b-ala-library-records
  situation: A service provider must keep a record of who used what without that record becoming a readable log of a person's interests, but the duty is a recommended policy that depends on each institution adopting it and on courts or subpoenas being resisted.
  original setting: Libraries should adopt a policy that treats circulation records and other records identifying library users as confidential, and resist legal demands for them absent a proper showing of good cause.
  mechanism: Institutional confidentiality policy plus procedures for handling subpoenas and law-enforcement requests; no technical minimization of records is specified. (outcome: partial)
  evidence: "Formally adopt a policy that specifically recognizes its circulation records and other records identifying the names of library users to be confidential."
- id: tw-gov-household-register-proxy-copy-discretion
  situation: A government office that holds a record may ask a proxy's requester for a copy of the principal's identity document, and the scope of what it may collect is left to the office's discretion.
  original setting: 內政部函釋：戶政事務所受理委託申請戶籍謄本時，得為蒐集委託人身分證明文件影本，並可斟酌裁量所需附繳證明。
  mechanism: None stated; collection of document copies left to agency discretion under PDPA and administrative procedure rules. (outcome: fails)
  evidence: "即得為蒐集、處理申請人之個人資料（例如繳 驗委託人身分證明文件影本）"
- id: tw-pdpa-art11-3-deletion-exception
  situation: A party that has collected a person's data must delete it once the reason for holding it ends, but an open-ended exception lets it keep the data whenever it says it still needs it for its own duties.
  original setting: 個資法第11條第3項：特定目的消失或期限屆滿時應刪除，但因執行職務或業務所必須或經書面同意者不在此限。
  mechanism: Statutory deletion-on-purpose-lapse duty with exceptions for lawful duties or written consent; no technical erasure mechanism specified. (outcome: partial)
  evidence: "個人資料蒐集之特定目的消失或期限屆滿時，應主動或依當事人之請求，刪除、停止處理或利用該個人資料。但因執行職務或業務所必須或經當事人書面同意者，不在此限。"
- id: an-b-jury-selection
  situation: Someone must be drawn from a pool and seated for a task without the wider public learning who they are, but the default rule can flip to full publication of the identities of everyone selected, with confidentiality only as a judge-level exception.
  original setting: A federal district plan may make juror names public, but may also let a judge keep those names confidential where the interests of justice require.
  mechanism: Judge-discretionary confidentiality of juror names under a court's jury selection plan; no technical mechanism specified. (outcome: partial)
  evidence: "If the plan permits these names to be made public, it may nevertheless permit the chief judge of the district court"

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan where a verifier today collects far more than it needs, and where a university-signed cross-source-match proof would be enough. Prefer moments that are specific and not the first thing anyone would think of (avoid generic age checks, loan income checks, and diploma verification unless you can make them genuinely specific). Be honest: if a moment is weak because of law or practice, still say so in why_zk rather than hiding it.

For each idea fill inspired_by with the seed ids that actually shaped it and, for each, one sentence naming exactly what you borrowed. Use an empty list only if you truly used none.

Write the three ideas as a YAML list to ideas/univ-crossmatch__C.yaml (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys per item: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (list of {seed_id, borrowed_aspect}). Use only the Write tool for that one file. Reply with the single word DONE.
