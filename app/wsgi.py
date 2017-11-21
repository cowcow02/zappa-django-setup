"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from raven import Client
from raven.middleware import Sentry
from raven.transport.requests import RequestsHTTPTransport

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

client = Client(settings.SENTRY_DSN, transport=RequestsHTTPTransport)

application = Sentry(get_wsgi_application(), client=client)
