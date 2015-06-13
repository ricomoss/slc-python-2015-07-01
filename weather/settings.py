BASE_WEATHER_API = 'wrappers.base.BaseWeatherWrapper'
OPEN_WEATHER_MAP_API = 'wrappers.open_weather_map.OpenWeatherMap'
WEATHER_UNDERGROUND_API = 'wrappers.weather_underground.WeatherUnderground'

WEATHER_API_CHOICES = (
    OPEN_WEATHER_MAP_API,
    WEATHER_UNDERGROUND_API,
    BASE_WEATHER_API,
)

WEATHER_API = OPEN_WEATHER_MAP_API
