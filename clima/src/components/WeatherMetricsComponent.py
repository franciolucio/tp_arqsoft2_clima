from clima.src.components.WeatherLoaderComponent import getCurrentWeather, getLastDayWeather, getLastWeekWeather


def getCurrentWeatherEndpoint():
    currentWeather = getCurrentWeather()
    return currentWeather["temperature"]


def getLastDayWeatherEndpoint():
    lastDayWeather = getLastDayWeather()
    promLastDayWeather = lastDayWeather  # Hacer el calculo del promedio de la temperatura del ultimo dia
    return promLastDayWeather


def getLastWeekWeatherEndpoint():
    lastWeekWeather = getLastWeekWeather()
    promLastWeekWeather = lastWeekWeather     # Hacer el calculo del promedio de la temperatura de la ultima semana
    return promLastWeekWeather