"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.dev_settings.dev')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings') ## For deployment
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.stage')


application = get_wsgi_application()
