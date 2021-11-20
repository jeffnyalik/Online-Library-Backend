from .base import *
import os
from dotenv import load_dotenv

load_dotenv()

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.getenv('NAME'),
#         'USER': os.getenv('USER'),
#         'PASSWORD': os.getenv('PASSWORD'),
#         'HOST':os.getenv('HOST'),
#         'PORT':os.getenv('PORT')
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ALLOWED_HOSTS = ['online-library1990.herokuapp.com']

import dj_database_url
prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)