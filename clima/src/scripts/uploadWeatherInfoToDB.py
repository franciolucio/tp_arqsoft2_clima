from clima.src.components.WeatherLoaderComponent import uploadWeatherInfoToDB

import time


def runScipt(it, sec):
    print("<<< Start Scipt >>>")
    iterations = it
    seconds = sec - 1 # El -1 es para ajustar el tiempo de carga por lo que tarda ejecutar en local
    current = 0
    print("Iterations:", iterations, "/ Time:", seconds, "seconds")

    while current != iterations:
        uploadWeatherInfoToDB()
        current = current + 1
        print("Iteration", current, "de", iterations)
        time.sleep(seconds)

    print("<<< End Scipt >>>")
    return "<<< End Scipt >>>"



# Worker
"""
import schedule

def job():
    uploadWeatherInfoToDB()


schedule.every(5).minutes.at(":00").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
"""