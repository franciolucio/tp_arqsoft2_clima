from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('clima', Clima_APIView.as_view()),
	path('clima/<int:pk>', Clima_APIView.as_view()),
    path('climaToday', ClimaStatisticsToday_APIView.as_view()),
    path('climaWeek', ClimaStatisticsWeek_APIView.as_view())
]