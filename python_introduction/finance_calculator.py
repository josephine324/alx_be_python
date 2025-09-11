# finance_calculator.py

# Get user input
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate annual savings (before interest)
annual_savings = monthly_savings * 12

# Add 5% interest
projected_savings = annual_savings + (annual_savings * 0.05)

# Display results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")

