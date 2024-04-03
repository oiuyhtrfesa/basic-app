"""
WSGI config for crop_prediction_web project.
action="{% url 'result' %}
It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crop_prediction_web.settings')

application = get_wsgi_application()
