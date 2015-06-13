import sys
import random

import requests

from wrappers.exceptions import RandomWrapperException
from wrappers.interface import WeatherInterface


class OpenWeatherMap(WeatherInterface):
    API_URL = 'http://api.openweathermap.org'
    API_URI = '/data/2.5/weather'

    @staticmethod
    def _to_celsius(kelvin_str):
        """
        Convert from Kelvin to Celsius
        :param kelvin_str: Temperature given in Kelvin (string)
        :return: Temperature given in Celsius to 2 decimal places (string)
        """
        return str('{:.2f}'.format(float(kelvin_str) - 272.15))

    @staticmethod
    def _to_fahrenheit(kelvin_str):
        """
        Convert from Kelvin to Fahrenheit
        :param kelvin_str: Temperature given in Kelvin (string)
        :return: Temperature given in Fahrenheit to 2 decimal places (string)
        """
        return str('{:.2f}'.format((float(kelvin_str) - 272.15) * 1.8 + 32))

    @staticmethod
    def _to_miles_per_hour(mps_str):
        """
        Convert from Meters/Second to Miles/Hour
        :param mps_str: Speed given in Meters/Second (string)
        :return: Speed given in Miles/Hour to 2 decimal places (string)
        """
        mps = float(mps_str)

        # Exact Conversion
        centimeters_ps = mps * 100
        inches_ps = centimeters_ps / 2.54
        feet_ps = inches_ps / 12
        miles_ps = feet_ps / 5280
        seconds_per_hour = 60 * 60
        miles_per_hour = miles_ps * seconds_per_hour

        return str('{:.2f}'.format(miles_per_hour))

    def get_weather_info(self, postal_code):
        # Cause a random failure
        if random.choice((True, False)):
            raise RandomWrapperException
        url = '{}{}'.format(self.API_URL, self.API_URI)
        params = {'zip': '{},us'.format(postal_code)}
        resp = requests.get(url, params=params)
        try:
            resp_json = resp.json()
        except:
            raise RandomWrapperException
        celsius = self._to_celsius(resp_json['main']['temp'])
        fahrenheit = self._to_fahrenheit(resp_json['main']['temp'])
        mps = resp_json['wind']['speed']
        mph = self._to_miles_per_hour(mps)
        self.weather_payload = {
            'temperature': (celsius, fahrenheit),
            'pressure': resp_json['main']['pressure'],
            'humidity': resp_json['main']['humidity'],
            'wind_speed': (mps, mph),
            'wind_direction': resp_json['wind']['deg'],
        }

    @property
    def temperature(self):
        return self.weather_payload[sys._getframe().f_code.co_name]

    @property
    def pressure(self):
        return self.weather_payload[sys._getframe().f_code.co_name]

    @property
    def humidity(self, *args, **kwargs):
        return self.weather_payload[sys._getframe().f_code.co_name]

    @property
    def wind_speed(self):
        return self.weather_payload[sys._getframe().f_code.co_name]

    @property
    def wind_direction(self):
        return self.weather_payload[sys._getframe().f_code.co_name]

    def display_content(self):
        print('Results from {}'.format(self.__class__.__name__))
        print('Temperature: {}'.format(self.temperature))
        print('Pressure: {}'.format(self.pressure))
        print('Humidity: {}'.format(self.humidity))
        print('Wind Speed: {}'.format(self.wind_speed))
        print('Wind Direction: {}'.format(self.wind_direction))
