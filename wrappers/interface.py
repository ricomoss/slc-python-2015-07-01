class WeatherInterface(object):
    def __init__(self):
        self.weather_payload = dict()

    def get_weather_info(self, *args, **kwargs):
        """
        Generic getter for creating the instance package for the weather info
        :return: Python Dictionary
        """
        raise NotImplementedError(
            '{} must implement _get_weather_info'.format(
                self.__class__.__name__))

    @property
    def temperature(self):
        """
        Interface for the temperature property
        :return: Temperature in degrees (Celsius, Fahrenheit) (Tuple)
        """
        raise NotImplementedError(
            '{} must implement temperature'.format(self.__class__.__name__))

    @property
    def pressure(self):
        """
        Interface for the pressure property
        :return: Pressure in Hectopascal (hPa)
        """
        raise NotImplementedError(
            '{} must implement pressure'.format(self.__class__.__name__))

    @property
    def humidity(self):
        """
        Interface for the humidity property
        :return: Humidity in percentage (%)
        """
        raise NotImplementedError(
            '{} must implement humidity'.format(self.__class__.__name__))

    @property
    def wind_speed(self):
        """
        Interface for the wind speed property
        :return: Wind Speed (meter/sec, miles/hour) (Tuple)
        """
        raise NotImplementedError(
            '{} must implement wind_speed'.format(self.__class__.__name__))

    @property
    def wind_direction(self):
        """
        Interface for the wind direction property
        :return: Wind direction in degrees (meteorological)
        """
        raise NotImplementedError(
            '{} must implement wind_direction'.format(self.__class__.__name__))

    def display_content(self):
        """
        Print the content of the weather_payload in a meaningful way
        """
        raise NotImplementedError(
            '{} must implement display_content'.format(
                self.__class__.__name__))
