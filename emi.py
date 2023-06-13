from decimal import Decimal, ROUND_HALF_UP

def calculate_emi(principal, interest_rate, tenure):
    # Convert interest rate from percentage to decimal
    interest_rate = Decimal(interest_rate) / Decimal(100)

    # Calculate monthly interest rate
    monthly_interest_rate = interest_rate / Decimal(12)

    # Calculate the number of monthly installments
    num_installments = Decimal(tenure) * Decimal(12)

    # Calculate the EMI using the formula
    emi = (principal * monthly_interest_rate * (Decimal(1) + monthly_interest_rate) ** num_installments) / ((Decimal(1) + monthly_interest_rate) ** num_installments - Decimal(1))

    # Round the EMI to 2 decimal places
    emi = emi.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)

    return emi

# Get user input
principal = Decimal(input("Enter the loan amount: "))
interest_rate = Decimal(input("Enter the annual interest rate (%): "))
tenure = int(input("Enter the loan tenure (in years): "))

emi = calculate_emi(principal, interest_rate, tenure)
total_amount = emi * (Decimal(tenure) * Decimal(12))
total_interest_amount = total_amount - principal

# Print the results
print("============================================")
print("Monthly EMI:", emi)
print("Total Amount to be Paid:", total_amount)
print("Total Interest Amount Paid:", total_interest_amount)
print("============================================")