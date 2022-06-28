from clima.src.components.WeatherLoaderComponent import getCurrentWeather, getLastDayWeather, getLastWeekWeather


def getCurrentWeatherEndpoint():
    currentWeather = getCurrentWeather()
    if currentWeather:
        return currentWeather
    else:
        return "An unexpected error has occurred, please try again"


def getLastDayWeatherEndpoint():
    lastDayWeather = getLastDayWeather()
    if lastDayWeather:
        return lastDayWeather
    else:
        return "An unexpected error has occurred, please try again"


def getLastWeekWeatherEndpoint():
    lastWeekWeather = getLastWeekWeather()
    if lastWeekWeather:
        return lastWeekWeather
    else:
        return "An unexpected error has occurred, please try again"