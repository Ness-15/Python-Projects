import requests

def convert_currency(amount, from_currency, to_currency):
    # The API endpoint for currency conversion
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    # Send a GET request to the API endpoint
    response = requests.get(url)

    # Parse the response and extract the conversion rate for the target currency
    data = response.json()
    rate = data["rates"][to_currency]

    # Calculate the converted amount
    converted_amount = round(amount * rate, 2)

    # Return the converted amount as a string
    return str(converted_amount)

# Example usage
amount = 100
from_currency = "USD"
to_currency = "EUR"

converted_amount = convert_currency(amount, from_currency, to_currency)

print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
