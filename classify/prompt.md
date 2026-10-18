You are classifying proposed selective-disclosure use cases by the KIND OF FACT the verifier needs established about the person. Read /Users/liangcc/projects/repos/zkID_explore/classify/in.json (96 ideas). Read no other file.

For each idea decide, from the idea's `predicate` and `moment`:

family (exactly one, the main fact the verifier needs):
- who_you_are: innate or ascribed trait (age, gender, birthplace, nationality at birth, ethnicity)
- where_you_belong: membership or affiliation (employer, school, residency, union, congregation, building, platform account standing)
- who_you_are_linked_to: relationship (guardian, spouse, dependent, owner, delegate, co-applicant)
- what_you_hold: possession or entitlement (ticket, licence, visa, balance, subsidy eligibility, number of orders)
- what_youve_done: record or history (criminal, driving, payment, vaccination, attendance, work history)
- what_you_can_do: qualification or capability (degree, professional licence, skill test)
- what_state_youre_in: current situation or vulnerability (disability, pregnancy, low income, victim status, illness, current location, hospitalised)
family_secondary: another family from the list if a second kind of fact is clearly also required, else null.

sensitivity: "special" if the fact falls in GDPR Art. 9/10 or Taiwan PDPA Art. 6 special categories (health or medical, genetic, sex life or orientation, ethnicity, religion, political opinion, union membership, biometric, criminal record), else "ordinary". If "special", also give special_kind in one or two words.

stability: one of "immutable" (never changes), "slow" (changes over months or years), "volatile" (changes daily or in real time), "event" (a one-off occurrence like a purchase or entry).

attester: who would sign the fact: one of "government", "company", "platform", "school_or_hospital", "peer_or_self", "other".

Return ONLY a JSON list of 96 objects written to the output path named in your task, each: {"id","family","family_secondary","sensitivity","special_kind","stability","attester"}. Use a python script that you write to emit the JSON, with the labels typed by you per idea (do not guess from keywords). Verify all 96 ids are present exactly once. Reply with one line.
