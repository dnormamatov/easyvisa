"""Seed data for countries, visa types, and visa requirements."""

COUNTRIES = [
    {"name": "Latvia", "code": "LV"},
    {"name": "Slovakia", "code": "SK"},
    {"name": "Germany", "code": "DE"},
    {"name": "Poland", "code": "PL"},
    {"name": "United Kingdom", "code": "GB"},
]

VISA_TYPES = [
    {"name": "Student Visa", "slug": "student"},
    {"name": "Tourist Visa", "slug": "tourist"},
    {"name": "Work Visa", "slug": "work"},
]

VISA_REQUIREMENTS = [
    # Latvia
    {
        "country_code": "LV",
        "visa_type_slug": "student",
        "required_documents": (
            "• Valid passport (6+ months validity)\n"
            "• University acceptance letter\n"
            "• Proof of tuition payment or scholarship\n"
            "• Bank statement (€3,000+ balance)\n"
            "• Health insurance valid in Schengen\n"
            "• Accommodation confirmation\n"
            "• 2 passport-size photos\n"
            "• Completed visa application form"
        ),
        "application_process": (
            "1. Receive acceptance from a Latvian university\n"
            "2. Gather all required documents\n"
            "3. Book appointment at VFS Global (Tashkent)\n"
            "4. Submit application and pay visa fee\n"
            "5. Attend biometrics appointment\n"
            "6. Wait for decision and collect passport"
        ),
        "processing_time": "15–30 business days",
        "estimated_costs": (
            "• Visa fee: €80\n"
            "• VFS service fee: ~€30\n"
            "• Health insurance: €50–100/year\n"
            "• Translation/notarization: €50–150\n"
            "• Total estimate: €210–360"
        ),
    },
    {
        "country_code": "LV",
        "visa_type_slug": "tourist",
        "required_documents": (
            "• Valid passport (3+ months beyond stay)\n"
            "• Travel itinerary and hotel bookings\n"
            "• Bank statement (€50/day minimum)\n"
            "• Travel health insurance (€30,000 coverage)\n"
            "• Return flight tickets\n"
            "• Employment letter or business registration\n"
            "• 2 passport-size photos\n"
            "• Completed Schengen visa application"
        ),
        "application_process": (
            "1. Prepare travel plan and bookings\n"
            "2. Purchase travel insurance\n"
            "3. Book appointment at VFS Global (Tashkent)\n"
            "4. Submit documents and pay fees\n"
            "5. Attend biometrics\n"
            "6. Collect visa upon approval"
        ),
        "processing_time": "10–15 business days",
        "estimated_costs": (
            "• Visa fee: €80\n"
            "• VFS service fee: ~€30\n"
            "• Travel insurance: €20–40\n"
            "• Total estimate: €130–150"
        ),
    },
    {
        "country_code": "LV",
        "visa_type_slug": "work",
        "required_documents": (
            "• Valid passport\n"
            "• Work permit from OCMA (Latvia)\n"
            "• Employment contract with Latvian employer\n"
            "• Employer's registration documents\n"
            "• Proof of qualifications\n"
            "• Criminal record certificate\n"
            "• Health insurance\n"
            "• 2 passport-size photos"
        ),
        "application_process": (
            "1. Employer applies for work permit in Latvia\n"
            "2. Receive work permit approval\n"
            "3. Apply for Type D national visa at VFS Global\n"
            "4. Submit all documents and attend biometrics\n"
            "5. Travel to Latvia and apply for residence permit"
        ),
        "processing_time": "30–60 business days",
        "estimated_costs": (
            "• Visa fee: €80\n"
            "• Work permit fee: ~€100\n"
            "• VFS service fee: ~€30\n"
            "• Document translation: €100–200\n"
            "• Total estimate: €310–410"
        ),
    },
    # Slovakia
    {
        "country_code": "SK",
        "visa_type_slug": "student",
        "required_documents": (
            "• Valid passport (6+ months validity)\n"
            "• Letter of acceptance from Slovak university\n"
            "• Proof of financial means (€4,000+/year)\n"
            "• Accommodation proof\n"
            "• Health insurance for Schengen area\n"
            "• Academic transcripts (translated)\n"
            "• 2 biometric photos\n"
            "• Completed visa application form"
        ),
        "application_process": (
            "1. Apply and get accepted to a Slovak university\n"
            "2. Collect and translate documents\n"
            "3. Schedule appointment at embassy/VFS\n"
            "4. Submit application with biometrics\n"
            "5. Wait for visa decision\n"
            "6. Register residence upon arrival in Slovakia"
        ),
        "processing_time": "15–30 business days",
        "estimated_costs": (
            "• Visa fee: €80\n"
            "• VFS service fee: ~€35\n"
            "• Health insurance: €50–120/year\n"
            "• Document translation: €50–150\n"
            "• Total estimate: €215–385"
        ),
    },
    {
        "country_code": "SK",
        "visa_type_slug": "tourist",
        "required_documents": (
            "• Valid passport\n"
            "• Round-trip flight reservation\n"
            "• Hotel/accommodation bookings\n"
            "• Bank statement (€50/day)\n"
            "• Schengen travel insurance\n"
            "• Employment/income proof\n"
            "• 2 passport photos\n"
            "• Visa application form"
        ),
        "application_process": (
            "1. Plan your trip and make reservations\n"
            "2. Obtain travel insurance\n"
            "3. Book embassy/VFS appointment\n"
            "4. Submit application and biometrics\n"
            "5. Track application status\n"
            "6. Collect passport with visa"
        ),
        "processing_time": "10–15 business days",
        "estimated_costs": (
            "• Visa fee: €80\n"
            "• VFS service fee: ~€35\n"
            "• Travel insurance: €20–40\n"
            "• Total estimate: €135–155"
        ),
    },
    {
        "country_code": "SK",
        "visa_type_slug": "work",
        "required_documents": (
            "• Valid passport\n"
            "• Work permit from Slovak Labour Office\n"
            "• Employment contract\n"
            "• Employer's business registration\n"
            "• Educational certificates\n"
            "• Criminal record (apostilled)\n"
            "• Health insurance\n"
            "• 2 biometric photos"
        ),
        "application_process": (
            "1. Employer obtains work permit in Slovakia\n"
            "2. Apply for national D visa\n"
            "3. Submit documents at embassy/VFS\n"
            "4. Attend biometrics appointment\n"
            "5. Receive visa and travel to Slovakia\n"
            "6. Apply for temporary residence within 3 days"
        ),
        "processing_time": "30–45 business days",
        "estimated_costs": (
            "• Visa fee: €80\n"
            "• Work permit: ~€170\n"
            "• VFS service fee: ~€35\n"
            "• Apostille/translation: €100–250\n"
            "• Total estimate: €385–535"
        ),
    },
    # Germany
    {
        "country_code": "DE",
        "visa_type_slug": "student",
        "required_documents": (
            "• Valid passport\n"
            "• University admission letter (Zulassungsbescheid)\n"
            "• Blocked account (€11,904/year) or scholarship proof\n"
            "• Health insurance confirmation\n"
            "• Academic certificates (translated & certified)\n"
            "• Language proficiency proof (German/English)\n"
            "• Biometric photos\n"
            "• Completed national visa application"
        ),
        "application_process": (
            "1. Apply to German university and receive admission\n"
            "2. Open blocked account (Sperrkonto) or show scholarship\n"
            "3. Book appointment at German Embassy (Tashkent)\n"
            "4. Submit visa application with all documents\n"
            "5. Attend interview if required\n"
            "6. Receive visa and register at university upon arrival"
        ),
        "processing_time": "4–8 weeks",
        "estimated_costs": (
            "• Visa fee: €75\n"
            "• Blocked account setup: €50–150\n"
            "• Health insurance: €80–120/month\n"
            "• Document certification: €100–300\n"
            "• Total estimate: €305–645 (excluding blocked funds)"
        ),
    },
    {
        "country_code": "DE",
        "visa_type_slug": "tourist",
        "required_documents": (
            "• Valid passport (3+ months validity)\n"
            "• Travel itinerary with dates\n"
            "• Hotel bookings or invitation letter\n"
            "• Bank statement (€45–100/day)\n"
            "• Schengen travel insurance (€30,000+)\n"
            "• Flight reservations\n"
            "• Employment/income proof\n"
            "• 2 biometric photos"
        ),
        "application_process": (
            "1. Prepare travel plan and bookings\n"
            "2. Get travel health insurance\n"
            "3. Book appointment at German Embassy\n"
            "4. Submit Schengen visa application\n"
            "5. Provide biometrics\n"
            "6. Collect passport with visa sticker"
        ),
        "processing_time": "10–15 business days",
        "estimated_costs": (
            "• Visa fee: €80\n"
            "• Travel insurance: €25–50\n"
            "• Total estimate: €105–130"
        ),
    },
    {
        "country_code": "DE",
        "visa_type_slug": "work",
        "required_documents": (
            "• Valid passport\n"
            "• Approved work visa/pre-approval from German authorities\n"
            "• Employment contract with salary details\n"
            "• Employer's invitation and company documents\n"
            "• Professional qualifications (recognized in Germany)\n"
            "• CV and reference letters\n"
            "• Criminal record certificate\n"
            "• Health insurance proof"
        ),
        "application_process": (
            "1. Employer initiates visa process with local Foreigners' Office\n"
            "2. Receive pre-approval (Vorabzustimmung)\n"
            "3. Apply for national visa at German Embassy\n"
            "4. Attend interview with complete documentation\n"
            "5. Receive visa and travel to Germany\n"
            "6. Apply for residence permit at local Ausländerbehörde"
        ),
        "processing_time": "6–12 weeks",
        "estimated_costs": (
            "• Visa fee: €75\n"
            "• Qualification recognition: €100–600\n"
            "• Document translation: €150–300\n"
            "• Residence permit fee (in Germany): ~€100\n"
            "• Total estimate: €425–1,075"
        ),
    },
    # Poland
    {
        "country_code": "PL",
        "visa_type_slug": "student",
        "required_documents": (
            "• Valid passport\n"
            "• University acceptance letter\n"
            "• Proof of tuition payment\n"
            "• Bank statement (€3,000+ or PLN equivalent)\n"
            "• Health insurance valid in Poland\n"
            "• Accommodation confirmation\n"
            "• Academic documents (translated to Polish/English)\n"
            "• 2 passport photos"
        ),
        "application_process": (
            "1. Get accepted to a Polish university\n"
            "2. Pay tuition deposit if required\n"
            "3. Book appointment at Polish Embassy/VFS\n"
            "4. Submit national visa application\n"
            "5. Attend biometrics\n"
            "6. Apply for residence card after arrival"
        ),
        "processing_time": "15–30 business days",
        "estimated_costs": (
            "• Visa fee: €80\n"
            "• VFS service fee: ~€25\n"
            "• Health insurance: €40–100/year\n"
            "• Translation: €50–150\n"
            "• Total estimate: €195–355"
        ),
    },
    {
        "country_code": "PL",
        "visa_type_slug": "tourist",
        "required_documents": (
            "• Valid passport\n"
            "• Travel itinerary\n"
            "• Hotel/accommodation bookings\n"
            "• Bank statement (€50/day)\n"
            "• Schengen travel insurance\n"
            "• Return tickets\n"
            "• Employment letter\n"
            "• 2 passport photos"
        ),
        "application_process": (
            "1. Plan trip and make reservations\n"
            "2. Purchase travel insurance\n"
            "3. Book VFS/embassy appointment\n"
            "4. Submit Schengen visa application\n"
            "5. Provide biometrics\n"
            "6. Collect visa upon approval"
        ),
        "processing_time": "10–15 business days",
        "estimated_costs": (
            "• Visa fee: €80\n"
            "• VFS service fee: ~€25\n"
            "• Travel insurance: €20–40\n"
            "• Total estimate: €125–145"
        ),
    },
    {
        "country_code": "PL",
        "visa_type_slug": "work",
        "required_documents": (
            "• Valid passport\n"
            "• Work permit (zezwolenie na pracę)\n"
            "• Employment contract\n"
            "• Employer's registration documents\n"
            "• Professional qualifications\n"
            "• Criminal record certificate\n"
            "• Health insurance\n"
            "• 2 biometric photos"
        ),
        "application_process": (
            "1. Employer obtains work permit from Voivodeship Office\n"
            "2. Apply for national D visa at embassy/VFS\n"
            "3. Submit all required documents\n"
            "4. Attend biometrics appointment\n"
            "5. Travel to Poland with visa\n"
            "6. Apply for temporary residence permit"
        ),
        "processing_time": "30–60 business days",
        "estimated_costs": (
            "• Visa fee: €80\n"
            "• Work permit: ~€50\n"
            "• VFS service fee: ~€25\n"
            "• Translation/apostille: €100–200\n"
            "• Total estimate: €255–355"
        ),
    },
    # United Kingdom
    {
        "country_code": "GB",
        "visa_type_slug": "student",
        "required_documents": (
            "• Valid passport\n"
            "• CAS (Confirmation of Acceptance for Studies) from UK university\n"
            "• TB test certificate (from approved clinic in Tashkent)\n"
            "• Bank statement (28-day rule, tuition + £1,334/month living costs)\n"
            "• Academic qualifications\n"
            "• English language test (IELTS/TOEFL) if required\n"
            "• ATAS certificate (for certain courses)\n"
            "• Parental consent (if under 18)"
        ),
        "application_process": (
            "1. Apply to UK university and receive CAS\n"
            "2. Take TB test at approved clinic\n"
            "3. Prepare financial evidence (28-day rule)\n"
            "4. Apply online at gov.uk/student-visa\n"
            "5. Pay IHS (Immigration Health Surcharge) and visa fee\n"
            "6. Book biometrics at VFS Global\n"
            "7. Submit documents and wait for decision"
        ),
        "processing_time": "3–8 weeks",
        "estimated_costs": (
            "• Visa fee: £490\n"
            "• IHS: £776/year\n"
            "• TB test: ~£50\n"
            "• VFS priority (optional): £500\n"
            "• Total estimate: £1,316+ (standard service)"
        ),
    },
    {
        "country_code": "GB",
        "visa_type_slug": "tourist",
        "required_documents": (
            "• Valid passport\n"
            "• Bank statements (6 months, showing sufficient funds)\n"
            "• Employment letter with salary and leave approval\n"
            "• Travel itinerary and accommodation\n"
            "• Property ownership documents (if applicable)\n"
            "• Family ties proof in Uzbekistan\n"
            "• Previous travel history\n"
            "• Invitation letter (if visiting someone)"
        ),
        "application_process": (
            "1. Complete online application at gov.uk/standard-visitor-visa\n"
            "2. Pay visa fee online\n"
            "3. Book appointment at VFS Global (Tashkent)\n"
            "4. Submit biometrics and supporting documents\n"
            "5. Wait for decision (may take several weeks)\n"
            "6. Collect passport with visa vignette"
        ),
        "processing_time": "3–6 weeks (standard)",
        "estimated_costs": (
            "• Visa fee (6 months): £115\n"
            "• VFS service fee: included\n"
            "• Priority service (optional): £500\n"
            "• Total estimate: £115+ (standard)"
        ),
    },
    {
        "country_code": "GB",
        "visa_type_slug": "work",
        "required_documents": (
            "• Valid passport\n"
            "• Certificate of Sponsorship (CoS) from UK employer\n"
            "• TB test certificate\n"
            "• Proof of English language (B1 level minimum)\n"
            "• Bank statement (if required)\n"
            "• Criminal record certificate (for certain jobs)\n"
            "• Professional qualifications\n"
            "• Employment contract details"
        ),
        "application_process": (
            "1. Receive job offer from licensed UK sponsor\n"
            "2. Employer issues Certificate of Sponsorship\n"
            "3. Take TB test if staying 6+ months\n"
            "4. Apply online for Skilled Worker visa\n"
            "5. Pay visa fee and IHS\n"
            "6. Book biometrics at VFS Global\n"
            "7. Receive decision and travel to UK"
        ),
        "processing_time": "3–8 weeks",
        "estimated_costs": (
            "• Visa fee (up to 3 years): £719\n"
            "• IHS: £1,035/year\n"
            "• TB test: ~£50\n"
            "• Skills certificate (if needed): varies\n"
            "• Total estimate: £1,804+ (3-year visa)"
        ),
    },
]
