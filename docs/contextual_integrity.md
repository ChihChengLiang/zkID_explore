# Contextual integrity as the frame for the cell design (v2)

## The idea in brief

Helen Nissenbaum's theory of contextual integrity ("Privacy as Contextual Integrity", 2004; *Privacy in Context*, 2010) holds that privacy is not secrecy or control but the *appropriateness of information flows*. Each social setting (healthcare, school, commerce, civic life, family) has norms about what may flow from whom to whom and under what conditions. A diagnosis passing from patient to doctor is appropriate; the same diagnosis passing to an employer is not, though the information is identical.

A flow has five parameters: **sender, recipient, subject, information type, transmission principle** (the condition under which it flows: consent, legal requirement, payment, confidentiality, and so on). It violates contextual integrity when any parameter departs from the setting's norms. Norms are not beyond question: they can be judged by whether they serve the setting's purposes and the interests of those affected, which is how a narrower flow can be justified.

What it adds here: a test for over-disclosure that is not just "too much data" (the flow breaks a norm), a way to say when a narrower proof is still fit for purpose (it serves the setting's purpose), and a place for legal duties (the transmission principle). What it does not do: say anything about adoption, or tell us the norms for Taiwan, which have to be learned from local sources.

## Mapping to this project

| CI parameter | Our axis |
|---|---|
| subject | the person (not an axis) |
| sender | holder or issuer (issuer axis) |
| recipient | verifier / setting (Google place types and OSM, pruned) |
| information type | attribute family + predicate |
| transmission principle | **new axis**: required_by_law, consented_for_benefit, commercial_convenience, safety_security, public_record |
| context | **new tag**: origin context and use context, with `context_distance` same / adjacent / different |

Definitions are in `config/axes.yaml`.

## Cross-context tag
A flow is cross-context when the fact originates in one setting and the verifier uses it in a different one. Label origin and use from the context list, then set `context_distance`. This is where minimal disclosure helps most: inside one context the relationship already bounds what is asked; across contexts the verifier has no business seeing the rest of the source record. It also predicts adoption cost (new issuer, new wallet, new agreements).

## Critic v2 (replaces validity, coherence and the four kill tests)
The v1 critic judged "how well does ZK fit". v2 asks two questions from contextual integrity, plus the adoption checks, which contextual integrity does not cover.

1. **Norm violation today.** State the verifier's legitimate purpose in its context. Does today's flow breach the norms of that context, and on which parameter (recipient, information type, transmission principle, retention)? If not, there is no opportunity (tax filing: the verifier is the issuer).
2. **Purpose-sufficiency.** Does the minimal flow (the proposed predicate) still serve that purpose? What is lost?
3. **Transmission-principle check** (replaces retention_law). Does the principle that applies today permit the minimal flow? `blocks` when a law or regulator requires the full document.
4. **Aggregation** (replaces linkability). Would repeated presentations let anyone combine facts across contexts?
5. **Adoption blockers** (kept, outside contextual integrity): issuer unwilling; verifier lacks tooling or the person lacks a wallet.

Kept unchanged for comparability with v1: `rubric_score`, `novelty`, `provenance_faithful`.

Caveat: contextual integrity says nothing about technology adoption, and norms differ by culture; Taiwan's norms (building committees, temples, family records) must come from local sources, not Western defaults.
