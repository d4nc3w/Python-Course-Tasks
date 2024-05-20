import requests
import matplotlib.pyplot as graph
from datetime import datetime

url = "http://api.bp.pl/api/exchangerates/rates/c"

# x = list(range(0, 10))
# y = list(range(-10, 0))
# graph.plot(x, y)
# graph.show()

while True:
    print("-------------MENU-------------")
    print("(1) Get current PLN exchange rate")
    print("(2) Get exchange rate of given currency to PLN")
    print("(3) Get exchange rate of given currency for given period")
    print("(4) Exit")
    print("------------------------------")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        code = input("Enter currency code: ")
        # I DONT KNOW WHY IT DOESNT WORK ANYMORE IT WORKED!!!
        #url = f'http://api.nbp.pl/api/exchangerates/rates/c/{code}/today/?format=json'
        # Thats why data from yesterday is used
        url = f'http://api.nbp.pl/api/exchangerates/rates/c/{code}/last/1/?format=json'

        print(url)
        response = requests.get(url)
        rates = response.json()['rates']
        print(f'Rates: {rates}')
    if choice == 2:
        code = input("Enter currency code: ")
        period = input("Enter period in number of days: ")
        url = f'http://api.nbp.pl/api/exchangerates/rates/c/{code}/last/{period}/?format=json'
        response = requests.get(url)
        rates = response.json()['rates']
        print(f'Rates: {rates}')

        # graph
        x = [entry['effectiveDate'] for entry in rates]
        y = [entry['bid'] for entry in rates]
        graph.plot(x, y)
        graph.xlabel('Date')
        graph.ylabel('Bid')
        graph.show()

    if choice == 3:
        code = input("Enter currency code: ")
        _from = input("Enter start date (YYYY-MM-DD): ")
        _to = input("Enter end date (YYYY-MM-DD): ")
        url = f'http://api.nbp.pl/api/exchangerates/rates/a/{code}/{_from}/{_to}/?format=json'
        response = requests.get(url)
        rates = response.json()['rates']
        print(f'Rates: {rates}')

        # graph
        x = [entry['effectiveDate'] for entry in rates]
        y = [entry['mid'] for entry in rates]
        graph.plot(x, y)
        graph.xlabel('Date')
        graph.ylabel('Mid')
        graph.show()

    if choice == 4:
        print("Closing...")
        print("------------------------------")
        exit()