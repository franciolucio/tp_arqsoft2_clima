from django.apps import AppConfig
import requests_cache

class ClimaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clima'
    requests_cache.install_cache('clima_cache', backend='sqlite', expire_after=300)
