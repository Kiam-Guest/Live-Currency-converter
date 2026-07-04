import re
import requests

#converter works with the following currencies
# Additional currencies can be added to the allowed set by including the 3 letter currency code in the ALLOWED.
# It would be best practise to also update user facing messages to reflect new currency options, however this will not break the code.
#A full list of supported currencies can be found at: https://frankfurter.dev/currencies/
ALLOWED = {"GBP", "USD", "EUR", "CAD", "AUD"}


#Splits the user input.
#This allows the user to either input the entire amount and currency in one go,
#  or to input the amount and then be prompted for the currency separately.
def parse_amount_and_currency(user_input):
    user_input = user_input.strip().upper()

    match = re.fullmatch(r"(\d+(?:\.\d+)?)\s*([A-Z]{3})?", user_input)
    if not match:
        raise ValueError("Enter a value like 100, 100 GBP, or 100GBP")

    amount = float(match.group(1))
    currency = match.group(2)

    return amount, currency

#Calls API and calculates results.
def convert_currency(amount, from_currency, to_currency):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in ALLOWED or to_currency not in ALLOWED:
        raise ValueError("Only GBP, USD, EUR, CAD, AUD are allowed.")

    if from_currency == to_currency:
        return {
            "from": from_currency,
            "to": to_currency,
            "amount": amount,
            "rate": 1.0,
            "converted": amount
        }
#API where conversion rates are pulled from.  No API key required.  Can be changed to another provider.
    url = "https://api.frankfurter.dev/v1/latest"
    params = {
        "base": from_currency,
        "symbols": to_currency
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    if "rates" not in data or to_currency not in data["rates"]:
        raise ValueError(f"Unexpected API response: {data}")

    rate = data["rates"][to_currency]
    converted = amount * rate
#Tidies the data into a dictionary for easy access and printing.
    return {
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "rate": rate,
        "converted": converted,
        "date": data.get("date")
    }

#Main program loop.  This is where the user is prompted for input and the results are printed.
if __name__ == "__main__":
    first_input = input("Enter amount (e.g. 100 or 100GBP): ")

    amount, from_currency = parse_amount_and_currency(first_input)

    if not from_currency:
        from_currency = input("From (GBP/USD/EUR/CAD/AUD): ").strip().upper()

    to_currency = input("To (GBP/USD/EUR/CAD/AUD): ").strip().upper()

    result = convert_currency(amount, from_currency, to_currency)

    print(f"{result['amount']} {result['from']} = {result['converted']:.2f} {result['to']}")
    print(f"Rate: {result['rate']:.4f}")
    print(f"Date: {result['date']}")