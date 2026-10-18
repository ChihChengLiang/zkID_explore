You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: night-market management committee (OSM: marketplace)
The verifier needs to establish: holds a current food-hygiene and stall permit
Kind of claim (predicate type): freshness
Today the verifier collects the information under this condition: required by law: a statute or regulator obliges the verifier to collect (and often keep) it (KYC/AML, tenancy, licensing)
The fact originates in: government_admin; it is used in: commerce
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: tw-bank-deposit-dual-id-check
  situation: A bank must verify who a person is before opening an account, which means examining identity documents, but the cited rule does not say whether copies are kept or for how long.
  original setting: 金管會函釋：金融機構受理開立存款帳戶，應實施雙重身分證明文件查核及確認客戶身分之措施，以防制金融犯罪。
  mechanism: Dual identity-document inspection at account opening; retention and copy handling not specified in the cited text. (outcome: partial)
  evidence: "應實施雙重身分證明文件查核及確認客戶身分"
- id: tw-pdpa-art5-purpose-limit
  situation: A rule requires anyone collecting personal data to stay within the necessary scope of its stated purpose, but it gives no concrete way to show what was necessary, so the collector decides what counts as necessary.
  original setting: 個資法第5條要求蒐集、處理或利用個人資料不得逾越特定目的之必要範圍，並應與蒐集目的具正當合理之關聯。
  mechanism: Legal purpose-limitation and proportionality principle; no technical mechanism specified. (outcome: partial)
  evidence: "個人資料之蒐集、處理或利用，應尊重當事人之權益，依誠實及信用方法為之，不得逾越特定目的之必要範圍，並應與蒐集之目的具有正當合理之關聯。"
- id: an-a-samesite-cookies
  situation: A stored credential should be presented only to the party that issued it in the current context, but the browser sends it on any request the context triggers, so an unrelated observer can match the holder across contexts.
  original setting: A cookie is attached to requests made from third-party sites embedded in a page, which lets those third parties recognise the same browser across unrelated websites.
  mechanism: The SameSite cookie attribute, which limits the cookie to same-site requests (Strict, Lax, or None); the IETF draft describes it as a per-cookie setting, and cross-site behaviour depends on the chosen value. (outcome: partial)
  evidence: "If the "SameSite" attribute's value is "Strict", the cookie will only be sent along with "same-site" requests."
- id: tw-gov-id-number-reissue-misuse-2025
  situation: Once the number that identifies a person leaks, reissuing the physical card does not stop someone presenting the same number, so verifiers that check the number and a photo can be fooled.
  original setting: 身分證遺失並掛失換發新證後，同一身分證號碼仍被他人持續冒用，當事人遭罰單與討債困擾。
  mechanism: None; reissuing the card does not change the number. (outcome: fails)
  evidence: "盡管換發新的身分證，但身分證號碼不會改變"
- id: an-b-hipaa-safe-harbor
  situation: A party wants to share a record set that cannot identify any person, but the test is a checklist of removable fields plus a no-actual-knowledge condition, so the holder must still judge whether leftover fields re-identify someone.
  original setting: Health information may be shared for research or trials as de-identified data only after a fixed list of identifiers of the individual and of relatives, employers or household members is removed.
  mechanism: Safe Harbor method removing 18 enumerated identifiers (with ZIP-code truncation rule and age aggregation), or an expert-determination alternative; re-identification codes allowed only if not derived from or disclosed about the individual. (outcome: works)
  evidence: "The following identifiers of the individual or of relatives, employers, or household members of the individual, are removed"
- id: an-b-sealed-bid-far
  situation: A party submits a value that must stay hidden from competitors until a fixed moment, while the holder of the submissions must be able to prove later that none were seen early and must handle identifying wrappers without exposing the content.
  original setting: Federal sealed bids must stay unopened and unviewed in a locked or restricted-access box until the scheduled opening, and envelopes may be opened only to identify them by an official designated for that purpose.
  mechanism: Physical and access-control safeguarding of sealed bids with designated-official exception for envelope identification, plus a written record of any mistaken early opening. (outcome: works)
  evidence: "the bids shall not be opened or viewed, and shall remain in a locked bid box, a safe, or in a secured, restricted-access electronic bid box."

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/night-market-stall__D.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
