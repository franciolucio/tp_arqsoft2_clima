# # Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status
from django.http import Http404
from django.shortcuts import render


def index(request):
    return render(request,"clima/index.html")