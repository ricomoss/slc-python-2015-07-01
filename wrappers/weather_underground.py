
import sys
import random

import requests

from wrappers.exceptions import RandomWrapperException
from wrappers.interface import WeatherInterface

import pprint
pp = pprint.PrettyPrinter(indent=4)


class WeatherUnderground(WeatherInterface):
    API_URL = 'http://api.wunderground.com'
    API_CONDITIONS_URI = '/api/{}/conditions/q/{}/{}.json'
    API_GEOLOOKUP_URI = '/api/{}/geolookup/q/{}.json'
    API_KEY = '55db22c8e7934760'

    @staticmethod
    def _to_meters_per_second(kph_str):
        """
        Convert from Kilometers/Hour to Meters/Second
        :param kph_str: Speed given in Kilometers/Hour (string)
        :return: Speed given in Meters/Second to 2 decimal places (string)
        """
        kph = float(kph_str)
        meters_ph = kph * 1000
        seconds_per_hour = 60 * 60
        mps = meters_ph / seconds_per_hour

        return str('{:.2f}'.format(mps))

    def _get_codes(self, postal_code):
        api_uri = self.API_GEOLOOKUP_URI.format(self.API_KEY, postal_code)
        url = '{}{}'.format(self.API_URL, api_uri)
        resp = requests.get(url)
        try:
            resp_json = resp.json()['location']
        except:
            raise RandomWrapperException
        city_code = resp_json['city'].replace(' ', '_')
        state_code = resp_json['state']
        return state_code, city_code

    def get_weather_info(self, postal_code):
        # Cause a random failure
        if random.choice((True, False)):
            raise RandomWrapperException
        state_code, city_code = self._get_codes(postal_code)
        api_uri = self.API_CONDITIONS_URI.format(
            self.API_KEY, state_code, city_code)
        url = '{}{}'.format(self.API_URL, api_uri)
        resp = requests.get(url)
        try:
            resp_json = resp.json()['current_observation']
        except:
            raise RandomWrapperException
        celsius = resp_json['temp_c']
        fahrenheit = resp_json['temp_f']
        mps = self._to_meters_per_second(
            resp_json['wind_kph'])
        mph = resp_json['wind_mph']
        humidity = resp_json['relative_humidity'].strip('%')
        self.weather_payload = {
            'temperature': (celsius, fahrenheit),
            'pressure': resp_json['pressure_mb'],
            'humidity': humidity,
            'wind_speed': (mps, mph),
            'wind_direction': resp_json['wind_degrees'],
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
