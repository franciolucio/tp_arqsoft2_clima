from django.db import models

# Create your models here.
class Clima(models.Model):
    temperature = models.FloatField()
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    description = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
