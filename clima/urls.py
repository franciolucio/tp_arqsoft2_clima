from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('clima', Clima_APIView.as_view()),
	path('clima/<int:pk>', Clima_APIView.as_view()),
    path('climaToday', ClimaStatisticsToday_APIView.as_view()),
    path('climaWeek', ClimaStatisticsWeek_APIView.as_view())
]