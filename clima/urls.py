from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('weather', Weather_APIView.as_view()),
    path('currentWeather', WeatherCurrent_APIView.as_view()),
    path('lastDayWeather', WeatherLastDay_APIView.as_view()),
    path('lastWeekWeather', WeatherLastWeek_APIView.as_view()),
    path('runScript/<int:it>/<int:sec>', UploadWeatherInfo_APIView.as_view())
]