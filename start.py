import schedule
import time

def job():
    print('Hello Word!!!')
            
schedule.every(1).minutes.at(":00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)