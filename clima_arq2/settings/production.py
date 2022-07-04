from .base import *
import os
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['clima-arq2.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'devllasmjmoebd',
        'USER': 'dvjjaqjjtprbra',
        'PASSWORD' : '1450667d90c465b1d483c90d5a448da546fad5993f5a28b476e87d13db09b3b3',
        'HOST': 'ec2-35-168-194-15.compute-1.amazonaws.com',
        'PORT': 5432
    }
}

