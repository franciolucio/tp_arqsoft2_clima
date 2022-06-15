from django.urls import path
from .views import *
from django.contrib import admin

from clima import views

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('clima', Clima_APIView.as_view()),
	path('clima/<int:pk>', Clima_APIView.as_view()),
    path('climaToday', ClimaStatisticsToday_APIView.as_view()),
    path('climaWeek', ClimaStatisticsWeek_APIView.as_view()),
    path('startScript', views.startScript, name='startScript'),
    path('stopScript', views.stopScript, name='stopScript')
]