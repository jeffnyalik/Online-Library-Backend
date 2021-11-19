from .base import *
import os
from dotenv import load_dotenv

load_dotenv()

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD'),
        'HOST':os.getenv('HOST'),
        'PORT':os.getenv('PORT')
    }
}
