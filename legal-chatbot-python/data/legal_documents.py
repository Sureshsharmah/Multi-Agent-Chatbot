"""
Sample legal document data for the chatbot.
In a production environment, this would be loaded from a database or file system.
"""

LEGAL_DOCUMENTS = [
    {
        "id": "litigation-guide",
        "title": "Guide to Litigation in India",
        "description": "Provides an overview of litigation procedures in India",
        "sections": [
            {
                "id": "litigation-1",
                "title": "Filing a Lawsuit",
                "content": """
                    The process of filing a lawsuit in India involves several steps:
                    
                    1. Preparation of Plaint: The first step is to prepare a plaint, which is a written statement that contains the facts and legal grounds on which the plaintiff (the person filing the lawsuit) is basing their claim. The plaint must include:
                       - The name, description, and place of residence of the plaintiff
                       - The name, description, and place of residence of the defendant
                       - A statement of the facts constituting the cause of action and when it arose
                       - A statement of the value of the subject-matter of the suit for the purposes of jurisdiction and court fees
                       - The relief which the plaintiff claims
                    
                    2. Filing in Court: Once the plaint is prepared, it must be filed in the appropriate court that has jurisdiction over the matter. The jurisdiction depends on:
                       - Territorial jurisdiction: Where the defendant resides or where the cause of action arose
                       - Pecuniary jurisdiction: The value of the subject matter
                       - Subject-matter jurisdiction: The nature of the case
                    
                    3. Payment of Court Fees: Court fees must be paid according to the Court Fees Act and the value of the suit.
                    
                    4. Scrutiny and Registration: The court will scrutinize the plaint to ensure it meets all requirements. If accepted, the plaint will be registered and assigned a case number.
                    
                    5. Issuance of Summons: The court will issue summons to the defendant, informing them of the lawsuit and requiring them to appear before the court.
                    
                    6. Service of Summons: The summons must be served on the defendant, either personally or through registered post.
                    
                    7. Appearance of Defendant: The defendant must appear before the court on the specified date and file a written statement in response to the plaint.
                    
                    8. Framing of Issues: After both parties have presented their initial statements, the court will frame the issues to be decided in the case.
                    
                    9. Trial: Evidence is presented, witnesses are examined, and arguments are heard.
                    
                    10. Judgment: The court delivers its judgment based on the evidence and arguments presented.
                    
                    11. Decree: A formal expression of the judgment is drawn up, known as a decree.
                    
                    12. Execution: If necessary, the decree can be executed to enforce the judgment.
                """
            },
            {
                "id": "litigation-2",
                "title": "Court Hierarchy",
                "content": """
                    The Indian judicial system follows a hierarchical structure:
                    
                    1. Supreme Court of India: The apex court and the final court of appeal. It has original, appellate, and advisory jurisdiction.
                    
                    2. High Courts: Each state has a High Court, which has jurisdiction over the entire state. Some High Courts have jurisdiction over more than one state or union territory.
                    
                    3. District Courts: These are subordinate to the High Courts and are established in each district. They handle both civil and criminal cases.
                    
                    4. Lower Courts: These include Civil Judge Courts (Junior Division and Senior Division) for civil matters and Judicial Magistrate Courts for criminal matters.
                    
                    5. Special Courts: These are established to handle specific types of cases, such as Family Courts, Consumer Courts, and Labor Courts.
                    
                    The hierarchy ensures that if a party is not satisfied with the decision of a lower court, they can appeal to a higher court.
                """
            },
            {
                "id": "litigation-3",
                "title": "Legal Representation",
                "content": """
                    In India, legal representation is primarily provided by advocates who are enrolled with the Bar Council of India or a State Bar Council.
                    
                    1. Types of Advocates:
                       - Senior Advocates: Designated by the Supreme Court or High Courts based on standing and experience
                       - Advocates: Regular practicing lawyers
                       - Advocate-on-Record: Lawyers who are entitled to file cases in the Supreme Court
                    
                    2. Appointment of an Advocate:
                       - A party can appoint an advocate by executing a vakalatnama (power of attorney)
                       - The advocate then represents the party in court proceedings
                    
                    3. Role of an Advocate:
                       - Providing legal advice
                       - Drafting legal documents
                       - Representing clients in court
                       - Negotiating settlements
                    
                    4. Legal Aid:
                       - For those who cannot afford legal representation, legal aid is available through:
                         - Legal Services Authorities at the national, state, and district levels
                         - NGOs and legal aid clinics
                         - Pro bono services offered by advocates
                    
                    5. In-house Counsel:
                       - Companies often have in-house legal departments
                       - In-house counsel provide legal advice to the company and coordinate with external advocates when necessary
                """
            }
        ]
    },
    {
        "id": "corporate-laws",
        "title": "Legal Compliance & Corporate Laws by ICAI",
        "description": "Covers corporate and taxation laws",
        "sections": [
            {
                "id": "corporate-1",
                "title": "Company Formation",
                "content": """
                    Formation of a company in India is governed by the Companies Act, 2013. The process involves:
                    
                    1. Obtaining Digital Signature Certificate (DSC): The proposed directors must obtain DSCs from authorized certifying agencies.
                    
                    2. Obtaining Director Identification Number (DIN): Each proposed director must obtain a DIN by submitting Form DIR-3 to the Ministry of Corporate Affairs (MCA).
                    
                    3. Name Approval: Apply for name approval through the SPICe+ form on the MCA portal. The name should not be identical or similar to an existing company and should not violate the provisions of the Emblems and Names Act.
                    
                    4. Preparation of Memorandum of Association (MOA) and Articles of Association (AOA):
                       - MOA defines the company's relationship with the outside world
                       - AOA governs the internal management of the company
                    
                    5. Filing of Incorporation Documents: Submit the SPICe+ form along with the required documents and fees to the Registrar of Companies (ROC).
                    
                    6. Certificate of Incorporation: Upon satisfaction, the ROC issues a Certificate of Incorporation, which is conclusive evidence of the company's formation.
                    
                    7. Post-Incorporation Compliance:
                       - Obtain Permanent Account Number (PAN) and Tax Deduction Account Number (TAN)
                       - Open a bank account in the company's name
                       - Conduct the first board meeting
                       - Appoint auditors
                       - Issue share certificates to subscribers
                    
                    8. Commencement of Business: File a declaration in Form INC-20A within 180 days of incorporation, confirming that the company has received the minimum subscription amount.
                """
            },
            {
                "id": "corporate-2",
                "title": "Corporate Governance",
                "content": """
                    Corporate Governance in India is regulated by various laws and regulations, primarily the Companies Act, 2013, and SEBI guidelines for listed companies.
                    
                    1. Board of Directors:
                       - Composition: Minimum of 3 directors for public companies and 2 for private companies
                       - Independent Directors: Listed companies and certain public companies must have at least one-third of the board as independent directors
                       - Women Directors: Listed companies and certain public companies must have at least one woman director
                       - Resident Director: At least one director must have stayed in India for at least 182 days in the previous calendar year
                    
                    2. Board Meetings:
                       - Minimum 4 board meetings per year for all companies
                       - Gap between two consecutive meetings should not exceed 120 days
                       - Notice of at least 7 days must be given for board meetings
                       - Quorum: One-third of the total strength or two directors, whichever is higher
                    
                    3. Committees of the Board:
                       - Audit Committee: Mandatory for listed companies and certain public companies
                       - Nomination and Remuneration Committee: Mandatory for listed companies and certain public companies
                       - Stakeholders Relationship Committee: Mandatory for companies with more than 1000 shareholders
                       - Corporate Social Responsibility Committee: Mandatory for companies meeting certain financial thresholds
                    
                    4. Key Managerial Personnel (KMP):
                       - Managing Director/CEO
                       - Company Secretary
                       - Chief Financial Officer
                       - Whole-time Director
                    
                    5. Disclosures and Transparency:
                       - Financial statements
                       - Related party transactions
                       - Remuneration of directors and KMPs
                       - Corporate governance report (for listed companies)
                    
                    6. Audits:
                       - Statutory audit
                       - Internal audit
                       - Secretarial audit
                       - Cost audit (for specified companies)
                    
                    7. Corporate Social Responsibility (CSR):
                       - Companies meeting certain financial thresholds must spend at least 2% of their average net profits on CSR activities
                       - Formulation of CSR policy
                       - Constitution of CSR committee
                       - Disclosure of CSR activities in the annual report
                """
            },
            {
                "id": "corporate-3",
                "title": "Taxation Laws",
                "content": """
                    Taxation laws in India are complex and subject to frequent changes. The main taxes applicable to companies are:
                    
                    1. Income Tax:
                       - Companies are taxed at a flat rate of 30% (domestic companies) or 40% (foreign companies)
                       - Domestic companies can opt for a reduced rate of 22% (plus surcharge and cess) if they forgo certain deductions and exemptions
                       - New manufacturing companies can opt for a rate of 15% (plus surcharge and cess) subject to certain conditions
                       - Minimum Alternate Tax (MAT) at 15% of book profits if the tax liability under normal provisions is less than MAT
                       - Advance tax to be paid in four installments
                       - Annual return to be filed by the due date
                    
                    2. Goods and Services Tax (GST):
                       - Comprehensive indirect tax levied on supply of goods and services
                       - Four rate structure: 5%, 12%, 18%, and 28%
                       - Registration required if turnover exceeds specified limits
                       - Monthly/quarterly returns to be filed
                       - E-way bill for movement of goods
                    
                    3. Tax Deducted at Source (TDS):
                       - Companies must deduct tax at source for specified payments
                       - Rates vary depending on the nature of payment
                       - TDS to be deposited by the 7th of the following month
                       - Quarterly TDS returns to be filed
                       - Annual TDS certificates to be issued
                    
                    4. Dividend Distribution Tax (DDT):
                       - Abolished from FY 2020-21
                       - Dividends now taxable in the hands of recipients
                    
                    5. Transfer Pricing:
                       - International transactions between associated enterprises must be at arm's length
                       - Detailed documentation and reporting requirements
                       - Annual compliance report to be filed
                    
                    6. Equalization Levy:
                       - 2% on consideration received by non-resident e-commerce operators
                       - 6% on specified services
                    
                    7. Tax Incentives:
                       - For startups
                       - For specific industries
                       - For units in special economic zones
                       - For research and development
                    
                    8. Double Taxation Avoidance Agreements (DTAAs):
                       - India has DTAAs with more than 80 countries
                       - Provides relief from double taxation
                       - Reduced withholding tax rates for certain payments
                """
            }
        ]
    }
]