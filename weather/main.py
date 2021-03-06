#! /usr/bin/env python
import sys
import os

from wrappers.weather_api import WeatherApi

# These imports are for use as examples to show how to force a klass instance
from wrappers.open_weather_map import OpenWeatherMap
from wrappers.weather_underground import WeatherUnderground


def weather_help():
    print('*' * 60)
    print('* Usage: python main.py postal_code                        *')
    print('* args: postal_code (US Support Only - 5 digits)           *')
    print('*                                                          *')
    print('* Display weather information:                             *')
    print('* Temperature: Degrees (Celcius, Fahrenheit)               *')
    print('* Pressure: Hectopascal (hPa)                              *')
    print('* Humidity: Percentage (%)                                 *')
    print('* Wind Speed: meter/sec, miles/hour                        *')
    print('* Wind Direction: Degrees (meteorological)                 *')
    print('*' * 60)
    sys.exit()


def display_weather_info(postal_code):
    weather_api = WeatherApi(postal_code)
    weather_api.display_content()


if __name__ == '__main__':
    os.system(['clear', 'cls'][os.name == 'nt'])
    if len(sys.argv) != 2:
        weather_help()

    entered_postal_code = sys.argv[1]
    if not entered_postal_code.isdigit() or len(entered_postal_code) != 5:
        weather_help()

    display_weather_info(entered_postal_code)
