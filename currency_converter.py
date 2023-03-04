import sys
import requests
import colorama
from datetime import datetime
from colorama import Fore, Back
colorama.init(autoreset=True)


def convert_currency():
    print()
    print(Fore.YELLOW + " <<< CURRENCY CONVERTER >>> ")
    print()
    user_currency = input(Fore.CYAN + " Enter your currency: ")
    target_currency = input(Fore.CYAN + " Enter target currency: ")

    while True:
        try:
            amount = float(input(Fore.YELLOW + " Enter amount: "))
        except:
            print(' The amount must be a numeric value!')
            continue

        if not amount > 0:
            print(' The amount must be greater than 0')
            continue
        else:
            break

    url = ('https://api.apilayer.com/fixer/convert?to='
          + target_currency + '&from=' + user_currency +
          '&amount=' + str(amount))
    
    payload = {}
    headers = {"apikey": "Re35bKIFhwFN1IqYC6D4skJUhoa5GS4R"}
    response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code

    if status_code != 200:
        print(' Uh oh, there was a problem. Please try again later')
        quit()

    result = response.json()
    print(Fore.GREEN + ' Conversion result: ' + str(result['result']))


convert_currency()