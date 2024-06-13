# Given income
income = 250000

# Tax rates for Lowtaxland and Ripoffland
lowtaxland_rate = 0.05
ripoffland_rate = 0.43

# Calculating the tax amounts
tax_lowtaxland = income * lowtaxland_rate
tax_ripoffland = income * ripoffland_rate

# Calculating the difference in tax amounts
tax_difference = tax_ripoffland - tax_lowtaxland

# Printing the required output
print(f"Your income is {income} and you would pay {tax_lowtaxland} income tax in Lowtaxland or {tax_ripoffland} income tax in Ripoffland. You would save {tax_difference} by paying taxes in Lowtaxland!")
