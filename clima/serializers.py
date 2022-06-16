from rest_framework import serializers
from clima.models import Clima


# Serializers define the API representation.
class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clima
        fields = ['id','temperature','latitude','longitude','description']