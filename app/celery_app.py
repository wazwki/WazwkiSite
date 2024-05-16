import os
import time
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_settings.settings')

app = Celery('app_settings')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()
app.conf.broker_connection_retry_on_startup = True

'''
Simple task for demonstration how it work and how write tasks
@app.task()
def debug_task():
    time.sleep(20)
    print("debug task celery")
'''
