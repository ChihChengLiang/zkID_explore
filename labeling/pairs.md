# Pair labeling (30 pairs)

For each pair decide **same** (you would count them as one idea: same everyday moment and same kind of verifier, even if worded differently or with a different issuer), **different**, or **unsure**. Fill `labeling/labels.csv`. Cosine and arm are hidden on purpose.

## Pair 1

**A.** **Teaching-assistant or part-time lab hire matched to a work-permit or labour-insurance claim**  
Moment: A university department hires an international or a cross-campus student as a part-time research assistant, and the payroll office must confirm that the student who holds the university's enrolment and department-approval claim is the same person who holds a valid work-permit or labour-insurance enrolment from a government issuer.  
Verifier: University or research-institute human resources and payroll office  
Predicate: The holder of a university-signed enrolment and supervisor-approval credential is the same person as the holder of a government-issued work-eligibility credential (work permit or labour insurance status), proven without revealing passport or ARC number to the department that only needs to approve the hire.  
Issuer: University (enrolment and approval claim), matched to the Ministry of Labor or immigration agency (work eligibility claim)

**B.** **Telecom student-plan SIM activation tied to a university enrolment**  
Moment: A student applies online or in a shop for a discounted student mobile plan or a campus-partner SIM and the telecom must confirm that the enrolled student is the same named person applying, not someone using stolen identity data.  
Verifier: Telecom operator online applications platform or retail shop  
Predicate: The university-signed enrolment claim and the wallet identity credential refer to the same holder, proved with a possession-bound match instead of typing in ID number and issue date.  
Issuer: University (enrolment) cross-matched with the national digital wallet identity credential.

## Pair 2

**A.** **Alumni-discount claim matched to a transit or telecom subscriber account**  
Moment: A graduate renews a subsidised or alumni-linked service (for example a campus-partner telecom plan, a university-affiliated co-working or gym membership, or an alumni association rate) and the vendor wants proof that the person holding the subscription account is the same person the university recognises as an alumnus.  
Verifier: Alumni association or partner vendor offering alumni pricing  
Predicate: The person who holds a university-signed alumnus credential is the same person as the holder of a second issuer's credential (a telecom or membership account credential), proven without revealing the national ID or student number to the vendor.  
Issuer: University (alumnus status claim), matched to a telecom or membership issuer's subscriber claim

**B.** **Student-rate transit pass bound to the same person as the telecom/bank account**  
Moment: A student buys a discounted monthly commuter pass or youth fare product through a transit operator's app, which must be sure the student-status claim belongs to the same person who holds the stored-value or payment account the pass is loaded onto.  
Verifier: Transit operator or e-ticketing issuer (e.g. a city MRT or bus card scheme, or an e-ticket platform).  
Predicate: The university-signed enrolled-this-semester claim and the payment or ticketing account's holder claim refer to the same person, shown without revealing the national ID number to the operator.  
Issuer: University registrar (enrolment status), matched against the wallet-held account or identity credential from a second issuer.

## Pair 3

**A.** **Visitor access to a school or kindergarten after a child's infection with a fixed exclusion period**  
Moment: A child returns to kindergarten or primary school after hand-foot-mouth disease, influenza or COVID, and the school requires proof the child is no longer contagious and has served the exclusion period, which is time-bounded by health-department guidance.  
Verifier: School nurse or kindergarten administrator  
Predicate: A hospital-signed status "cleared to return" valid from the clearance date for the rest of the school term or a stated number of days, without disclosing which illness or the treatment.  
Issuer: Hospital (paediatrics department)

**B.** **Post-surgery or post-procedure "may be left alone / cleared for pickup" window for a ride or care service**  
Moment: After day surgery or a colonoscopy under sedation, the patient is collected by a family member, a taxi or a nursing-aide service that asks for the discharge summary to prove the patient is cleared to leave and who is responsible.  
Verifier: Taxi or care-transport dispatcher, home-care agency, or a hotel or recovery guesthouse near the hospital  
Predicate: Hospital signs "discharged in stable condition, may travel or stay unaccompanied after time T" and it is valid only for the next 24 hours.  
Issuer: Hospital discharge system issuing a time-limited status.

## Pair 4

**A.** **Landlord checks six months of rent payments without seeing the bank statement**  
Moment: A tenant renewing or applying for a rental in Taipei or Taichung is asked by the landlord or agent to photograph passbook pages or send bank statements to prove they have always paid rent on time.  
Verifier: Landlord or rental agency  
Predicate: Count of monthly outgoing transfers of at least the rent amount to the same payee in the last 6 months is 6, with no more than 0 returned or failed transfers.  
Issuer: Tenant's bank (bank signs the count over its own transaction ledger)

**B.** **Landlord rent-payment track record without sharing the tenant's bank statements**  
Moment: A tenant renewing a lease or applying for a new rental in Taipei is asked by the landlord or agent to hand over several months of passbook pages or bank app screenshots to show they pay rent on time.  
Verifier: Private landlord or rental agency (房仲/包租代管業者)  
Predicate: Over the last 12 months, at least 11 monthly outgoing transfers to the same payee were made on or before the 5th of the month (count and on-time ratio computed by the bank).  
Issuer: The tenant's bank (signing a payment-regularity statistic over the account's transfers)

## Pair 5

**A.** **Employer sick-leave or surgery-recovery verification for a specific absence period**  
Moment: An employee is hospitalised or has outpatient surgery and the HR department wants proof that the absence is genuine and covers a date range, before approving paid sick leave or the Labor Standards Act sick-leave allowance.  
Verifier: Employer HR or payroll department  
Predicate: A hospital-signed attestation that the holder was medically unfit for work for the dates from X to Y (credential valid only for that interval), with no diagnosis.  
Issuer: Hospital (attending physician or medical records office)

**B.** **Hospital-signed fit-to-fly or fit-to-travel window for an airline or ferry to the outlying islands**  
Moment: A passenger recovering from surgery, late pregnancy or a heart event books a flight to Kinmen, Penghu or Lanyu, or a long-haul flight, and the carrier or tour operator asks for a doctor's fitness note. Staff photocopy or photograph the note and sometimes keep it with the booking.  
Verifier: Airline check-in counter, ferry operator or travel agent handling the booking  
Predicate: A hospital physician signs that the holder is medically fit to travel for a trip on dates within a stated window, and the proof stops being valid after the window. No diagnosis, procedure, gestational detail or medication is shown.  
Issuer: Treating hospital (attending physician's office)

## Pair 6

**A.** **Delivery-platform courier rating for a building management committee hire**  
Moment: A residential community (社區) in Taipei hires a part-time package-room or night-shift concierge, or lets a gig courier get a building access tag. The management committee wants evidence of reliability.  
Verifier: Community management committee (管理委員會) or its property management company  
Predicate: Lifetime completed deliveries on a delivery platform is at least 500 AND average customer rating is at least 4.7  
Issuer: Delivery platform account (Uber Eats / foodpanda courier app), attested via zkTLS over the logged-in session; the platform never agreed to issue credentials

**B.** **Online marketplace seller sales threshold for a night-market or pop-up stall slot**  
Moment: A Shopee or Ruten seller applies to a city-run weekend creative market (such as a Taichung or Tainan pop-up bazaar) for a priority stall slot that is reserved for sellers who already have a proven online sales record.  
Verifier: Market organizer or district office running the stall lottery  
Predicate: Seller account has at least 200 completed orders and at least 95 percent positive reviews in the past 6 months  
Issuer: Marketplace seller account (seller center), shown through a zkTLS proof over the seller center page

## Pair 7

**A.** **Insurer or employer wellness program checks monthly gym and pharmacy spending band, not itemized purchases**  
Moment: A health-insurance discount programme or a corporate wellness benefit in Taiwan asks participants to upload credit-card statements to prove they spent on fitness, with the same statements revealing pharmacy, clinic and other purchases.  
Verifier: Private insurer or employer benefits administrator  
Predicate: Total card spending in merchant categories for gyms and sports venues over 12 months falls in a stated band, computed by the bank over the cardholder's cards, with no other category disclosed.  
Issuer: Card-issuing bank, which categorizes transactions by merchant category code

**B.** **Overseas-study sponsor shows enough funds without handing a school the family's whole account history**  
Moment: A Taiwanese family applying for a student visa or university admission abroad must show a parent's bank statements proving funds for tuition and living costs for the first year, and the parent sends months of statements to a foreign admissions office or visa agent.  
Verifier: Foreign university admissions office, embassy, or study-abroad agency in Taiwan  
Predicate: The sponsor's combined balance across the bank's accounts has stayed at or above the required amount (for example NT$1,000,000) for each of the last 90 days.  
Issuer: The sponsor's bank, signing a minimum-balance-over-period aggregate across the sponsor's accounts at that bank.

## Pair 8

**A.** **Ride-hail rating as a deposit waiver for scooter and car-share rental**  
Moment: A traveler or student at a shared-car or e-scooter kiosk in Taipei or Kaohsiung is asked to leave a deposit, or the operator screenshots the person's Uber or LINE Taxi passenger profile to judge reliability.  
Verifier: Car-share or scooter-rental operator (for example a station-based car-share service or a rental shop near a train station)  
Predicate: Passenger rating on the ride-hail account is at least 4.8 and the account has at least 50 completed trips  
Issuer: Ride-hail platform account, with the claim made verifiable through a zkTLS session proof against the platform's own logged-in page (the platform is not an issuer and has not agreed to anything)

**B.** **Game or app account level for a community tournament entry**  
Moment: A local esports or board-game-app tournament in Taiwan limits entry to players above a ranking or account level, to stop smurf accounts, and today asks players to hand over account login or screen-share the profile.  
Verifier: Tournament organizer or community Discord moderator  
Predicate: In-game ranked tier >= Diamond (or rating >= 2400) and account age >= 1 year  
Issuer: The game publisher's player profile API, attested through a zkTLS proof of the logged-in profile response

## Pair 9

**A.** **One-per-person limited-edition drop and sneaker or concert pre-sale queues**  
Moment: A Taiwanese buyer tries to claim a limited sale (a console restock, a convenience-store collab figurine, a concert pre-sale) where each person may buy only one, and scalpers use many accounts.  
Verifier: Online retailer or ticketing platform running a limited release.  
Predicate: This account is bound to a distinct, currently active real-name mobile subscriber, and no other account on this platform (for this drop) was bound to the same subscriber.  
Issuer: A Taiwanese mobile carrier (real-name registered subscriber under NCC rules).

**B.** **One free-trial or sign-up bonus per person for a delivery app promotion**  
Moment: A Taiwanese food-delivery or e-commerce app gives a new-user coupon worth a few hundred NT dollars; people farm it with many accounts and burner numbers, so the app starts asking for ID verification or e-invoice carrier and bank details.  
Verifier: Delivery or shopping app running a new-user promotion  
Predicate: This is a distinct subscriber who has not already claimed this promotion under this app's scope, without revealing the number or identity.  
Issuer: Telco with the real-name subscriber record.

## Pair 10

**A.** **Neighbourhood group-buy and community app one-vote-per-household style polls**  
Moment: A residents' community app or LINE-based building management committee runs a poll or a subsidised bulk-purchase (for example a shared water-purifier contract) where each member may take part once, and joining currently means giving a phone number and name to the organiser.  
Verifier: Building management committee or community group-buy organiser.  
Predicate: This participant is one real subscriber and has not already responded in this poll, without revealing the number.  
Issuer: A Taiwanese mobile carrier.

**B.** **One-per-person lottery entry for convenience-store and department-store promotions**  
Moment: A person enters an online draw (for example a 7-Eleven or anniversary-sale prize draw) that is limited to one entry per person, and the organizer wants to stop people from entering with many throwaway phone numbers.  
Verifier: A retailer or the marketing agency running the promotion campaign page.  
Predicate: This entrant holds exactly one real, active postpaid or verified prepaid subscription, and has not entered this campaign before (campaign-scoped uniqueness tag).  
Issuer: A Taiwanese mobile carrier (such as Chunghwa Telecom, Taiwan Mobile or FarEasTone), which already registers every SIM against a real-name identity.

## Pair 11

**A.** **Electricity-bill subsidy roll as proof of eligibility for a school lunch or after-school care fee waiver**  
Moment: A parent enrolls a child in a public after-school care program (or applies for a lunch-fee reduction) at the start of the semester and must show proof of being a low-income or subsidised household.  
Verifier: School administration office / district after-school care operator  
Predicate: The household's utility account is a member of the set of accounts on the low-income or subsidised-rate roll (for example, accounts receiving the low-income household electricity discount).  
Issuer: Taipower (or the local water company), signing membership in the subsidised-account roll

**B.** **Proving a rooftop-solar or farm-pump account is on the registered roll for a grant**  
Moment: A farmer or small household applies for a county subsidy for solar panels, a cold-storage unit or an efficient irrigation pump, and the county office asks for the electricity account's power-contract copy and recent bills to confirm the site is on the registered agricultural or residential-subsidy contract class.  
Verifier: County agriculture or environment bureau processing the grant  
Predicate: The electricity account belongs to the set of accounts under the agricultural-use or registered-subsidy contract class (membership, without the account number, location or consumption).  
Issuer: Taipower signing contract-class roll membership for the account

## Pair 12

**A.** **Night-market stall helper proves current employment to get a staff-only phone plan or rental viewing slot**  
Moment: A landlord or agency in Taipei offers a lower rent or fast-track viewing to tenants who are currently employed at a stable company, and asks for a recent pay slip or employment certificate.  
Verifier: Private landlord or rental agency  
Predicate: Holder is currently employed by a registered employer (not terminated or resigned) as of the last 24 hours  
Issuer: The employer, via an employer-signed credential with revocation upon termination

**B.** **Still-employed proof for landlord rent-guarantee renewal**  
Moment: A tenant renews a lease mid-term and the landlord or rental-management company asks for proof that the tenant is still employed, as a condition of keeping a reduced deposit.  
Verifier: Landlord or property management / rental platform  
Predicate: Employer has signed within the last 7 days that this holder is currently an active employee (not terminated, not on unpaid leave beyond a threshold); signature is revocable on resignation.  
Issuer: Employer (HR system) issuing a short-lived employment-status credential into the wallet.

## Pair 13

**A.** **Student-rate transit pass bound to the same person as the telecom/bank account**  
Moment: A student buys a discounted monthly commuter pass or youth fare product through a transit operator's app, which must be sure the student-status claim belongs to the same person who holds the stored-value or payment account the pass is loaded onto.  
Verifier: Transit operator or e-ticketing issuer (e.g. a city MRT or bus card scheme, or an e-ticket platform).  
Predicate: The university-signed enrolled-this-semester claim and the payment or ticketing account's holder claim refer to the same person, shown without revealing the national ID number to the operator.  
Issuer: University registrar (enrolment status), matched against the wallet-held account or identity credential from a second issuer.

**B.** **Dormitory and campus-housing off-campus lease renewal tied to a landlord-side identity record**  
Moment: A student renting a room near campus is asked by the landlord or a rental agency to prove both that they are enrolled and that the person named on the lease is the same one the university enrolled, so the landlord can claim rent subsidy or insurance cover.  
Verifier: Private landlord or rental agency, and possibly a subsidy administrator reviewing the lease.  
Predicate: The university's signed enrolment claim and the lease or household-record claim from a second issuer (such as the household registration office) refer to the same person, without disclosing the ID number to the landlord.  
Issuer: University registrar, matched against a household registration or ID credential from a government issuer.

## Pair 14

**A.** **Sick-leave validity window for a school or exam make-up without the diagnosis**  
Moment: A parent in Taiwan asks a school to excuse a child's absence from a midterm or a school trip, or a university student asks for a make-up exam after illness. The school asks for the diagnosis certificate (診斷證明書) to be photocopied or photographed and sent over LINE or the school portal.  
Verifier: School administrative office or university registrar  
Predicate: A hospital physician attests that the holder was medically unfit to attend school or sit exams between date A and date B. The proof is valid only for that window and reveals no diagnosis, department or treatment.  
Issuer: Treating hospital, via its physician-signed certificate system

**B.** **Post-surgery or post-procedure "may be left alone / cleared for pickup" window for a ride or care service**  
Moment: After day surgery or a colonoscopy under sedation, the patient is collected by a family member, a taxi or a nursing-aide service that asks for the discharge summary to prove the patient is cleared to leave and who is responsible.  
Verifier: Taxi or care-transport dispatcher, home-care agency, or a hotel or recovery guesthouse near the hospital  
Predicate: Hospital signs "discharged in stable condition, may travel or stay unaccompanied after time T" and it is valid only for the next 24 hours.  
Issuer: Hospital discharge system issuing a time-limited status.

## Pair 15

**A.** **Delivery-platform rating threshold for a building's package-room courier access**  
Moment: A freelance food or parcel courier (Uber Eats, foodpanda, Lalamove driver) applies to a Taipei residential community management committee (社區管委會) or a premium office building for a standing courier access pass, and the building wants evidence the courier is experienced and reliable.  
Verifier: Community management office or building property manager issuing recurring courier access  
Predicate: Platform account has at least 500 completed deliveries and a rating of at least 4.7 over the last 12 months  
Issuer: The delivery platform's own driver account, attested through a zkTLS session over the driver app's stats page (platform did not agree to issue credentials)

**B.** **Online marketplace seller sales threshold for a night-market or pop-up stall slot**  
Moment: A Shopee or Ruten seller applies to a city-run weekend creative market (such as a Taichung or Tainan pop-up bazaar) for a priority stall slot that is reserved for sellers who already have a proven online sales record.  
Verifier: Market organizer or district office running the stall lottery  
Predicate: Seller account has at least 200 completed orders and at least 95 percent positive reviews in the past 6 months  
Issuer: Marketplace seller account (seller center), shown through a zkTLS proof over the seller center page

## Pair 16

**A.** **Still-employed check on gig-platform or staffing-agency workers entering a client factory gate**  
Moment: A dispatched worker from a staffing agency arrives at a client's plant in Taoyuan; the gate must confirm that the agency still employs them, since dispatch contracts end abruptly.  
Verifier: Client factory security gate or contractor-access system  
Predicate: Holder is currently employed by a named staffing agency under a live dispatch contract, with the signature issued today and revocable.  
Issuer: Staffing or dispatch agency as employer.

**B.** **Staff-only discount and access at a company-partnered gym or clinic**  
Moment: An employee walks into a gym, dental clinic or cafeteria operator that has a corporate partnership with their employer and wants the staff rate; the counter must confirm the person is currently employed there, not a former employee with an old badge.  
Verifier: Partner gym, clinic, or vendor front desk  
Predicate: Employer signed within the last 24 hours that the holder is a current employee of this company (presented as a member of the partner group, without name).  
Issuer: Employer, signing a daily or weekly employment-status token; revoking it at departure.

## Pair 17

**A.** **Online marketplace seller reputation for a night-market stall or consignment shop slot**  
Moment: A Shopee or Ruten seller wants a physical consignment shelf in a Taipei pop-up shop or a booth at a weekend market. The organizer wants to know the seller is real and fulfils orders reliably.  
Verifier: Pop-up market organizer or consignment shop owner  
Predicate: Shopee shop completed orders in the last 6 months is at least 200 AND on-time shipping rate is at least 95 percent  
Issuer: Shopee seller center account, attested via zkTLS

**B.** **Delivery-platform rating threshold for a building's package-room courier access**  
Moment: A freelance food or parcel courier (Uber Eats, foodpanda, Lalamove driver) applies to a Taipei residential community management committee (社區管委會) or a premium office building for a standing courier access pass, and the building wants evidence the courier is experienced and reliable.  
Verifier: Community management office or building property manager issuing recurring courier access  
Predicate: Platform account has at least 500 completed deliveries and a rating of at least 4.7 over the last 12 months  
Issuer: The delivery platform's own driver account, attested through a zkTLS session over the driver app's stats page (platform did not agree to issue credentials)

## Pair 18

**A.** **Anonymous eligibility for community solar or energy-saving appliance rebate lottery**  
Moment: A resident enters a local government rebate draw for efficient appliances or a rooftop solar subsidy that is reserved for households on the utility's subsidised or demand-response enrolled roll, and is asked to upload a bill so officials can check enrolment and de-duplicate entries.  
Verifier: City government bureau running the rebate draw  
Predicate: The entrant's account is a member of the enrolled subsidy roll and has not already entered (membership plus a single-use token), with no address or usage revealed.  
Issuer: Taipower, signing enrolment membership of its subsidy or demand-response roll

**B.** **Landlord-free proof that a rented unit is on the residential-rate roll for a tenant subsidy**  
Moment: A tenant applies for a municipal rent subsidy or a student housing grant that requires the unit to be billed at the residential rate (not commercial or illegal sub-divided rates). The office asks for water and electricity bills, which expose the landlord's account, the tenant's name, and the exact unit.  
Verifier: City housing bureau or university housing office  
Predicate: The tenant's utility account is a member of the set of accounts on the residential tariff class at an eligible metering configuration (individual meter, not shared)  
Issuer: Taipower and Taiwan Water Corporation (each signs its own roll membership)

## Pair 19

**A.** **Showing a nanny or tutor is not on the sex-offender notification register**  
Moment: A parent hires a private after-school tutor, a babysitter from a platform, or a cram-school teaches a trial class, and the hiring side wants assurance the person is not on the sexual-offender registry (性侵害加害人登記). Today they ask for a police record certificate (良民證) from the candidate.  
Verifier: A parent, a childcare or tutoring platform, or a small cram-school owner  
Predicate: The holder is not on the sexual-offence offender registration or notification list (non-membership), plus the signing authority and date.  
Issuer: Ministry of the Interior (police administration), or the Ministry of Justice for the criminal record side

**B.** **Showing a landlord that a tenant is not on the public-housing or rent-subsidy disqualification list**  
Moment: A tenant applying to a private landlord that participates in the government social-housing sublease scheme, or a landlord renting under a subsidy program, must show the applicant is not disqualified for owning other property or prior fraud. The agency or landlord's agent collects tax and property records.  
Verifier: Landlord or intermediary operator under the sublease-subsidy program  
Predicate: The applicant is NOT on the register of persons disqualified or blacklisted from housing subsidy for prior false declaration or recovered overpayment.  
Issuer: Ministry of the Interior Construction and Planning Agency (or local housing bureau) as keeper of the disqualification list.

## Pair 20

**A.** **Small-claims or maintenance negotiation proving total outflow to one payee**  
Moment: In a mediation at a township mediation committee or a family-court conciliation, one party says they have paid the other a certain total (for example support or a loan repayment) over a year, and the other side disputes the sum.  
Verifier: Mediator, court clerk or the counterparty's lawyer  
Predicate: Sum of transfers from the person's account to a named payee account between two dates equals or exceeds a stated amount  
Issuer: The bank holding the paying account, signing a sum over a filtered set of transactions

**B.** **Landlord checks six months of rent payments without seeing the bank statement**  
Moment: A tenant renewing or applying for a rental in Taipei or Taichung is asked by the landlord or agent to photograph passbook pages or send bank statements to prove they have always paid rent on time.  
Verifier: Landlord or rental agency  
Predicate: Count of monthly outgoing transfers of at least the rent amount to the same payee in the last 6 months is 6, with no more than 0 returned or failed transfers.  
Issuer: Tenant's bank (bank signs the count over its own transaction ledger)

## Pair 21

**A.** **Electricity-bill subsidy roll as proof of eligibility for a school lunch or after-school care fee waiver**  
Moment: A parent enrolls a child in a public after-school care program (or applies for a lunch-fee reduction) at the start of the semester and must show proof of being a low-income or subsidised household.  
Verifier: School administration office / district after-school care operator  
Predicate: The household's utility account is a member of the set of accounts on the low-income or subsidised-rate roll (for example, accounts receiving the low-income household electricity discount).  
Issuer: Taipower (or the local water company), signing membership in the subsidised-account roll

**B.** **Proving a tenant's subsidised-utility status to a landlord or social-housing agency without revealing the rented address**  
Moment: A person applying for a rent subsidy or a social-housing waitlist slot must show they currently hold a utility account on the subsidised roll, but the agency is also a different locality from the one they rent in, and the applicant does not want a prospective landlord or agency to see the address and usage history.  
Verifier: Municipal housing bureau or social-housing intermediary (e.g. a city social housing agency or a rent-subsidy application window)  
Predicate: The applicant's utility account belongs to the set of accounts on the subsidised-rate roll (and is active), without revealing which account or address.  
Issuer: Taipower / Taiwan Water Corporation

## Pair 22

**A.** **Alumni-discount claim matched to a transit or telecom subscriber account**  
Moment: A graduate renews a subsidised or alumni-linked service (for example a campus-partner telecom plan, a university-affiliated co-working or gym membership, or an alumni association rate) and the vendor wants proof that the person holding the subscription account is the same person the university recognises as an alumnus.  
Verifier: Alumni association or partner vendor offering alumni pricing  
Predicate: The person who holds a university-signed alumnus credential is the same person as the holder of a second issuer's credential (a telecom or membership account credential), proven without revealing the national ID or student number to the vendor.  
Issuer: University (alumnus status claim), matched to a telecom or membership issuer's subscriber claim

**B.** **Hospital internship or clinical-placement badge matched to professional licence**  
Moment: A nursing or medical student starts a clinical placement at a teaching hospital, and the hospital must confirm the university-enrolled student is the same person as the holder of a separate vaccination or background-check record from another issuer.  
Verifier: Hospital HR or placement coordinator  
Predicate: The university-signed placement-eligibility claim and the health-authority vaccination claim refer to the same person, with neither the ID number nor other health records revealed.  
Issuer: University (placement eligibility), matched against a second issuer such as the health authority vaccination record

## Pair 23

**A.** **Student-status discount tied to the same person as the transit or telecom account**  
Moment: A student buys a youth/student monthly pass or a campus-plan mobile subscription, and the seller must be sure the enrolled student is the same person as the account holder.  
Verifier: Transit operator student-pass counter or telecom reseller  
Predicate: The university-signed "currently enrolled" claim and the national-ID-bound claim in the wallet refer to the same person, without revealing the ID number or student number.  
Issuer: University (enrollment status), matched against a second issuer such as the MOI digital ID or a telecom account

**B.** **Dorm or campus-housing landlord checks tenant is the enrolled student named on the lease deposit subsidy**  
Moment: A private landlord renting near a university takes a student tenant who claims a rent subsidy or student-rate lease, and the landlord's bank or local-government subsidy office needs to confirm the tenant is the enrolled student.  
Verifier: Private landlord or housing subsidy office  
Predicate: The university enrollment claim and the tenant's government-issued identity claim belong to the same person, with the ID number and student number withheld.  
Issuer: University (enrollment), matched against the national digital ID or household registration credential

## Pair 24

**A.** **Contract cleaner or security guard proves current on-duty authorization at a building gate**  
Moment: A building management office or gated community in Taiwan lets outsourced staff (cleaning, security, delivery of company goods) enter when their employer vouches they are currently on its roster, and today collects an ID copy and writes down the national ID number in a paper visitor log.  
Verifier: Building management committee or reception desk  
Predicate: Holder is on the active roster of a named contractor employer as of now  
Issuer: The contracting employer, signing a short-lived roster-membership credential and revoking it when the worker leaves

**B.** **Current-staff check for a corporate-discount purchase at a telco or retailer counter**  
Moment: A person buys a phone plan or appliance at a store under an employee-benefit partnership, and the clerk photocopies the employee badge and ID card to confirm the buyer works at the partner company.  
Verifier: Telco or retail store clerk running a corporate-partner discount (企業員工專案)  
Predicate: Holder is a current employee of the partner company today, not a former one still carrying an old badge.  
Issuer: The partner employer, signing a freshness-bound 'currently employed here' status and revoking it when the person leaves.

## Pair 25

**A.** **Proof of recent negative infectious-disease clearance for a short-stay care-facility or day-care visit**  
Moment: A visitor, volunteer or new aide at a nursing home, long-term care center or kindergarten has to show they were tested or cleared (for example no active TB, influenza or norovirus symptoms) within the past few days before entering. Staff today often ask for a photo of the lab report or hospital slip at the door.  
Verifier: Long-term care facility, nursing home or kindergarten staff at the entrance or HR desk  
Predicate: A hospital signs a status of cleared for entry, valid only for N days from the test date. The verifier checks that the status is still in its window and learns neither the test type, the result detail nor any other clinical content.  
Issuer: Hospital laboratory or infection-control department

**B.** **Hospital-signed 'infection-free window' for a hospital-ward caregiver or private nursing-home visitor**  
Moment: A family member or foreign live-in caregiver (外籍看護) arrives at a Taiwanese nursing home or a ward during an outbreak and must show they recently tested negative or are not in an infectious period.  
Verifier: Nursing home (護理之家) front desk or ward access control  
Predicate: Hospital attests 'no active infectious-disease restriction' valid from test date to test date + N days (e.g. 7 days); nothing else.  
Issuer: Hospital or clinic laboratory that ran the test

## Pair 26

**A.** **Night-market stall applies for a platform seller badge with a turnover band, not account history**  
Moment: A small food or goods vendor applying to sell through a delivery or e-commerce platform in Taiwan is asked to upload bank statements to show monthly receipts, so the platform can set a deposit or credit limit.  
Verifier: Delivery or e-commerce platform's merchant onboarding team  
Predicate: Total incoming deposits across the vendor's business accounts over the last 6 months fall in a stated band (for example NT$100,000 to NT$300,000 per month), and no month is more than 30 percent below the average.  
Issuer: The vendor's bank (including a credit cooperative or farmers' and fishermen's association bank), signing a turnover-band aggregate.

**B.** **Overseas-study sponsor shows enough funds without handing a school the family's whole account history**  
Moment: A Taiwanese family applying for a student visa or university admission abroad must show a parent's bank statements proving funds for tuition and living costs for the first year, and the parent sends months of statements to a foreign admissions office or visa agent.  
Verifier: Foreign university admissions office, embassy, or study-abroad agency in Taiwan  
Predicate: The sponsor's combined balance across the bank's accounts has stayed at or above the required amount (for example NT$1,000,000) for each of the last 90 days.  
Issuer: The sponsor's bank, signing a minimum-balance-over-period aggregate across the sponsor's accounts at that bank.

## Pair 27

**A.** **Active-staff proof for staff-only discount at a hospital or university cafeteria and parking**  
Moment: A nurse or contract cleaner at a hospital in Taichung wants the staff meal rate and staff parking tariff, which operators run via outsourced concessions that must not give staff rates to people who have left.  
Verifier: Outsourced cafeteria or parking concessionaire  
Predicate: Holder is on the active payroll or roster of this institution as of today (freshness under 24 hours).  
Issuer: Hospital or university HR/outsourcing employer, including the contractor employer for outsourced workers.

**B.** **Staff-only discount and access at a company-partnered gym or clinic**  
Moment: An employee walks into a gym, dental clinic or cafeteria operator that has a corporate partnership with their employer and wants the staff rate; the counter must confirm the person is currently employed there, not a former employee with an old badge.  
Verifier: Partner gym, clinic, or vendor front desk  
Predicate: Employer signed within the last 24 hours that the holder is a current employee of this company (presented as a member of the partner group, without name).  
Issuer: Employer, signing a daily or weekly employment-status token; revoking it at departure.

## Pair 28

**A.** **One Lunar New Year red-envelope or limited-edition drop claim per person on a Taiwanese convenience-store app**  
Moment: A convenience-store or delivery app in Taiwan releases a limited batch of free coffee coupons or a collectible item at a set hour, and people create many throwaway accounts with prepaid SIM numbers to grab several.  
Verifier: A convenience-store chain loyalty app operator running a limited-quantity promotion.  
Predicate: The claimant holds exactly one active, real-name-registered mobile subscription, and this promotion-specific nullifier has not been used before.  
Issuer: A Taiwanese mobile carrier (real-name SIM registration holder).

**B.** **One vote per person in an apartment-building or community management committee online poll**  
Moment: A Taiwanese residential community (a building management committee) runs an online poll for a repair fund or rule change, and needs one ballot per resident household member without exposing who voted how.  
Verifier: The community management committee (or its property management company) running a LINE or web voting tool.  
Predicate: The voter is one unique real subscriber, and the ballot nullifier is unique for this poll.  
Issuer: A Taiwanese mobile carrier.

## Pair 29

**A.** **Ride-hailing driver rating and trip count for a fleet-leasing deposit waiver**  
Moment: A part-time driver in Taipei applies to a car-leasing or fleet company that waives the deposit for proven reliable drivers. Today the company asks for screenshots of the driver app showing earnings history, ratings, and trip details.  
Verifier: Fleet leasing company or taxi/ride-hailing fleet operator  
Predicate: Completed trips on the platform in the last 12 months >= 500 and average rating >= 4.8  
Issuer: The ride-hailing platform account page, via a zkTLS session proof over the driver's logged-in API response (the platform does not issue credentials)

**B.** **Online marketplace seller sales threshold for a night-market or pop-up stall slot**  
Moment: A Shopee or Ruten seller applies to a city-run weekend creative market (such as a Taichung or Tainan pop-up bazaar) for a priority stall slot that is reserved for sellers who already have a proven online sales record.  
Verifier: Market organizer or district office running the stall lottery  
Predicate: Seller account has at least 200 completed orders and at least 95 percent positive reviews in the past 6 months  
Issuer: Marketplace seller account (seller center), shown through a zkTLS proof over the seller center page

## Pair 30

**A.** **E-commerce seller reputation for a landlord's short-term shop-space sublease**  
Moment: A small online seller on a Taiwanese marketplace wants to rent a pop-up counter or storefront from a landlord. The landlord asks for backend sales dashboards to judge whether the seller can pay rent.  
Verifier: Landlord or property manager of a pop-up space  
Predicate: Trailing 6-month monthly average order revenue >= NT$150,000 and seller cancellation rate <= 2%  
Issuer: The e-commerce marketplace seller dashboard, attested by a zkTLS proof of the logged-in seller-center response

**B.** **Delivery-platform rating threshold for a building's package-room courier access**  
Moment: A freelance food or parcel courier (Uber Eats, foodpanda, Lalamove driver) applies to a Taipei residential community management committee (社區管委會) or a premium office building for a standing courier access pass, and the building wants evidence the courier is experienced and reliable.  
Verifier: Community management office or building property manager issuing recurring courier access  
Predicate: Platform account has at least 500 completed deliveries and a rating of at least 4.7 over the last 12 months  
Issuer: The delivery platform's own driver account, attested through a zkTLS session over the driver app's stats page (platform did not agree to issue credentials)
