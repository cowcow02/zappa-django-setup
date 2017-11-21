import os

from django.conf import settings
from raven import Client
from raven.transport.requests import RequestsHTTPTransport

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

import logging

def lambda_exception_handler(e, event, context):
    client = Client(settings.SENTRY_DSN, transport=RequestsHTTPTransport)
    client.captureException()
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)
    logger.error('Something went wrong!')
    logger.error(e)
    logger.error(event)
    logger.error(context)

    return True  # Prevent invocation retry
