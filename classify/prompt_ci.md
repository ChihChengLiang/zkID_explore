You are labeling proposed selective-disclosure use cases with a contextual-integrity frame. Read /Users/liangcc/projects/repos/zkID_explore/classify/in.json (96 ideas) and no other file.

For each idea label, from its moment, verifier, issuer and disclosed_today:

transmission_principle: the condition under which the verifier collects the information TODAY (before any ZK proof). One of:
- required_by_law: a statute or regulator obliges the verifier to collect (and often keep) it (KYC/AML, tenancy, licensing)
- consented_for_benefit: the person hands it over voluntarily to receive a benefit or service (discount, subsidy, access)
- commercial_convenience: the verifier collects it because it is easy or helps its business (marketing, fraud screening, habit), with no legal duty
- safety_security: collected to protect people or premises (access control, child safety, fraud/abuse prevention)
- public_record: the fact is already in a public register or published list
- other: none of the above fit

origin_context: the setting where the fact is created or held by its issuer. One of: healthcare, education, employment, finance, commerce, government_admin, housing, transport, telecom_online, civic_community, justice_security, family_social, utilities, leisure_events, religion
use_context: the setting where the verifier uses it. One of: healthcare, education, employment, finance, commerce, government_admin, housing, transport, telecom_online, civic_community, justice_security, family_social, utilities, leisure_events, religion
context_distance: one of
- same: origin and use are one context (the organisations may differ)
- adjacent: contexts that routinely share information by law or custom (healthcare to social welfare, employment to finance, school to government)
- different: contexts with no customary information sharing
(Decide origin/use first, then distance; same label for both contexts implies "same".)

Return ONLY a JSON list of 96 objects with keys id, transmission_principle, origin_context, use_context, context_distance, written to the output path in your task. Write a small python script with the labels typed by you per idea (not keyword rules), and verify all 96 ids appear exactly once. Reply with one line.