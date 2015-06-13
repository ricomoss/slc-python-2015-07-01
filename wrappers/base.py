import sys
import random

from wrappers.exceptions import RandomWrapperException
from wrappers.interface import WeatherInterface


class BaseWeatherWrapper(WeatherInterface):
    def get_weather_info(self, *args, **kwargs):
        # Cause a random failure
        if random.choice((True, False)):
            raise RandomWrapperException
        self.weather_payload = {
            'temperature': ('Celsius', 'Fahrenheit'),
            'pressure': 'Hectopascal',
            'humidity': 'Percentage',
            'wind_speed': ('meter/sec', 'miles/hour'),
            'wind_direction': 'degrees',
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
