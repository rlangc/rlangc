# Predefined exchange rates (example rates)
exchange_rates = {
    'USD': {'EUR': 0.91, 'GBP': 0.76, 'INR': 83.00},
    'EUR': {'USD': 1.10, 'GBP': 0.84, 'INR': 91.00},
    'GBP': {'USD': 1.32, 'EUR': 1.19, 'INR': 109.00},
    'INR': {'USD': 0.012, 'EUR': 0.011, 'GBP': 0.0092}
}

def show_currencies():
    """Display available currencies."""
    print("\nAvailable currencies:", ', '.join(exchange_rates.keys()))

def convert_currency(amount, from_currency, to_currency):
    """Convert amount from one currency to another using exchange rates."""
    try:
        rate = exchange_rates[from_currency][to_currency]
        return round(amount * rate, 2)
    except KeyError:
        return None

def main():
    print("Welcome to the Currency Converter!")
    
    while True:
        show_currencies()
        
        from_currency = input("Enter the currency you have (e.g. USD, EUR): ").upper()
        if from_currency not in exchange_rates:
            print("Invalid currency. Please choose from the available options.")
            continue
        
        to_currency = input("Enter the currency to convert to (e.g. GBP, INR): ").upper()
        if to_currency not in exchange_rates[from_currency]:
            print("Invalid conversion option. Please choose from the available options.")
            continue
        
        try:
            amount = float(input(f"Enter the amount in {from_currency}: "))
            if amount <= 0:
                print("Please enter a positive amount.")
                continue
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue
        
        converted_amount = convert_currency(amount, from_currency, to_currency)
        if converted_amount is not None:
            print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}.")
        else:
            print("Currency conversion failed. Please try again.")

        another_conversion = input("Would you like to perform another conversion? (yes/no): ").strip().lower()
        if another_conversion != 'yes':
            break
    
    print("Thank you for using the Currency Converter!")

if __name__ == "__main__":
    main()