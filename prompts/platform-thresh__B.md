You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan (digital wallet, government and private issuers). Work alone; do not read any file in this repository other than what is named here, and do not look at other agents' output.

TASK CELL
Attribute source (who could sign the claim): platform-zktls
Predicate type: threshold
Situation: A platform account (not designed to issue credentials) holds a number about the user; a verifier wants proof it exceeds a threshold without seeing the account.

INSPIRATION MATERIAL (real excerpts from other settings; use any that help, ignore any that don't):
- id: rd-google-wallet-zkp-age-no-linkage
  situation: A gatekeeper needs one yes/no fact about a holder, and the proof it receives must not reveal the underlying birth date or let the issuer or the gatekeeper track the holder.
  original setting: Apps asking for age or identity through Google Wallet's digital ID receive shared data; the vendor says it uses zero-knowledge proofs so a verifier learns only the claim.
  mechanism: Zero-knowledge proof on ISO 18013-7 mdocs for an over-18 statement, device-bound transactions, no server-side storage of credential data. (outcome: works)
  evidence: "ZKP ensures that presentations are not identifiable or trackable by the issuer, the relying party, or Google."
- id: an-b-va-id-scanning
  situation: A venue must confirm that a person is over a threshold age from an identity document, but scanning captures the whole card, so the rule caps what is kept to a few fields and bans secondary use, while the holder still sees everything on the card at the moment of the scan.
  original setting: A merchant may scan the machine-readable zone of a driver's license for an age check, but the scan data it may collect and keep is limited to name, address, date of birth and license number, and may not be disseminated for marketing.
  mechanism: Statutory field-limit and retention ban on scan data, with a prohibition on sale or marketing dissemination; no proof-of-age mechanism that avoids reading the document. (outcome: partial)
  evidence: "Information collected by scanning an individual's driver's license or other document pursuant to this subdivision shall be limited to the individual's name, address, and date of birth and the number of the driver's license or other document;"
- id: rd-korea-mdl-age-check-barcode
  situation: A shop must confirm that a buyer is above an age threshold, but the buyer's credential shows the full photo and card details to the cashier, not just the age result.
  original setting: Korea's digital driver's licence in the PASS app is used for age checks in convenience stores, but the same credential also shows the holder's photo on screen.
  mechanism: QR or barcode scan from the wallet app for age verification at the counter; the age result, not the full card, is the intended output. (outcome: partial)
  evidence: "the digital driver’s license can be used to verify age at convenient stores for the purchase of age-limited goods such as alcohol and cigarettes"
- id: rd-eudi-wallet-selective-disclosure-recital
  situation: A verifier needs one attribute from a larger identity record, but the holder cannot share just that attribute from the record.
  original setting: EU law requires the Digital Identity Wallet to let users disclose only some attributes, so relying parties can get what the service needs and no more.
  mechanism: Selective disclosure of attributes from electronic attestations held in the EU Digital Identity Wallet. (outcome: partial)
  evidence: "The European Digital Identity Wallet should technically enable the selective disclosure of attributes to relying parties."
- id: tw-gov-uid-duplicate-minimal-disclosure
  situation: A party asks a registry for identity-number information to settle a dispute; the registry could disclose the full reassigned value, but a narrower answer, whether a duplicate exists, is enough to settle it.
  original setting: 金融機構因國民身分證統一編號重複申請網路銀行而生爭議，欲索取重配後統號；內政部函釋戶政僅可告知有無重複。
  mechanism: Registry reports only whether the number is duplicated, not the reassigned number; the bank marks its own internal record instead. (outcome: works)
  evidence: "戶政事務所得僅告知國民身分證統一編號有無重複，而不提供 其變更之統號"
- id: an-a-oauth-scopes
  situation: A holder asks a verifier for a credential covering more attributes than the single fact the relying party needs, and the issuer has no obligation to honour a narrower request.
  original setting: A client asks for broad access scopes to a resource server when it needs only one narrow permission, and the user approves the broader grant.
  mechanism: The client states a scope parameter in the request, and the authorization server returns the granted scope in the token response; the server may grant less than requested. (outcome: partial)
  evidence: "The authorization server MAY fully or partially ignore the scope requested by the client, based on the authorization server policy or the resource owner's instructions."

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan where a verifier today collects far more than it needs, and where a platform-zktls-signed threshold proof would be enough. Prefer moments that are specific and not the first thing anyone would think of (avoid generic age checks, loan income checks, and diploma verification unless you can make them genuinely specific). Be honest: if a moment is weak because of law or practice, still say so in why_zk rather than hiding it.

For each idea fill inspired_by with the seed ids that actually shaped it and, for each, one sentence naming exactly what you borrowed. Use an empty list only if you truly used none.

Write the three ideas as a YAML list to ideas/platform-thresh__B.yaml (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys per item: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (list of {seed_id, borrowed_aspect}). Use only the Write tool for that one file. Reply with the single word DONE.
