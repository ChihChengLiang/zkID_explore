You are helping find non-obvious uses of zero-knowledge / selective-disclosure credentials in Taiwan (digital wallet, government and private issuers). Work alone; do not read any file in this repository other than what is named here, and do not look at other agents' output.

TASK CELL
Attribute source (who could sign the claim): utility
Predicate type: membership
Situation: A utility can sign that an account belongs to a set (a subsidised roll); a verifier wants set membership without learning the address or usage.

INSPIRATION MATERIAL (real excerpts from other settings; use any that help, ignore any that don't):
- id: an-a-chaum-blind
  situation: A signer must certify that a holder has a valid token without seeing the token's content, and must later be unable to link the certified token back to the signing event.
  original setting: A ballot authority must sign a voter's ballot to certify it, but it must not learn how the voter voted, and the counted ballot must still be accepted as valid.
  mechanism: A blind signature, where the message is blinded with a random factor before signing, and the holder unblinds the signature so it verifies against the original message under the signer's public key. (outcome: works)
  evidence: "An unlinkable blind signature provides this guarantee, as the authority will not see the contents of any ballot it signs, and will be unable to link the blinded ballots it signs back to the un-blinded ballots it receives for counting."
- id: an-b-secret-ballot-moad
  situation: A voter must prove eligibility and cast a valid choice while the record of that choice cannot be linked back to them, but the same process must still let officials verify who voted, so the separation depends on procedure rather than on a proof.
  original setting: In the Australian secret ballot, voters keep their identity anonymous from the vote they cast, with separate voting compartments and sealed double envelopes for postal votes.
  mechanism: Separate voting compartments and two-envelope sealing for postal and absentee ballots so identity is not attached to the vote at counting; eligibility is checked separately from the ballot. (outcome: works)
  evidence: "A secret ballot is a voting method where the voter keeps their identity anonymous to provide political privacy."
- id: rd-google-wallet-zkp-age-no-linkage
  situation: A gatekeeper needs one yes/no fact about a holder, and the proof it receives must not reveal the underlying birth date or let the issuer or the gatekeeper track the holder.
  original setting: Apps asking for age or identity through Google Wallet's digital ID receive shared data; the vendor says it uses zero-knowledge proofs so a verifier learns only the claim.
  mechanism: Zero-knowledge proof on ISO 18013-7 mdocs for an over-18 statement, device-bound transactions, no server-side storage of credential data. (outcome: works)
  evidence: "ZKP ensures that presentations are not identifiable or trackable by the issuer, the relying party, or Google."
- id: an-a-privacy-pass
  situation: A verifier only needs to learn that the holder passed an earlier check, but the proof it receives can be matched to the issuance event and to every other use of the same proof.
  original setting: Servers authorise clients with cookies that record a prior challenge, and the same cookie lets them track one client across sessions.
  mechanism: Clients present unlinkable proofs that attest to a prior authorisation, so the origin cannot link redemption to issuance or to other redemptions. (outcome: works)
  evidence: "the privacy goals of Privacy Pass are oriented around unlinkability based on redemption, issuance, and attestation contexts"
- id: an-b-jury-selection
  situation: Someone must be drawn from a pool and seated for a task without the wider public learning who they are, but the default rule can flip to full publication of the identities of everyone selected, with confidentiality only as a judge-level exception.
  original setting: A federal district plan may make juror names public, but may also let a judge keep those names confidential where the interests of justice require.
  mechanism: Judge-discretionary confidentiality of juror names under a court's jury selection plan; no technical mechanism specified. (outcome: partial)
  evidence: "If the plan permits these names to be made public, it may nevertheless permit the chief judge of the district court"
- id: rd-eudi-wallet-selective-disclosure-recital
  situation: A verifier needs one attribute from a larger identity record, but the holder cannot share just that attribute from the record.
  original setting: EU law requires the Digital Identity Wallet to let users disclose only some attributes, so relying parties can get what the service needs and no more.
  mechanism: Selective disclosure of attributes from electronic attestations held in the EU Digital Identity Wallet. (outcome: partial)
  evidence: "The European Digital Identity Wallet should technically enable the selective disclosure of attributes to relying parties."

Propose exactly 3 distinct use cases for this cell: concrete everyday moments in Taiwan where a verifier today collects far more than it needs, and where a utility-signed membership proof would be enough. Prefer moments that are specific and not the first thing anyone would think of (avoid generic age checks, loan income checks, and diploma verification unless you can make them genuinely specific). Be honest: if a moment is weak because of law or practice, still say so in why_zk rather than hiding it.

For each idea fill inspired_by with the seed ids that actually shaped it and, for each, one sentence naming exactly what you borrowed. Use an empty list only if you truly used none.

Write the three ideas as a YAML list to ideas/utility-member__B.yaml (relative to /Users/liangcc/projects/repos/zkID_explore) with exactly these keys per item: title, moment, verifier, predicate, disclosed_today, issuer, why_zk, inspired_by (list of {seed_id, borrowed_aspect}). Use only the Write tool for that one file. Reply with the single word DONE.
