""" WSGI config for app_setings project """

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_settings.settings')

application = get_wsgi_application()
