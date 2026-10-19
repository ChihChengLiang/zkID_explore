Classify proposed selective-disclosure use cases by WHO SIGNS the claim (source) and WHO ASKS for it (consumer). Read /Users/liangcc/projects/repos/zkID_explore/classify_sc/in.json (246 ideas) and no other file.

For each idea choose exactly one source_type from the `issuer` field (plus the title and moment for context) and exactly one consumer_type from the `verifier` field. Use the labels below verbatim. Use "other" only when nothing fits, and then add other_note (a short phrase suggesting a new category).

SOURCE TYPES (who issues or signs the claim):
- gov_civil: civil and identity registries: household registration, immigration, ID cards, land registry, tax
- gov_welfare: social welfare, health insurance, labour insurance, disability or low-income certification
- gov_justice: courts, police, prosecutors, victim-protection services, criminal and enforcement records
- gov_licensing: licensing and regulatory bodies: professional licences, business registry, hygiene or safety permits, labour inspection
- education: schools, universities, registrars, training bodies
- healthcare: hospitals, clinics, nurses, medical records
- employer: employers, payroll, contractors
- finance: banks, insurers, payment providers
- telecom: mobile carriers and ISPs
- utility: electricity, water, gas utilities
- platform: e-commerce, ride-hail, delivery, marketplace or social platform accounts
- community_body: unions, building committees, temples and congregations, political parties, associations, libraries
- venue_operator: ticketers, stadiums, event or venue operators
- peer: an individual person vouching for or holding the claim
- other: none of the above

CONSUMER TYPES (who asks and checks):
- landlord_housing: landlords, rental agencies, dormitories, housing operators
- employer_hr: employers, HR, contractors hiring
- school: schools, universities, scholarship or admissions offices
- healthcare: hospitals, clinics, wards, care centres
- bank_insurer: banks, insurers, brokers, lenders
- government_office: government counters and agencies that ask citizens for documents
- justice_security: courts, police, security desks, access control
- retail_commerce: shops, e-commerce sellers, convenience stores, marketplaces
- telecom_digital: telecom shops and online services, apps, digital platforms asking users
- transport_rental: car, scooter, bike rental, airlines, ferries, parking
- venue_events: stadiums, concerts, ticketing, entertainment venues, onsen and baths
- library_culture: libraries, museums, cultural institutions
- religious_body: temples, churches, religious groups
- community_committee: building committees, unions, associations, political parties running votes or membership
- food_vendor: restaurants, night-market stalls, food vendors and their market committees
- hospitality_travel: hotels, tour groups, travel agencies
- funeral_estate: funeral homes, notaries, estate and inheritance handlers
- utility_company: utilities asking for proof
- machine_kiosk: vending machines, lockers, self-service kiosks
- volunteer_ngo: NGOs, volunteer coordinators, charities, disaster shelters
- peer: an individual person verifying another individual
- other: none of the above

Return ONLY a JSON list of 246 objects with keys id, source_type, consumer_type, other_note (empty string when not "other"), written to the output path in your task. Write a small python script with the labels typed by you per idea (not keyword rules), and verify all 246 ids appear exactly once and every label is in the lists. Reply with one line.