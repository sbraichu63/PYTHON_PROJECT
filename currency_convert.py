def currency_converter(amount, rate):
    return amount * rate

try:
    amount = float(input("Enter the amount: "))
    from_currency = input("From currency (e.g., USD, INR, EUR): ").upper()
    to_currency = input("To currency (e.g., USD, INR, EUR): ").upper()
    rate = float(input(f"Enter the conversion rate from {from_currency} to {to_currency}: "))
    result = currency_converter(amount, rate)
    print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
except Exception as e:
    print("Invalid input.")
