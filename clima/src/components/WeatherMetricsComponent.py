from clima.src.components.WeatherLoaderComponent import getCurrentWeather, getLastDayWeather, getLastWeekWeather
import requests

def getCurrentWeatherEndpoint():
    try:
        currentWeather = getCurrentWeather()
        return currentWeather["temperature"]
    except requests.exceptions.Timeout:
        print('TIME OUT !!!!')

def getLastDayWeatherEndpoint():
    lastDayWeather = getLastDayWeather()
    promLastDayWeather = lastDayWeather  # Hacer el calculo del promedio de la temperatura del ultimo dia
    return promLastDayWeather


def getLastWeekWeatherEndpoint():
    lastWeekWeather = getLastWeekWeather()
    promLastWeekWeather = lastWeekWeather     # Hacer el calculo del promedio de la temperatura de la ultima semana
    return promLastWeekWeather