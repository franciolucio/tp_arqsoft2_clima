from clima.src.components.WeatherLoaderComponent import uploadWeatherInfoToDB
import schedule
import time

def job():
    uploadWeatherInfoToDB()
            
schedule.every(5).minutes.at(":00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)