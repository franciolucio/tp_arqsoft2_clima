# # Create your views here.

from clima.src.components.WeatherMetricsComponent import getCurrentWeatherEndpoint, getLastDayWeatherEndpoint, getLastWeekWeatherEndpoint
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Clima
from .serializers import WeatherSerializer
from rest_framework import status
from django.http import Http404
from django.shortcuts import render


def index(request):
    return render(request,"clima/index.html")

class Weather_APIView(APIView):

	def get(self, request, format=None, *args, **kwargs):
		allClima = Clima.objects
		serializer = WeatherSerializer(allClima, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = WeatherSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WeatherDetails_APIView(APIView):

	def get_object(self, pk):
		try:
			return Clima.objects.get(pk=pk)
		except Clima.DoesNotExist:
			raise Http404
	
	def get(self, request, pk, format=None):
		clima = self.get_object(pk)
		serializer = Clima(clima)  
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		usuario = self.get_object(pk)
		serializer = WeatherSerializer(usuario, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
	def delete(self, request, pk, format=None):
		clima = self.get_object(pk)
		clima.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class WeatherCurrent_APIView(APIView):
    
	def get(self, request, format=None, *args, **kwargs):
		currentWeather = getCurrentWeatherEndpoint()
		return Response(currentWeather)


class WeatherLastDay_APIView(APIView):
    
	def get(self, request, format=None, *args, **kwargs):
		lastDayWeather = getLastDayWeatherEndpoint()
		return Response(lastDayWeather)


class WeatherLastWeek_APIView(APIView):
    
	def get(self, request, format=None, *args, **kwargs):
		lastWeekWeather = getLastWeekWeatherEndpoint()
		return Response(lastWeekWeather)