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
    if __name__ == "__main__":

        while(1):
            user_currency = input(Fore.CYAN + " Enter your currency: ")
            target_currency = input(Fore.CYAN + " Enter target currency: ")

            while True:
                try:
                    amount = float(input(Fore.YELLOW + " Enter amount: "))
                except:
                    print(Fore.BLACK + Back.RED + " The amount must be a numeric value! ")
                    print()
                    continue

                if not amount > 0:
                    print(Fore.BLACK + Back.RED + " The amount must be greater than 0 ")
                    print()
                    continue
                else:
                    break

            url = ("https://api.apilayer.com/fixer/convert?to="
                + target_currency + '&from=' + user_currency +
                '&amount=' + str(amount))
            
            payload = {}
            headers = {"apikey": "YOUR API KEY"}
            response = requests.request("GET", url, headers=headers, data=payload)
            status_code = response.status_code
            trgt_crrncy = target_currency.upper()

            if status_code != 200:
                print(Fore.BLACK + Back.RED + " There was an error. Please try again later ")
                print()
                quit()

            result = response.json()
            print()
            print(Fore.BLACK + Back.GREEN + " Conversion result: " + trgt_crrncy + " " + str(result["result"]) + " ")
            print()

convert_currency()
