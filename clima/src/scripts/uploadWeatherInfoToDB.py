from clima.src.components.WeatherLoaderComponent import uploadWeatherInfoToDB
import schedule
import time

def job():
    uploadWeatherInfoToDB()
            
schedule.every(1).hour.at(":00:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)