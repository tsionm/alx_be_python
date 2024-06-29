# User Input: Monthly Income
monthly_income = float(input("Enter your monthly income: "))

# User Input: Monthly Expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Projected Annual Savings (ignoring compounding for simplicity)
annual_interest_rate = 0.05  # 5% annual interest rate (as a decimal)
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Print User's Monthly Savings
print(f"Your monthly savings are ${monthly_savings:.2f}.")

# Print Projected Annual Savings after Interest
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")

