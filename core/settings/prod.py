from .base import *
import os
from dotenv import load_dotenv



load_dotenv()

DEBUG=True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SECRET_KEY = os.getenv('SECRET_KEY', '2534a4dde10e2dbdebdb2675b6ac96aeb54409854db0e3a05424a33067a4')

ALLOWED_HOSTS = ['online-library1990.herokuapp.com']


import dj_database_url
DATABASES['default'] =  dj_database_url.config()