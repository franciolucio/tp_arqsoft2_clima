from locust import HttpUser, task, between

class Weather(HttpUser):
    wait_time = between(1, 5)
    
    @task
    def get_currentWeather(self):
        self.client.get("currentWeather")
        
    @task
    def get_lastDayWeather(self):
        self.client.get("lastDayWeather")
        
    @task
    def get_lastWeekWeather(self):
        self.client.get("lastWeekWeather")