import importlib

from weather import settings
from wrappers import exceptions as wrappers_exceptions
from wrappers.interface import WeatherInterface


def retry(func):
    def wrapped(*args, **kwargs):
        args = list(args)
        wrapper_instance = args.pop(0)
        if kwargs.get('ignore_retry'):
            return func(wrapper_instance, *args, **kwargs)
        try:
            return func(wrapper_instance, *args, **kwargs)
        except wrappers_exceptions.RandomWrapperException:
            print('Random Exception using {}!'.format(
                wrapper_instance.instance.__class__.__name__))
            kwargs['ignore_retry'] = True
            for module_str in settings.WEATHER_API_CHOICES:
                instance = wrapper_instance._get_instance(module_str)
                wrapper_instance.instance = instance
                try:
                    return getattr(wrapper_instance, func.__name__)(
                        *args, **kwargs)
                except wrappers_exceptions.RandomWrapperException:
                    print('Another Random Exception using {}!'.format(
                        instance.__class__.__name__))
                    pass
            raise wrappers_exceptions.ExhaustedWrapperException
    return wrapped


class WeatherApi(WeatherInterface):
    def __init__(self, postal_code, klass=None):
        if klass:
            self.instance = klass()
        else:
            self.instance = self._get_instance(settings.WEATHER_API)
        super(WeatherApi, self).__init__()
        self.postal_code = postal_code
        self.get_weather_info()

    def _get_instance(self, module_str):
        module, klass = module_str.rsplit('.', 1)
        return getattr(importlib.import_module(module), klass)()

    @retry
    def get_weather_info(self, ignore_retry=False):
        self.instance.get_weather_info(self.postal_code)

    @property
    def temperature(self):
        return self.instance.temperature

    @property
    def pressure(self):
        return self.instance.pressure

    @property
    def humidity(self):
        return self.instance.humidity

    @property
    def wind_speed(self):
        return self.instance.wind_speed

    @property
    def wind_direction(self):
        return self.instance.wind_direction

    def display_content(self):
        return self.instance.display_content()
