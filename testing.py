income = 250_000
lowtaxland_rate = 250_000 * 0.05
ripoffland_rate = 250_000 * 0.45    
better_benefits = ripoffland_rate - lowtaxland_rate

print (f"Your income is {income} and you would pay {lowtaxland_rate} income tax in Lowtaxland or {ripoffland_rate} income tax in Ripoffland. You would save {better_benefits} by paying taxes in Lowtaxland")