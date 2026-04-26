

"""
All regulatory limits are hardcoded and may not be up to date with current regulations
ONLY for Canada and English documents
"""
# ---- FEDERAL Criminal Code of Canada s.347(2)----
CRIMINAL_USURY_APR = 60.0

# ---- BC BPCPA PAYDAY LOANS REGULATION----
BC_PAYDAY_MAX_FEE_PER_100 = 14.00
BC_PAYDAY_MAX_LOAN_AMOUNT = 1500.00
BC_PAYDAY_MAX_TERM_LENGTH_IN_DAYS = 62
# A lender can only charge this once per loan
BC_MAX_NSF_FEE = 20.0
# You can cancel for any reason without penalty within this window
BC_CANCEL_WINDOW = 2.0
# Lenders are prohibited from provided a second loan while one is still outstanding
BC_CONCURRENT_LOANS_ALLOWED = False
# A lender cannot roll over the balance of an old loan into a new one or change a fee to extend the loan
BC_ROLLOVERS_ALLOWED = False

# ---- ONTARIO ----
ON_MAX_FEE_PER_100 = 15.0
# Lenders are prohibited from provided a second loan while one is still outstanding
ON_CONCURRENT_LOANS_ALLOWED = False
# A lender cannot roll over the balance of an old loan into a new one or change a fee to extend the loan
ON_ROLLOVERS_ALLOWED = False

# ---- CAUSE FLAGS ----
CLAUSE_FLAGS = {"MANDATORY_ARBITRATION": {"flag": True, "severity": "critical"},
               "WAGE_ASSIGNMENT": {"flag": True, "severity": "critical"},
               "CONFESSED_JUDGMENT": {"flag": True, "severity": "critical"},
               "BALLOON_PAYMENTS": {"flag": True, "severity": "critical"}}

# Only Quebec is exempt from section 347
EXEMPT_PROVINCES_FROM_SECTION_THREE_FOURTY_SEVEN = {"British Columbia",
                                                    "Alberta",
                                                    "Saskatchewan",
                                                    "Manitoba",
                                                    "Ontario",
                                                    "New Brunswick",
                                                    "Nova Scotia",
                                                    "Prince Edward Island",
                                                    "Newfoundland and Labrador"}
PROVINCE_MAP = {
    "BC": "British Columbia",
    "AB": "Alberta",
    "SK": "Saskatchewan",
    "MB": "Manitoba",
    "ON": "Ontario",
    "QC": "Quebec",
    "NB": "New Brunswick",
    "NS": "Nova Scotia",
    "PE": "Prince Edward Island",
    "NL": "Newfoundland and Labrador",
}