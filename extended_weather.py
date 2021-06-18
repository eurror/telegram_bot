import requests


BASE_URL = 'https://api.openweathermap.org/data/2.5/onecall?'
GEO_COORDINATES = 'lat=42.87&lon=74.59'
API_KEY = 'dbbe9c42acb0907171fb9540f8f38a02'
UNITS = 'metric'
# units Temperature is available in Fahrenheit, Celsius and Kelvin units.
# For temperature in Fahrenheit use units = imperial
# For temperature in Celsius use units = metric
# Temperature in Kelvin is used by default,
# no need to use units parameter in API call
URL = BASE_URL + GEO_COORDINATES + '&appid=' + \
    API_KEY + '&lang=ru' + '&units=' + UNITS


response = requests.get(URL)
data = response.json()
daily = data['daily']
day_0 = daily[0]
day_1 = daily[1]
day_2 = daily[2]
day_3 = daily[3]
day_4 = daily[4]
day_5 = daily[5]
day_6 = daily[6]
day_7 = daily[7]
weather_for_next_7_days = f'''Погода на сегодня: {day_0['weather'][0]['description']}
Максимальная температура: {day_0['temp']['max']}°C
Минимальная температура: {day_0['temp']['min']}°C
Утром: {day_0['temp']['morn']}°C
Вечером: {day_0['temp']['eve']}°C
Ночью: {day_0['temp']['night']}°C
Ощущается как: {day_0['feels_like']['day']}°C

Погода на следующие 7 дней:

1:
Погода: {day_1['weather'][0]['description']}
Максимальная температура: {day_1['temp']['max']}°C
Минимальная температура: {day_1['temp']['min']}°C
Утром: {day_1['temp']['morn']}°C
Вечером: {day_1['temp']['eve']}°C
Ночью: {day_1['temp']['night']}°C
Ощущается как: {day_1['feels_like']['day']}°C

2:
Погода: {day_2['weather'][0]['description']}
Максимальная температура: {day_2['temp']['max']}°C
Минимальная температура: {day_2['temp']['min']}°C
Утром: {day_2['temp']['morn']}°C
Вечером: {day_2['temp']['eve']}°C
Ночью: {day_2['temp']['night']}°C
Ощущается как: {day_2['feels_like']['day']}°C

3:
Погода: {day_3['weather'][0]['description']}
Максимальная температура: {day_3['temp']['max']}°C
Минимальная температура: {day_3['temp']['min']}°C
Утром: {day_3['temp']['morn']}°C
Вечером: {day_3['temp']['eve']}°C
Ночью: {day_3['temp']['night']}°C
Ощущается как: {day_3['feels_like']['day']}°C

4:
Погода: {day_4['weather'][0]['description']}
Максимальная температура: {day_4['temp']['max']}°C
Минимальная температура: {day_4['temp']['min']}°C
Утром: {day_4['temp']['morn']}°C
Вечером: {day_4['temp']['eve']}°C
Ночью: {day_4['temp']['night']}°C
Ощущается как: {day_4['feels_like']['day']}°C

5:
Погода: {day_5['weather'][0]['description']}
Максимальная температура: {day_5['temp']['max']}°C
Минимальная температура: {day_5['temp']['min']}°C
Утром: {day_5['temp']['morn']}°C
Вечером: {day_5['temp']['eve']}°C
Ночью: {day_5['temp']['night']}°C
Ощущается как: {day_5['feels_like']['day']}°C

6:
Погода: {day_6['weather'][0]['description']}
Максимальная температура: {day_6['temp']['max']}°C
Минимальная температура: {day_6['temp']['min']}°C
Утром: {day_6['temp']['morn']}°C
Вечером: {day_6['temp']['eve']}°C
Ночью: {day_6['temp']['night']}°C
Ощущается как: {day_6['feels_like']['day']}°C

7:
Погода: {day_7['weather'][0]['description']}
Максимальная температура: {day_7['temp']['max']}°C
Минимальная температура: {day_7['temp']['min']}°C
Утром: {day_7['temp']['morn']}°C
Вечером: {day_7['temp']['eve']}°C
Ночью: {day_7['temp']['night']}°C
Ощущается как: {day_7['feels_like']['day']}°C'''
