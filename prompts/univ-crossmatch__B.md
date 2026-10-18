You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan (digital wallet, government and private issuers). Work alone; do not read any file in this repository other than what is named here, and do not look at other agents' output.

TASK CELL
Attribute source (who could sign the claim): university
Predicate type: cross-source-match
Situation: A university can sign a claim that must be shown to refer to the same person as a claim from a second, unrelated issuer, without revealing the person's identifier to the verifier.

INSPIRATION MATERIAL (real excerpts from other settings; use any that help, ignore any that don't):
- id: an-a-chaum-blind
  situation: A signer must certify that a holder has a valid token without seeing the token's content, and must later be unable to link the certified token back to the signing event.
  original setting: A ballot authority must sign a voter's ballot to certify it, but it must not learn how the voter voted, and the counted ballot must still be accepted as valid.
  mechanism: A blind signature, where the message is blinded with a random factor before signing, and the holder unblinds the signature so it verifies against the original message under the signer's public key. (outcome: works)
  evidence: "An unlinkable blind signature provides this guarantee, as the authority will not see the contents of any ballot it signs, and will be unable to link the blinded ballots it signs back to the un-blinded ballots it receives for counting."
- id: rd-google-wallet-zkp-age-no-linkage
  situation: A gatekeeper needs one yes/no fact about a holder, and the proof it receives must not reveal the underlying birth date or let the issuer or the gatekeeper track the holder.
  original setting: Apps asking for age or identity through Google Wallet's digital ID receive shared data; the vendor says it uses zero-knowledge proofs so a verifier learns only the claim.
  mechanism: Zero-knowledge proof on ISO 18013-7 mdocs for an over-18 statement, device-bound transactions, no server-side storage of credential data. (outcome: works)
  evidence: "ZKP ensures that presentations are not identifiable or trackable by the issuer, the relying party, or Google."
- id: tw-gov-uid-duplicate-minimal-disclosure
  situation: A party asks a registry for identity-number information to settle a dispute; the registry could disclose the full reassigned value, but a narrower answer, whether a duplicate exists, is enough to settle it.
  original setting: 金融機構因國民身分證統一編號重複申請網路銀行而生爭議，欲索取重配後統號；內政部函釋戶政僅可告知有無重複。
  mechanism: Registry reports only whether the number is duplicated, not the reassigned number; the bank marks its own internal record instead. (outcome: works)
  evidence: "戶政事務所得僅告知國民身分證統一編號有無重複，而不提供 其變更之統號"
- id: an-a-privacy-pass
  situation: A verifier only needs to learn that the holder passed an earlier check, but the proof it receives can be matched to the issuance event and to every other use of the same proof.
  original setting: Servers authorise clients with cookies that record a prior challenge, and the same cookie lets them track one client across sessions.
  mechanism: Clients present unlinkable proofs that attest to a prior authorisation, so the origin cannot link redemption to issuance or to other redemptions. (outcome: works)
  evidence: "the privacy goals of Privacy Pass are oriented around unlinkability based on redemption, issuance, and attestation contexts"
- id: an-a-samesite-cookies
  situation: A stored credential should be presented only to the party that issued it in the current context, but the browser sends it on any request the context triggers, so an unrelated observer can match the holder across contexts.
  original setting: A cookie is attached to requests made from third-party sites embedded in a page, which lets those third parties recognise the same browser across unrelated websites.
  mechanism: The SameSite cookie attribute, which limits the cookie to same-site requests (Strict, Lax, or None); the IETF draft describes it as a per-cookie setting, and cross-site behaviour depends on the chosen value. (outcome: partial)
  evidence: "If the "SameSite" attribute's value is "Strict", the cookie will only be sent along with "same-site" requests."
- id: an-b-witness-protection
  situation: A protected person must be able to show a new identity without revealing the old one, but the program holder keeps a discretionary exception that lets it disclose the true identity to law enforcement or by court order.
  original setting: The Attorney General may disclose or refuse to disclose the identity or location of a relocated or protected witness, weighing danger to the person against the public benefit.
  mechanism: Discretionary non-disclosure of identity and location, with a mandatory disclosure exception to State or local law enforcement on request or by court order when the person is under investigation or charged with a serious offense. (outcome: partial)
  evidence: "disclose or refuse to disclose the identity or location of the person relocated or protected"

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan where a verifier today collects far more than it needs, and where a university-signed cross-source-match proof would be enough. Prefer moments that are specific and not the first thing anyone would think of (avoid generic age checks, loan income checks, and diploma verification unless you can make them genuinely specific). Be honest: if a moment is weak because of law or practice, still say so in why_zk rather than hiding it.

For each idea fill inspired_by with the seed ids that actually shaped it and, for each, one sentence naming exactly what you borrowed. Use an empty list only if you truly used none.

Write the three ideas as a YAML list to ideas/univ-crossmatch__B.yaml (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys per item: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (list of {seed_id, borrowed_aspect}). Use only the Write tool for that one file. Reply with the single word DONE.
