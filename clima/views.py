# # Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from .models import Clima
from .serializers import ClimaSerializer
from rest_framework import status
from django.http import Http404
from django.shortcuts import render


def index(request):
    return render(request,"clima/index.html")

class Clima_APIView(APIView):
	def get(self, request, format=None, *args, **kwargs):
		allClima = Clima.objects
		serializer = ClimaSerializer(allClima, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = ClimaSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClimaDetails_APIView(APIView):
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
		serializer = ClimaSerializer(usuario, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
	def delete(self, request, pk, format=None):
		clima = self.get_object(pk)
		clima.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class ClimaStatisticsToday_APIView(APIView):
    
	def get(self, request, format=None, *args, **kwargs):
		allClima = Clima.objects.filter()
		serializer = ClimaSerializer(allClima, many=True)
		return Response(serializer.data)

class ClimaStatisticsWeek_APIView(APIView):
    
	def get(self, request, format=None, *args, **kwargs):
		allClima = Clima.objects.filter()
		serializer = ClimaSerializer(allClima, many=True)
		return Response(serializer.data)