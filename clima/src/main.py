import requests
from pprint import pprint

import psycopg2
from psycopg2 import Error

import time


runScript = True

city = 'Quilmes'
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=21742993dd2295b184e94eb224c464dd&units=metric&lang=es'.format(city)


def startScript():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="dvjjaqjjtprbra",
                                    password="1450667d90c465b1d483c90d5a448da546fad5993f5a28b476e87d13db09b3b3",
                                    host="ec2-35-168-194-15.compute-1.amazonaws.com",
                                    port="5432",
                                    database="devllasmjmoebd")

        # Create a cursor to perform database operations
        cursor = connection.cursor()
            
        while runScript:
            res = requests.get(url)
            data = res.json()

            temp = data['main']['temp']
            latitude = data['coord']['lat']
            longitude = data['coord']['lon']
            description = data['weather'][0]['description']

            cursor.execute("INSERT INTO clima (temperature, latitude, longitude, description) VALUES (%s, %s, %s, %s)", (temp, latitude, longitude, description))

            connection.commit()

            time.sleep(60)

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()


def stopScript():
    runScript = False