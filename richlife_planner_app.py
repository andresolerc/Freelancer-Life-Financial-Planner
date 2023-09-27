# Import necessary libraries
import streamlit as st

# Title of the app
st.title("Freelancer Life Financial Planner")

# Sidebar for user inputs
with st.sidebar:
    st.header("User Inputs")
    st.header("Costs passed in the hourly rate")
    
    # Income
    base_hourly_rate = st.number_input("Enter your desired net hourly rate (€)", value=96.15, step=0.5)
    include_vakantiegeld = st.checkbox("Include Vakantiegeld (8%)")
    include_13th_month = st.checkbox("Include 13th Month (8.33%)")
    include_pension_contribution = st.checkbox("Include Pension Contribution")
    pension_percentage = st.slider("Pension Contribution (%)", 0, 20, 10) if include_pension_contribution else 0
    
    # Adjust hourly rate based on checkboxes
    adjustments = 1
    if include_vakantiegeld:
        adjustments += 0.08
    if include_13th_month:
        adjustments += 0.0833
    if include_pension_contribution:
        adjustments += pension_percentage / 100.0

    adjusted_hourly_rate = base_hourly_rate * adjustments
    
    hours_per_week = st.number_input("Hours worked per week", value=20.0, step=1.0)
    weeks_per_year = st.number_input("Weeks worked per year", value=52.0, step=1.0)

    # Insurance
    st.subheader("Insurance")
    liability_insurance = st.number_input("Professional Liability Insurance (€/year)", value=605.0, step=10.0)
    disability_insurance = st.number_input("Disability Insurance (€/year)", value=2988.0, step=10.0)
    legal_insurance = st.number_input("Legal Insurance (€/year)", value=346.0, step=10.0)
    equipment_insurance = st.number_input("Equipment Insurance (€/year)", value=144.0, step=10.0)
    health_insurance = st.number_input("Health Insurance (€/year)", value=1500.0, step=10.0)

    include_insurance_in_rate = st.checkbox("Include insurance costs in hourly rate to client?")

    total_insurance = liability_insurance + disability_insurance + legal_insurance + equipment_insurance +  health_insurance

    if include_insurance_in_rate:
        insurance_per_hour = total_insurance / (hours_per_week * weeks_per_year)
        adjusted_hourly_rate += insurance_per_hour

    # Equipment and Mobile Subscription Costs
    st.subheader("Equipment and Mobile Subscription Costs")
    macbook_pro_cost = st.number_input("MacBook Pro Cost (€)", value=3500.0, step=100.0)
    iphone_cost = st.number_input("iPhone Cost (€)", value=1855.0, step=100.0)
    mobile_subscription = st.number_input("Mobile Subscription (€/month)", value=36.0, step=1.0)
    office_subscription = st.number_input("Office Subscription (€/month)", value=143.0, step=1.0)
    include_equipment_in_rate = st.checkbox("Include equipment and subscription costs in hourly rate to client?")
    
    total_equipment_cost = macbook_pro_cost + iphone_cost
    total_subscription_cost = mobile_subscription + office_subscription * 12
    #total_office_subscription = office_subscription * 12
    
    if include_equipment_in_rate:
        equipment_per_hour = total_equipment_cost / (hours_per_week * weeks_per_year)
        subscription_per_hour = total_subscription_cost / (hours_per_week * weeks_per_year)
        adjusted_hourly_rate += equipment_per_hour + subscription_per_hour

    # Business Expenses Online Platforms
    st.subheader("Business Expenses Online Platforms")
    website_hosting = st.number_input("Website Hosting + Domain (€/year)", value=150.0, step=10.0)
    email_marketing = st.number_input("Email Marketing (€/year)", value=200.0, step=10.0)
    advertising = st.number_input("Advertising (€/year)", value=500.0, step=50.0)
    seo_tools = st.number_input("SEO Tools (€/year)", value=300.0, step=25.0)
    crm_invoicing = st.number_input("CRM & Invoicing (€/year)", value=250.0, step=25.0)
    include_expenses_in_rate = st.checkbox("Include business expenses in hourly rate to client?")

    total_expenses = website_hosting + email_marketing + advertising + seo_tools + crm_invoicing

    if include_expenses_in_rate:
        expenses_per_hour = total_expenses / (hours_per_week * weeks_per_year)
        adjusted_hourly_rate += expenses_per_hour

    # Banking Costs
    st.subheader("Banking Costs")
    monthly_account_fee = st.number_input("Monthly Account Fee (€/month)", value=6.0, step=1.0)
    transaction_fees = st.number_input("Transaction Fees (€/year)", value=50.0, step=5.0)
    business_credit_card = st.number_input("Business Credit Card (€/year)", value=30.0, step=5.0)
    include_banking_in_rate = st.checkbox("Include banking costs in hourly rate to client?")

    total_banking = (monthly_account_fee * 12) + transaction_fees + business_credit_card

    if include_banking_in_rate:
        banking_per_hour = total_banking / (hours_per_week * weeks_per_year)
        adjusted_hourly_rate += banking_per_hour

    st.header("Deductions on the net income after tax")

    # Emergency Fund
    st.subheader("Emergency Fund")
    emergency_fund_percentage = st.slider("Emergency Fund (%)", 0, 20, 5)
    
    # Professional Development
    st.subheader("Professional Development")
    professional_development = st.number_input("Professional Development (€/year)", value=2000.0, step=100.0)

    # Retirement Savings
    st.subheader("Retirement Savings")
    bux_etf_investment = st.slider("Bux ETF Investment (%)", 0, 20, 5)
    crypto_investment = st.slider("Crypto Bitcoin Investment (%)", 0, 20, 5)

    # Living Expenses
    st.subheader("Living Expenses")
    food_expense = st.number_input("Food (€/month)", value=700.0, step=50.0)
    rent_expense = st.number_input("Rent (€/month)", value=1000.0, step=50.0)
    house_services = st.number_input("House Services (€/month)", value=50.0, step=5.0)
    public_transport = st.number_input("Public Transport (€/month)", value=100.0, step=10.0)
    fitness = st.number_input("Fitness (€/month)", value=200.0, step=10.0)


# Main area for outputs and tables
st.header("Financial Overview")
st.header("Costs passed in the hourly rate")

# Calculate results
annual_income = adjusted_hourly_rate * hours_per_week * weeks_per_year
total_insurance = liability_insurance + disability_insurance + legal_insurance + equipment_insurance

# Calculate tax based on brackets
if annual_income <= 73031:
    tax_lower_bracket = annual_income * 0.3693
    tax_upper_bracket = 0
else:
    tax_lower_bracket = 73031 * 0.3693
    tax_upper_bracket = (annual_income - 73031) * 0.495

# Calculate total tax and net income after tax
total_tax = tax_lower_bracket + tax_upper_bracket
net_income_after_tax = annual_income - total_tax

# Calculate monthly and hourly net income
net_income_per_month = net_income_after_tax / 12
net_income_per_hour = net_income_after_tax / (hours_per_week * weeks_per_year)

# Calculate emergency fund and professional development costs
emergency_fund = net_income_after_tax * (emergency_fund_percentage / 100.0)
professional_development_cost = professional_development
# Calculate retirement savings
bux_etf_savings = net_income_after_tax * (bux_etf_investment / 100.0)
crypto_savings = net_income_after_tax * (crypto_investment / 100.0)
# Calculate living expenses
living_expenses = (food_expense + rent_expense + house_services + public_transport + fitness) * 12


# Display results
st.write(f"Annual Income (Including Adjustments): €{annual_income:,.2f}")
st.write(f"Hourly Rate to Charge Client (Excluding VAT 21%): €{adjusted_hourly_rate:,.2f}")
#st.write(f"Total Insurance Costs: €{total_insurance:,.2f}")

# Display tax for both brackets
st.write(f"Income Tax to be Paid (Up to €73,031 at 36.93%): €{tax_lower_bracket:,.2f}")
st.write(f"Income Tax to be Paid (Above €73,031 at 49.5%): €{tax_upper_bracket:,.2f}")

# Display net income after tax
st.write(f"Net Income After Tax: €{net_income_after_tax:,.2f}")
st.write(f"Net Income After Tax (Monthly): €{net_income_per_month:,.2f}")
st.write(f"Net Income After Tax (Hourly): €{net_income_per_hour:,.2f}")

st.header("Deductions on the net income after tax")

# Display individual deductions
st.write(f"Emergency Fund: €{emergency_fund:,.2f}")
st.write(f"Professional Development: €{professional_development_cost:,.2f}")
# Display individual retirement savings
st.write(f"Bux ETF Investment: €{bux_etf_savings:,.2f}")
st.write(f"Crypto Bitcoin Investment: €{crypto_savings:,.2f}")
# Display living expenses
st.write(f"Living Expenses: €{living_expenses:,.2f}")


# Calculate and display remaining net income after all deductions
remaining_net_income_after_all_deductions = net_income_after_tax - (emergency_fund + professional_development_cost + bux_etf_savings + crypto_savings + living_expenses)
st.write(f"Remaining Net Income After All Deductions: €{remaining_net_income_after_all_deductions:,.2f}")


# Run the app using: streamlit run app_name.py
