import math

def round(amount):
    return math.floor(amount + 0.5)

def calculate_tax_14to15(amount):
    tax_amount = 0
    if amount > 400000 and amount <= 750000:
        amount -= 400000
        tax_amount = amount * 0.05
    elif amount > 750000 and amount <= 1400000:
        amount -= 750000
        tax_amount = 17500 + amount * 0.1
    elif amount > 1400000 and amount <= 1500000:
        amount -= 1400000
        tax_amount = 82500 + amount * 0.125
    elif amount > 1500000 and amount <= 1800000:
        amount -= 1500000
        tax_amount = 95000 + amount * 0.15
    elif amount > 1800000 and amount <= 2500000:
        amount -= 1800000
        tax_amount = 140000 + amount * 0.175
    elif amount > 2500000 and amount < 3000000:
        amount -= 2500000
        tax_amount = 262500 + amount * 0.2
    elif amount > 3000000 and amount < 3500000:
        amount -= 3000000
        tax_amount = 362500 + amount * 0.225
    elif amount > 3500000 and amount < 4000000:
        amount -= 3500000
        tax_amount = 475000 + amount * 0.25
    elif amount > 4000000 and amount < 7000000:
        amount -= 4000000
        tax_amount = 600000 + amount * 0.275
    elif amount > 7000000:
        amount -= 7000000
        tax_amount = 1425000 + amount * 0.3

    return round(tax_amount)

def calculate_tax_15to16(amount):
    tax_amount = 0
    if amount > 400000 and amount <= 500000:
        amount -= 400000
        tax_amount = amount * 0.02
    elif amount > 500000 and amount <= 750000:
        amount -= 500000
        tax_amount = 2000 + amount * 0.05
    elif amount > 750000 and amount <= 1400000:
        amount -= 750000
        tax_amount = 14500 + amount * 0.1
    elif amount > 1400000 and amount <= 1500000:
        amount -= 1400000
        tax_amount = 79500 + amount * 0.125
    elif amount > 1500000 and amount <= 1800000:
        amount -= 1500000
        tax_amount = 92000 + amount * 0.15
    elif amount > 1800000 and amount < 2500000:
        amount -= 1800000
        tax_amount = 137000 + amount * 0.175
    elif amount > 2500000 and amount < 3000000:
        amount -= 2500000
        tax_amount = 259500 + amount * 0.2
    elif amount > 3000000 and amount < 3500000:
        amount -= 3000000
        tax_amount = 359500 + amount * 0.225
    elif amount > 3500000 and amount < 4000000:
        amount -= 3500000
        tax_amount = 472000 + amount * 0.25
    elif amount > 4000000 and amount < 7000000:
        amount -= 4000000
        tax_amount = 597000 + amount * 0.275
    elif amount > 7000000:
        amount -= 7000000
        tax_amount = 1422000 + amount * 0.3

    return round(tax_amount)

def calculate_tax_16to17(amount):
    tax_amount = 0
    if amount > 400000 and amount <= 500000:
        amount -= 400000
        tax_amount = amount * 0.02
    elif amount > 500000 and amount <= 750000:
        amount -= 500000
        tax_amount = 2000 + amount * 0.05
    elif amount > 750000 and amount <= 1400000:
        amount -= 750000
        tax_amount = 14500 + amount * 0.1
    elif amount > 1400000 and amount <= 1500000:
        amount -= 1400000
        tax_amount = 79500 + amount * 0.125
    elif amount > 1500000 and amount <= 1800000:
        amount -= 1500000
        tax_amount = 92000 + amount * 0.15
    elif amount > 1800000 and amount < 2500000:
        amount -= 1800000
        tax_amount = 137000 + amount * 0.175
    elif amount > 2500000 and amount < 3000000:
        amount -= 2500000
        tax_amount = 259500 + amount * 0.2
    elif amount > 3000000 and amount < 3500000:
        amount -= 3000000
        tax_amount = 359500 + amount * 0.225
    elif amount > 3500000 and amount < 4000000:
        amount -= 3500000
        tax_amount = 472000 + amount * 0.25
    elif amount > 4000000 and amount < 7000000:
        amount -= 4000000
        tax_amount = 597000 + amount * 0.275
    elif amount > 7000000:
        amount -= 7000000
        tax_amount = 1422000 + amount * 0.3

    return round(tax_amount)

def calculate_tax_17to18(amount):
    tax_amount = 0
    if amount > 400000 and amount <= 500000:
        amount -= 400000
        tax_amount = amount * 0.02
    elif amount > 500000 and amount <= 750000:
        amount -= 500000
        tax_amount = 2000 + amount * 0.05
    elif amount > 750000 and amount <= 1400000:
        amount -= 750000
        tax_amount = 14500 + amount * 0.1
    elif amount > 1400000 and amount <= 1500000:
        amount -= 1400000
        tax_amount = 79500 + amount * 0.125
    elif amount > 1500000 and amount <= 1800000:
        amount -= 1500000
        tax_amount = 92000 + amount * 0.15
    elif amount > 1800000 and amount < 2500000:
        amount -= 1800000
        tax_amount = 137000 + amount * 0.175
    elif amount > 2500000 and amount < 3000000:
        amount -= 2500000
        tax_amount = 259500 + amount * 0.2
    elif amount > 3000000 and amount < 3500000:
        amount -= 3000000
        tax_amount = 359500 + amount * 0.225
    elif amount > 3500000 and amount < 4000000:
        amount -= 3500000
        tax_amount = 472000 + amount * 0.25
    elif amount > 4000000 and amount < 7000000:
        amount -= 4000000
        tax_amount = 597000 + amount * 0.275
    elif amount > 7000000:
        amount -= 7000000
        tax_amount = 1422000 + amount * 0.3

    return round(tax_amount)

def calculate_tax_18to19(amount):
    tax_amount = 0
    if amount > 400000 and amount <= 800000:
        tax_amount = 1000
    elif amount > 800000 and amount <= 1200000:
        tax_amount = 2000
    elif amount > 1200000 and amount <= 2500000:
        amount -= 1200000
        tax_amount1 = amount * 0.05
        tax_amount2 = 2000
        tax_amount = tax_amount1 if tax_amount1 > tax_amount2 else tax_amount2
    elif amount > 2500000 and amount <= 4000000:
        amount -= 2500000
        tax_amount = 65000 + amount * 0.15
    elif amount > 4000000 and amount <= 8000000:
        amount -= 4000000
        tax_amount = 290000 + amount * 0.2
    elif amount > 8000000:
        amount -= 8000000
        tax_amount = 1090000 + amount * 0.25

    return round(tax_amount)

def calculate_tax_19to20(amount):
    tax_amount = 0
    if amount > 600000 and amount <= 1200000:
        amount -= 600000
        tax_amount = amount * 0.05
    elif amount > 1200000 and amount <= 1800000:
        amount -= 1200000
        tax_amount = 30000 + amount * 0.10
    elif amount > 1800000 and amount <= 2500000:
        amount -= 1800000
        tax_amount = 90000 + amount * 0.15
    elif amount > 2500000 and amount <= 3500000:
        amount -= 2500000
        tax_amount = 195000 + amount * 0.175
    elif amount > 3500000 and amount <= 5000000:
        amount -= 3500000
        tax_amount = 370000 + amount * 0.2
    elif amount > 5000000 and amount <= 8000000:
        amount -= 5000000
        tax_amount = 670000 + amount * 0.225
    elif amount > 8000000 and amount <= 12000000:
        amount -= 8000000
        tax_amount = 1345000 + amount * 0.25
    elif amount > 12000000 and amount <= 30000000:
        amount -= 12000000
        tax_amount = 2345000 + amount * 0.275
    elif amount > 30000000 and amount <= 50000000:
        amount -= 30000000
        tax_amount = 7295000 + amount * 0.30
    elif amount > 50000000 and amount <= 75000000:
        amount -= 50000000
        tax_amount = 13295000 + amount * 0.325
    elif amount > 75000000:
        amount -= 75000000
        tax_amount = 21420000 + amount * 0.35

    return round(tax_amount)

def calculate_tax_20to21(amount):
    tax_amount = 0
    if amount > 600000 and amount <= 1200000:
        amount -= 600000
        tax_amount = amount * 0.05
    elif amount > 1200000 and amount <= 1800000:
        amount -= 1200000
        tax_amount = 30000 + amount * 0.10
    elif amount > 1800000 and amount <= 2500000:
        amount -= 1800000
        tax_amount = 90000 + amount * 0.15
    elif amount > 2500000 and amount <= 3500000:
        amount -= 2500000
        tax_amount = 195000 + amount * 0.175
    elif amount > 3500000 and amount <= 5000000:
        amount -= 3500000
        tax_amount = 370000 + amount * 0.2
    elif amount > 5000000 and amount <= 8000000:
        amount -= 5000000
        tax_amount = 670000 + amount * 0.225
    elif amount > 8000000 and amount <= 12000000:
        amount -= 8000000
        tax_amount = 1345000 + amount * 0.25
    elif amount > 12000000 and amount <= 30000000:
        amount -= 12000000
        tax_amount = 2345000 + amount * 0.275
    elif amount > 30000000 and amount <= 50000000:
        amount -= 30000000
        tax_amount = 7295000 + amount * 0.30
    elif amount > 50000000 and amount <= 75000000:
        amount -= 50000000
        tax_amount = 13295000 + amount * 0.325
    elif amount > 75000000:
        amount -= 75000000
        tax_amount = 21420000 + amount * 0.35

    return round(tax_amount)

def calculate_tax_21to22(amount):
    tax_amount = 0
    if amount > 600000 and amount <= 1200000:
        amount -= 600000
        tax_amount = amount * 0.05
    elif amount > 1200000 and amount <= 1800000:
        amount -= 1200000
        tax_amount = 30000 + amount * 0.10
    elif amount > 1800000 and amount <= 2500000:
        amount -= 1800000
        tax_amount = 90000 + amount * 0.15
    elif amount > 2500000 and amount <= 3500000:
        amount -= 2500000
        tax_amount = 195000 + amount * 0.175
    elif amount > 3500000 and amount <= 5000000:
        amount -= 3500000
        tax_amount = 370000 + amount * 0.2
    elif amount > 5000000 and amount <= 8000000:
        amount -= 5000000
        tax_amount = 670000 + amount * 0.225
    elif amount > 8000000 and amount <= 12000000:
        amount -= 8000000
        tax_amount = 1345000 + amount * 0.25
    elif amount > 12000000 and amount <= 30000000:
        amount -= 12000000
        tax_amount = 2345000 + amount * 0.275
    elif amount > 30000000 and amount <= 50000000:
        amount -= 30000000
        tax_amount = 7295000 + amount * 0.30
    elif amount > 50000000 and amount <= 75000000:
        amount -= 50000000
        tax_amount = 13295000 + amount * 0.325
    elif amount > 75000000:
        amount -= 75000000
        tax_amount = 21420000 + amount * 0.35

    return round(tax_amount)

def calculate_tax_23to24(amount):
    tax_amount = 0
    if amount > 600000 and amount <= 1200000:
        amount -= 600000
        tax_amount = amount * 0.025
    elif amount > 1200000 and amount <= 2400000:
        amount -= 1200000
        tax_amount = 15000 + amount * 0.125
    elif amount > 2400000 and amount <= 3600000:
        amount -= 2400000
        tax_amount = 165000 + amount * 0.225
    elif amount > 3600000 and amount <= 6000000:
        amount -= 3600000
        tax_amount = 435000 + amount * 0.275
    elif amount > 6000000:
        amount -= 6000000
        tax_amount = 1095000 + amount * 0.35
    return round(tax_amount)

def calculate_tax_22to23(amount):
    tax_amount = 0
    if amount > 600000 and amount <= 1200000:
        amount -= 600000
        tax_amount = amount * 0.025
    elif amount > 1200000 and amount <= 2400000:
        amount -= 1200000
        tax_amount = 15000 + amount * 0.125
    elif amount > 2400000 and amount <= 3600000:
        amount -= 2400000
        tax_amount = 165000 + amount * 0.2
    elif amount > 3600000 and amount <= 6000000:
        amount -= 3600000
        tax_amount = 405000 + amount * 0.25
    elif amount > 6000000 and amount <= 12000000:
        amount -= 6000000
        tax_amount = 1005000 + amount * 0.325
    elif amount > 12000000:
        amount -= 12000000
        tax_amount = 2955000 + amount * 0.35

    return round(tax_amount)

def calculate_tax_24to25(amount):
    tax_amount = 0
    if amount > 600000 and amount <= 1200000:
        amount -= 600000
        tax_amount = amount * 0.05
    elif amount > 1200000 and amount <= 2200000:
        amount -= 1200000
        tax_amount = 30000 + amount * 0.15
    elif amount > 2200000 and amount <= 3200000:
        amount -= 2200000
        tax_amount = 180000 + amount * 0.25
    elif amount > 3200000 and amount <= 4100000:
        amount -= 3200000
        tax_amount = 430000 + amount * 0.3
    elif amount > 4100000:
        amount -= 4100000
        tax_amount = 700000 + amount * 0.35
    return round(tax_amount)

def calculate_tax_25to26(amount):
    original_amount = amount
    tax_amount = 0
    if amount > 600000 and amount <= 1200000:
        amount -= 600000
        tax_amount = amount * 0.01
    elif amount > 1200000 and amount <= 2200000:
        amount -= 1200000
        tax_amount = 6000 + amount * 0.11
    elif amount > 2200000 and amount <= 3200000:
        amount -= 2200000
        tax_amount = 116000 + amount * 0.23
    elif amount > 3200000 and amount <= 4100000:
        amount -= 3200000
        tax_amount = 346000 + amount * 0.30
    elif amount > 4100000:
        amount -= 4100000
        tax_amount = 616000 + amount * 0.35

    if original_amount > 10000000:
        tax_amount = tax_amount * 1.09

    return round(tax_amount)

def input_updated(year_select, monthly_salary):
    if not year_select or year_select == "2025-2026":
        tax_amount = calculate_tax_25to26(monthly_salary * 12)
    elif not year_select or year_select == "2024-2025":
        tax_amount = calculate_tax_24to25(monthly_salary * 12)
    elif year_select == "2023-2024":
        tax_amount = calculate_tax_23to24(monthly_salary * 12)
    elif year_select == "2022-2023":
        tax_amount = calculate_tax_22to23(monthly_salary * 12)
    elif year_select == "2014-2015":
        tax_amount = calculate_tax_14to15(monthly_salary * 12)
    elif year_select == "2015-2016":
        tax_amount = calculate_tax_15to16(monthly_salary * 12)
    elif year_select == "2016-2017":
        tax_amount = calculate_tax_16to17(monthly_salary * 12)
    elif year_select == "2017-2018":
        tax_amount = calculate_tax_17to18(monthly_salary * 12)
    elif year_select == "2018-2019":
        tax_amount = calculate_tax_18to19(monthly_salary * 12)
    elif year_select == "2019-2020":
        tax_amount = calculate_tax_19to20(monthly_salary * 12)
    elif year_select == "2020-2021":
        tax_amount = calculate_tax_20to21(monthly_salary * 12)
    elif year_select == "2021-2022":
        tax_amount = calculate_tax_21to22(monthly_salary * 12)
    
    # Calculate all values
    monthly_salary_val = monthly_salary if not math.isnan(monthly_salary) else 0
    monthly_tax_val = round(tax_amount / 12) if not math.isnan(tax_amount) else 0
    salary_after_tax_val = (monthly_salary_val - monthly_tax_val) if not math.isnan((monthly_salary_val - monthly_tax_val)) else 0
    yearly_salary_val = round(monthly_salary_val * 12) if not math.isnan(round(monthly_salary_val * 12)) else 0
    yearly_income_after_tax_val = (yearly_salary_val - tax_amount) if not math.isnan((yearly_salary_val - tax_amount)) else 0
    yearly_tax_val = tax_amount if not math.isnan(tax_amount) else 0
    
    # Return as a dictionary
    return {
        "monthly_salary": monthly_salary_val,
        "monthly_tax": monthly_tax_val,
        "salary_after_tax": salary_after_tax_val,
        "yearly_salary": yearly_salary_val,
        "yearly_income_after_tax": yearly_income_after_tax_val,
        "yearly_tax": yearly_tax_val
    }