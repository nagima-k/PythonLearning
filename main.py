import requests

base_currency = input("Enter the base currency: ")
target_currency = input("Enter the currency you want to convert: ")
amount = input(f"Enter the amount of {base_currency} you want to convert: ")
url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"


response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    base_currency_rate = data["rates"][target_currency]

    print("It's -->  " + str(float(amount) * base_currency_rate)+str(target_currency))