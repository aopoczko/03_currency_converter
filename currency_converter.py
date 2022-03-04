import requests


def add_currency(currency):  #add new currency exchange rate to dictionary
    rates[currency] = float(requests.get(f'http://www.floatrates.com/daily/{start_currency}.json').json()[currency]['rate'])


def exchange():  #print currency exchange result $$$
    print(f'You received {round(cash * rates[currency], 2)} {currency.upper()}.')


start_currency = input().lower()
rates = {}
if start_currency != "usd":
    add_currency('usd')
if start_currency != "eur":
    add_currency('eur')

currency = " "

while currency != "":
    currency = input().lower()
    if currency == "":
        break

    cash = int(input())
    print("Checking the cache...")
    if currency in rates:
        print('Oh! It is in the cache!')
        exchange()
    else:
        print('Sorry, but it is not in the cache!')
        add_currency(currency)
        exchange()
