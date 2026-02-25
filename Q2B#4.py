principal = float(input("Enter initial amount: "))
years = int(input("Enter number of years: "))
rate_percent = float(input("Enter interest rate (percent per year): "))

rate = rate_percent / 100

amount = principal

for year in range(1, years + 1):
    amount = amount + (amount * rate)

print(f"At the end of {years} years, you will have {amount:.2f} dollars.")