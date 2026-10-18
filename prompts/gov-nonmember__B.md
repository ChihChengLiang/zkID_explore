You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan (digital wallet, government and private issuers). Work alone; do not read any file in this repository other than what is named here, and do not look at other agents' output.

TASK CELL
Attribute source (who could sign the claim): government
Predicate type: non-membership
Situation: A government authority can sign that a person does NOT appear on a particular list or register; a verifier wants only that absence.

INSPIRATION MATERIAL (real excerpts from other settings; use any that help, ignore any that don't):
- id: rd-google-wallet-zkp-age-no-linkage
  situation: A gatekeeper needs one yes/no fact about a holder, and the proof it receives must not reveal the underlying birth date or let the issuer or the gatekeeper track the holder.
  original setting: Apps asking for age or identity through Google Wallet's digital ID receive shared data; the vendor says it uses zero-knowledge proofs so a verifier learns only the claim.
  mechanism: Zero-knowledge proof on ISO 18013-7 mdocs for an over-18 statement, device-bound transactions, no server-side storage of credential data. (outcome: works)
  evidence: "ZKP ensures that presentations are not identifiable or trackable by the issuer, the relying party, or Google."
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
- id: an-a-chaum-blind
  situation: A signer must certify that a holder has a valid token without seeing the token's content, and must later be unable to link the certified token back to the signing event.
  original setting: A ballot authority must sign a voter's ballot to certify it, but it must not learn how the voter voted, and the counted ballot must still be accepted as valid.
  mechanism: A blind signature, where the message is blinded with a random factor before signing, and the holder unblinds the signature so it verifies against the original message under the signer's public key. (outcome: works)
  evidence: "An unlinkable blind signature provides this guarantee, as the authority will not see the contents of any ballot it signs, and will be unable to link the blinded ballots it signs back to the un-blinded ballots it receives for counting."
- id: an-a-privacy-pass
  situation: A verifier only needs to learn that the holder passed an earlier check, but the proof it receives can be matched to the issuance event and to every other use of the same proof.
  original setting: Servers authorise clients with cookies that record a prior challenge, and the same cookie lets them track one client across sessions.
  mechanism: Clients present unlinkable proofs that attest to a prior authorisation, so the origin cannot link redemption to issuance or to other redemptions. (outcome: works)
  evidence: "the privacy goals of Privacy Pass are oriented around unlinkability based on redemption, issuance, and attestation contexts"
- id: rd-apple-wallet-age-request-categories
  situation: A verifier wants a single over-threshold fact, but the request category bundles the issuing authority and a face photo with it, so the verifier can receive more than the age claim.
  original setting: Apple's Verify with Wallet API lists the data an app can request for age checks, and the age category also includes the issuing authority and the ID photo.
  mechanism: Age Over N Flag as a separate requestable value under an entitlement-gated API; no shared name or address. (outcome: partial)
  evidence: "Age verification data: Age Over N Flag Age in Years Issuing Authority ID Photo"

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan where a verifier today collects far more than it needs, and where a government-signed non-membership proof would be enough. Prefer moments that are specific and not the first thing anyone would think of (avoid generic age checks, loan income checks, and diploma verification unless you can make them genuinely specific). Be honest: if a moment is weak because of law or practice, still say so in why_zk rather than hiding it.

For each idea fill inspired_by with the seed ids that actually shaped it and, for each, one sentence naming exactly what you borrowed. Use an empty list only if you truly used none.

Write the three ideas as a YAML list to ideas/gov-nonmember__B.yaml (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys per item: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (list of {seed_id, borrowed_aspect}). Use only the Write tool for that one file. Reply with the single word DONE.
