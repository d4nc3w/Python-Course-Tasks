import requests

key = 'fcbea5926912a56c6d1356075cd5b831'

while True:
    print("-------------MENU-------------")
    print("(1) Get current weather in Warsaw")
    print("(2) Get 5 Day / 3 Hour forecast for Warsaw")
    print("(3) Get current weather in London")
    print("(4) Get Current Air Pollution in London")
    print("(5) Get Geo coordinates")
    print("(6) Exit")
    print("------------------------------")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        url= f'https://api.openweathermap.org/data/2.5/weather?q=Warsaw,pl&APPID={key}'
        response = requests.get(url)
        weather = response.json()
        print(f'Weather: {weather}')
    if choice == 2:
        url = f'https://api.openweathermap.org/data/2.5/forecast?q=Warsaw,pl&APPID={key}'
        response = requests.get(url)
        forecast = response.json()
        print(f'Forecast: {forecast}')
    if choice == 3:
        url = f'https://api.openweathermap.org/data/2.5/weather?q=London,uk,pl&APPID={key}'
        response = requests.get(url)
        weather = response.json()
        print(f'Weather: {weather}')
    if choice == 4:
        url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat=50&lon=50&APPID={key}'
        response = requests.get(url)
        pollution = response.json()
        print(f'Pollution: {pollution}')
    if choice == 5:
        city = input("Enter city name (In Uppercase): ")
        print("Examples: Warsaw, London, Paris, Berlin")
        url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&APPID={key}'
        response = requests.get(url)
        geo = response.json()
        print(f'Geo: {geo}')
    if choice == 6:
        print("Closing...")
        print("------------------------------")
        exit()
