import requests
import psycopg2
import time
from psycopg2 import Error
from datetime import datetime
from datetime import timedelta 


city = 'Quilmes'
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=21742993dd2295b184e94eb224c464dd&units=metric&lang=es'.format(city)
# https://httpbin.org/delay/10

def setCity(cityName):
    city = cityName


def getCurrentWeather():
    res = requests.get(url,timeout=5)
    data = res.json()

    currentWeather = {
        "temperature": data['main']['temp'],
        "latitude": data['coord']['lat'],
        "longitude": data['coord']['lon'],
        "description": data['weather'][0]['description']
    }
    now = time.ctime(int(time.time()))
    print ("Time: {0} / Used Cache: {1}".format(now, res.from_cache))
    return currentWeather

def getLastDaysWeather(number_of_days):
    try:
        yesterday = datetime.now() - timedelta(days = number_of_days)
        date = yesterday.strftime("%Y/%m/%d %H:%M:%S")
        print("date and time:",date)

        # Connect to an existing database
        connection = psycopg2.connect(
            user="dvjjaqjjtprbra",
            password="1450667d90c465b1d483c90d5a448da546fad5993f5a28b476e87d13db09b3b3",
            host="ec2-35-168-194-15.compute-1.amazonaws.com",
            port="5432",
            database="devllasmjmoebd"
        )

        # Create a cursor to perform database operations
        cursor = connection.cursor()

        cursor.execute(
            "SELECT SUM(temperature) AS suma, COUNT(*) AS total FROM clima_clima WHERE created_at > %s",
            (date,)
        )

        # Fetch result
        record = cursor.fetchone()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()

    print(record)
    lastDayWeather = record[0] / record[1]

    return round(lastDayWeather, 2)


def getLastDayWeather():
    return getLastDaysWeather(1)


def getLastWeekWeather():
    return getLastDaysWeather(7)


def uploadWeatherInfoToDB():
    try:
        currentWeather = getCurrentWeather()

        # Connect to an existing database
        connection = psycopg2.connect(
            user="dvjjaqjjtprbra",
            password="1450667d90c465b1d483c90d5a448da546fad5993f5a28b476e87d13db09b3b3",
            host="ec2-35-168-194-15.compute-1.amazonaws.com",
            port="5432",
            database="devllasmjmoebd"
        )

        # Create a cursor to perform database operations
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO clima_clima (temperature, latitude, longitude, description) VALUES (%s, %s, %s, %s)", 
            (currentWeather["temperature"], currentWeather["latitude"], currentWeather["longitude"], currentWeather["description"])
        )

        connection.commit()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()