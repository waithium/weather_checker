#weather checker

import requests

weather_api_key = 'YOUR API HERE' #this code uses uses OpenWeatherMap API service
city_name = input('enter your city name: ')

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&APPID={weather_api_key}")

'''
this is the list of all the data given  by open weather map api.

print(weather_data.json())
'''

if weather_data.json()['cod'] == "404":
    print("city not found!!")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp =  weather_data.json()['main']['temp']

    print(f'Today\'s weather in {city_name}: {weather}')
    print(f'Today\'s temperature in {city_name}: {temp}')
