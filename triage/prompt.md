You are labelling proposed selective-disclosure use cases with a structured schema. Read /Users/liangcc/projects/repos/zkID_explore/triage/in.json (37 ideas) and no other file.

CERTIFICATE CATALOGUE (certificate_id (name; issuer type): claim ids). Map each idea's needed attributes to `certificate_id.claim_id` from this list. If no catalogued certificate carries a needed attribute, write `MISSING:<short attribute name>`. Use only what the idea's `predicate` and `moment` need, not what `disclosed_today` hands over.
- eu_pid (EU person identification data (reference model); issuer gov_civil): family_name, given_name, birth_date, birth_place, nationality, portrait, resident_address, resident_city, resident_country, personal_administrative_number, sex, issuing_authority, issuance_date, expiry_date, document_number | precomputable: age_over_N (separate age attestation under CIR 2024/2977, not part of PID since v1.1)
- iso_mdl (Mobile driving licence (ISO 18013-5 data elements); issuer gov_licensing): family_name, given_name, birth_date, issue_date, expiry_date, issuing_country, issuing_authority, document_number, portrait, driving_privileges, un_distinguishing_sign, sex, height, birth_place, resident_address, nationality, age_in_years, age_birth_year, age_over_NN, administrative_number | precomputable: age_over_NN
- tw_national_id (Taiwan national ID card; issuer gov_civil): name, id_number, birth_date, sex, issue_date, address, portrait | precomputable: age_over_20; is_adult (age >= 18, Civil Code adulthood changed 2023); sex
- tw_household_transcript (Household registration transcript; issuer gov_civil): household_head, member_names, member_relationships, member_birth_dates, registered_domicile, household_address, marital_status, spouse_name, parents_names, ethnic_group | precomputable: is_resident_of_<city>; is_member_of_household_with_id_X; indigenous_status
- tw_arc (Alien resident certificate (ARC); issuer gov_civil): name, nationality, birth_date, sex, arc_number, residence_valid_until, residence_reason, address | precomputable: is_legally_resident_now; age_over_NN
- tw_passport (Passport (ICAO 9303-style data page); issuer gov_civil): surname, given_names, nationality, birth_date, sex, birth_place, passport_number, issue_date, expiry_date, portrait | precomputable: age_over_NN; nationality_is_X
- tw_entry_exit_record (Entry and exit record; issuer gov_civil): entry_dates, exit_dates, permitted_stay_until, visa_type | precomputable: has_not_overstayed; days_in_country_in_period
- tw_criminal_record (Police criminal record certificate; issuer gov_justice): subject_name, id_number, record_status, offence_details, issue_date | precomputable: no_record_as_of_date; no_offence_of_type_X
- tw_protection_order (Protection order; issuer gov_justice): order_type, applicant, respondent, valid_from, valid_until, restricted_acts, case_number | precomputable: is_protected_person_now; order_valid_between_dates
- tw_court_summons (Court summons or hearing notice; issuer gov_justice): case_number, court, hearing_datetime, role, subject_name | precomputable: has_hearing_today_at_court_X
- tw_driver_licence (Driver's licence; issuer gov_licensing): name, id_number, birth_date, licence_classes, issue_date, expiry_date, restrictions, address, licence_number, portrait | precomputable: valid_for_class_X_now; age_over_NN
- tw_vehicle_licence (Vehicle licence; issuer gov_licensing): plate_number, owner_name, vehicle_type, first_registration_date, inspection_due, owner_id_number | precomputable: owner_of_plate_X; inspection_current
- tw_nhi_card (National Health Insurance card; issuer gov_welfare): name, id_number, birth_date, sex, card_number, issue_date, catastrophic_illness_flag, enrolment_status | precomputable: is_insured_now; age_over_NN
- tw_labour_insurance_record (Labour insurance enrolment record; issuer gov_welfare): insured_employer, enrolment_start, enrolment_end, insured_salary_tier, total_coverage_years, claims_history | precomputable: currently_enrolled_with_employer_X; salary_tier >= T; coverage_years >= N
- tw_income_statement (Individual income tax statement; issuer gov_civil): tax_year, income_by_category, total_income, dependents, withholding | precomputable: total_income >= T for year Y
- tw_property_title (Land and building title; issuer gov_civil): owner_name, parcel_or_building_id, address, area, acquisition_date, encumbrances, assessed_value | precomputable: is_owner_of_address_X; no_encumbrance
- tw_diploma (Diploma; issuer education): holder_name, institution, degree_level, major, graduation_date, honours | precomputable: holds_degree_level >= X; degree_from_accredited_institution
- tw_transcript (Academic transcript; issuer education): courses, grades, gpa, credits, rank | precomputable: gpa >= T; credits >= N
- tw_enrolment_certificate (Enrolment certificate; issuer education): student_name, institution, student_number, enrolment_status, term, expected_graduation | precomputable: enrolled_this_term; student_of_institution_X
- tw_student_id (Student ID card; issuer education): name, student_number, institution, valid_until, portrait | precomputable: valid_student_now
- tw_professional_licence (Professional licence (e.g. nurse, engineer); issuer gov_licensing): holder_name, licence_type, licence_number, issue_date, valid_until, registration_status, practice_location, disciplinary_flag | precomputable: holds_valid_licence_of_type_X_now
- tw_safety_training (Safety training certificate; issuer gov_licensing): worker_name, course, issue_date, valid_until, provider | precomputable: valid_for_course_X_now
- tw_employment_certificate (Employment certificate; issuer employer): employee_name, employer, job_title, start_date, salary, currently_employed | precomputable: currently_employed_at_X; tenure >= N months; salary >= T
- tw_payslip (Payslip; issuer employer): employee_name, employer, period, gross, deductions, net | precomputable: monthly_income >= T for last N months
- tw_bank_deposit_certificate (Bank deposit certificate; issuer finance): account_holder, bank, balance, as_of_date, currency | precomputable: balance >= T as of date
- tw_bank_statement (Bank statement; issuer finance): account_holder, transactions, monthly_inflow, closing_balance | precomputable: average_monthly_inflow >= T; no_transaction_with_X
- tw_disability_certificate (Disability certificate; issuer gov_welfare): holder_name, id_number, disability_category, disability_level, review_due_date, valid_until | precomputable: holds_valid_disability_certificate; needs_accessible_parking
- tw_low_income_certificate (Low-income household certificate; issuer gov_welfare): household_head, household_size, income_tier, members, valid_from, valid_until | precomputable: eligible_for_subsidy_tier_X_now
- tw_vaccination_record (Vaccination record; issuer healthcare): vaccine, dose_dates, lot_number, provider | precomputable: vaccinated_against_X_since_date
- tw_medical_certificate (Medical certificate (diagnosis, rest advice); issuer healthcare): patient_name, diagnosis, treatment_dates, physician_advice, hospital | precomputable: unfit_for_work_between_dates; fit_to_fly_window
- tw_death_certificate (Death certificate and deregistration; issuer healthcare): deceased_name, date_of_death, cause_of_death, place_of_death | precomputable: person_X_is_deceased
- tw_heir_chart (Heir relationship chart; issuer gov_civil): deceased_name, heirs, order_of_inheritance | precomputable: is_heir_with_share >= S; is_next_of_kin_priority_1
- tw_power_of_attorney (Power of attorney / delegation; issuer peer): principal, delegate, scope, valid_from, valid_until | precomputable: is_authorised_delegate_for_task_X_today
- tw_military_status (Military service status; issuer gov_civil): service_type, completion_date, exemption_reason | precomputable: completed_service; exempt_status
- tw_business_registration (Company or business registration; issuer gov_licensing): business_name, unified_business_number, representative, directors, capital, address, status | precomputable: is_registered_and_active; is_representative_of_X
- tw_food_permit (Food hygiene and stall permit; issuer gov_licensing): holder_name, stall_type, location, valid_until | precomputable: holds_current_permit
- tw_utility_bill (Utility bill; issuer utility): account_holder, service_address, usage_kwh, amount_due, payment_status, subsidy_flag | precomputable: resides_at_address_X; on_subsidy_roll
- tw_sim_registration (SIM real-name registration; issuer telecom): subscriber_name, id_number, msisdn, activation_date, plan_type, line_status | precomputable: one_active_line_per_person; subscriber_tenure >= N months
- tw_event_ticket (Event ticket; issuer venue_operator): event, seat, ticket_id, purchase_time, holder_account, transferable | precomputable: holds_valid_ticket_for_event_X; one_ticket_per_person_per_event (nullifier)
- tw_union_card (Union membership card; issuer community_body): member_name, union, member_id, dues_paid_until | precomputable: is_member_in_good_standing_of_X
- tw_party_membership (Political party membership; issuer community_body): member_name, party, district, member_since, dues_status | precomputable: is_member_in_district_Y
- tw_library_card (Library card; issuer community_body): patron_name, card_number, borrowing_privilege, outstanding_fines, home_library, borrowing_history | precomputable: no_overdue_anywhere_in_network; is_registered_patron
- tw_unit_deed_vote (Condominium ownership and voting weight; issuer community_body): owner_name, unit, ownership_share, voting_weight, resident_flag | precomputable: owner_of_unit_with_weight_W_votes_once

SCHEMA AND SCALES:
# Structured fields for one idea: predicate (what attributes, what operation), channel (how the interaction happens today),
# and three ordinal signals replacing a dollar value. Draft; edit freely.
predicate:
  inputs:        "list of 'certificate_id.claim_id' from config/certificates.yaml, or 'MISSING:<attribute needed>' when no catalogued certificate carries it"
  operator:
    reveal:         "disclose the claim value as is"
    threshold:      "claim compared with a constant (age >= N, income >= T)"
    membership:     "claim value in a set, or the person is in a group"
    non_membership: "person is NOT in a list or register"
    uniqueness:     "one account, ticket or vote per person (needs a nullifier or similar)"
    freshness:      "status holds as of now (not revoked, not expired)"
    cross_match:    "claims from two different certificates refer to the same person"
    time_bounded:   "claim holds within a date window"
    aggregate:      "statistic over many records (sum, average, count)"
  zk_need:          # the smallest mechanism that does the job
    plain_disclosure:   "selective disclosure of an existing claim; no ZK"
    issuer_precomputed: "the issuer signs the derived claim (e.g. age_over_NN, is_resident); no ZK, but needs issuer cooperation"
    zk_derived:         "verifier needs a fact the issuer never signed, derived from signed claims (age from birth date, threshold on a number)"
    zk_join:            "proof must combine claims from different credentials"
    zk_nullifier:       "uniqueness across presentations"
    zk_nonmembership:   "proof of absence from a list"
    zk_aggregate:       "statistic over many signed records"
  unlinkability_needed: "yes if repeated presentations to the same or different verifiers must not be linkable"
  freshness_needed:     "none | days | realtime"
channel:
  current_evidence:     "paper_copy | id_shown_in_person | photo_of_id | digital_upload | app_login | machine_scan | none"
  interaction_mode:     "in_person_no_device | in_person_with_device | remote_online | remote_assisted | machine_mediated"
  verifier_reader:      "has_reader | would_need_tool | unknown  (can the verifier already scan or read a wallet presentation?)"
signals:
  reach_log10:          "order of magnitude of people in Taiwan hitting this moment per year: 3 (thousands) to 7 (millions)"
  harm_per_incident:    "1 inconvenience | 2 privacy exposure (retained copy) | 3 targeted misuse risk (fraud, stalking, discrimination) | 4 severe (safety, persecution)"
  verifier_incentive:   "0 none or negative | 1 weak (convenience) | 2 moderate (cost or compliance burden) | 3 strong (legal exposure, breach liability, fraud loss)"
  split_incentive:      "true when the benefit goes to the person and the cost of change to the verifier"


For each idea return an object with keys: id, inputs (list), operator (one of the operator keys), zk_need (one of the zk_need keys), unlinkability_needed ("yes"/"no"), freshness_needed ("none"/"days"/"realtime"), current_evidence, interaction_mode, verifier_reader, reach_log10 (integer 3-7), harm_per_incident (1-4), verifier_incentive (0-3), split_incentive (true/false), rationale (one sentence). Think about Taiwan: for channel, judge what really happens today (e.g. a rental counter photocopies the card in person; a delivery-app signup is already on the phone). When unsure about verifier tooling, use "unknown".

Return ONLY a JSON list of 37 objects, written to the output path named in your task, built by a small python script with the labels typed by you per idea (not keyword rules). Verify all 37 ids appear once and enumerated values are valid. Reply with one line.