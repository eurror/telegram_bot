import requests

from extended_weather import API_KEY, UNITS

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?q='
CITY = 'Bishkek'
URL = BASE_URL + CITY + '&appid=' + API_KEY + '&lang=ru' + '&units=' + UNITS

response = requests.get(URL)
data = response.json()
main = data['main']
temperature = main['temp']
feels_like = main['feels_like']
report = data['weather']
description = report[0]['description']
city = data['name']
weather_for_now = f'''Сегодня в {city} {description}
Средняя температура: {temperature}°C
Погода ощущается как: {feels_like}°C'''
