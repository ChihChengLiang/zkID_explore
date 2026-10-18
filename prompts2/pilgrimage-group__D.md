You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan. Work alone; read no repository file other than the ones named here, and do not look at other agents' output.

TASK CELL
Setting where the verifier works: pilgrimage or temple tour group (insurance, group fare)
The verifier needs to establish: belongs to a given congregation (religion: special category)
Kind of claim (predicate type): membership
Today the verifier collects the information under this condition: commercial convenience: the verifier collects it because it is easy or helps its business (marketing, fraud screening, habit), with no legal duty
The fact originates in: religion; it is used in: leisure_events
Who could sign the claim is open: you name the issuer (a government body, company, school, hospital, community body, platform or even a peer).

INSPIRATION MATERIAL (real excerpts from other settings). You MUST use at least two of these six items as structural inspiration:
- id: an-b-sealed-bid-far
  situation: A party submits a value that must stay hidden from competitors until a fixed moment, while the holder of the submissions must be able to prove later that none were seen early and must handle identifying wrappers without exposing the content.
  original setting: Federal sealed bids must stay unopened and unviewed in a locked or restricted-access box until the scheduled opening, and envelopes may be opened only to identify them by an official designated for that purpose.
  mechanism: Physical and access-control safeguarding of sealed bids with designated-official exception for envelope identification, plus a written record of any mistaken early opening. (outcome: works)
  evidence: "the bids shall not be opened or viewed, and shall remain in a locked bid box, a safe, or in a secured, restricted-access electronic bid box."
- id: tw-gov-household-register-original-only
  situation: A person asking an agency for a record must prove identity; the rule specifies inspecting the original card rather than handing over a copy, and it does not say the agency retains anything.
  original setting: 請領戶籍謄本時，申請人或利害關係人親自申請須繳驗身分證明文件正本，利害關係證明亦須正本。
  mechanism: Original identity document shown for in-person inspection; the checklist states no retention or copy requirement. (outcome: works)
  evidence: "當事人、利害關係人親自申請者，應繳驗身分證明文件正本；利害關係人應併繳驗利害關係證明文件正本。"
- id: tw-pdpa-art5-purpose-limit
  situation: A rule requires anyone collecting personal data to stay within the necessary scope of its stated purpose, but it gives no concrete way to show what was necessary, so the collector decides what counts as necessary.
  original setting: 個資法第5條要求蒐集、處理或利用個人資料不得逾越特定目的之必要範圍，並應與蒐集目的具正當合理之關聯。
  mechanism: Legal purpose-limitation and proportionality principle; no technical mechanism specified. (outcome: partial)
  evidence: "個人資料之蒐集、處理或利用，應尊重當事人之權益，依誠實及信用方法為之，不得逾越特定目的之必要範圍，並應與蒐集之目的具有正當合理之關聯。"
- id: rd-twdiw-field-selection-consent
  situation: A user must prove one eligibility fact to a counter, while the credential holds a whole identity record and the user chooses fields at presentation time with no field-level guarantee.
  original setting: Taiwan's Digital Identity Wallet lets users pick which fields to disclose in each scenario, but the official page does not say which fields an age check releases.
  mechanism: Per-scenario field selection after scanning a QR code, confirmed by biometric check, in the TW DIW sandbox. (outcome: partial)
  evidence: "Users can choose what information they consent to share in different scenarios"
- id: an-a-privacy-pass
  situation: A verifier only needs to learn that the holder passed an earlier check, but the proof it receives can be matched to the issuance event and to every other use of the same proof.
  original setting: Servers authorise clients with cookies that record a prior challenge, and the same cookie lets them track one client across sessions.
  mechanism: Clients present unlinkable proofs that attest to a prior authorisation, so the origin cannot link redemption to issuance or to other redemptions. (outcome: works)
  evidence: "the privacy goals of Privacy Pass are oriented around unlinkability based on redemption, issuance, and attestation contexts"
- id: an-a-oauth-scopes
  situation: A holder asks a verifier for a credential covering more attributes than the single fact the relying party needs, and the issuer has no obligation to honour a narrower request.
  original setting: A client asks for broad access scopes to a resource server when it needs only one narrow permission, and the user approves the broader grant.
  mechanism: The client states a scope parameter in the request, and the authorization server returns the granted scope in the token response; the server may grant less than requested. (outcome: partial)
  evidence: "The authorization server MAY fully or partially ignore the scope requested by the client, based on the authorization server policy or the resource owner's instructions."

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan, each with a different verifier party or situation, where today the verifier collects far more than it needs and the claim above would be enough. Do not repeat the cell text as the idea; make each moment specific. Be honest in why_zk if law or practice makes it weak.

For each idea, `inspired_by` must list the seeds you actually used. Each `borrowed_aspect` must be one sentence of the form "In <seed>, <X> does <Y>; here, <Z> plays that role", i.e. a mapping, not a vague echo. Every one of the six seeds does not have to be used, but each idea must cite at least one, and the three ideas together at least two different seeds.

Write ONLY a JSON list of 3 objects to ideas2/pilgrimage-group__D.json (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (a list of {"seed_id": ..., "borrowed_aspect": ...}). Use only the Write tool for that one file. Reply with the single word DONE.
