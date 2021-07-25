import data as data
import requests as requests, json


r_exchange_required_usd = requests.get(f'http://www.floatrates.com/daily/USD.json')
r_exchange_required_eur = requests.get(f'http://www.floatrates.com/daily/EUR.json')

r_exchange_to_json_required_usd = r_exchange_required_usd.json()
r_exchange_to_json_required_eur = r_exchange_required_eur.json()

cache = {}

custom_money_currency = input()

r_exchange_required_main_currency = requests.get(f'http://www.floatrates.com/daily/{custom_money_currency}.json')

r_exchange_to_json_required_main_currency= r_exchange_required_main_currency.json()

while True:
    exchange_input = input()

    if not exchange_input:
        break

    custom_money_cash = float(input())

    print("Checking the cache...")
    if exchange_input == "usd":
        print("Oh! It is in the cache!")
        required_cash_rate_usd_eur = float(r_exchange_to_json_required_usd[custom_money_currency]['rate'])
        exchange_result = custom_money_cash / required_cash_rate_usd_eur
        print(f'You received {round(exchange_result, 2)} {exchange_input.upper()}.')
    elif exchange_input == "eur":
        print("Oh! It is in the cache!")
        required_cash_rate_eur = float(r_exchange_to_json_required_eur[custom_money_currency]['rate'])
        exchange_result = custom_money_cash / required_cash_rate_eur
        print(f'You received {round(exchange_result, 2)} {exchange_input.upper()}.')
    elif len(cache) != 0 and exchange_input in cache:
        print("Oh! It is in the cache!")
        exchange_result = custom_money_cash * cache[exchange_input]
        print(f'You received {round(exchange_result, 2)} {exchange_input.upper()}.')
    else:
        print("Sorry, but it is not in the cache!")
        required_cash_rate = float(r_exchange_to_json_required_main_currency[exchange_input]['rate'])
        cache[exchange_input] = required_cash_rate
        exchange_result = custom_money_cash * required_cash_rate
        print(f'You received {round(exchange_result, 2)} {exchange_input.upper()}.')
