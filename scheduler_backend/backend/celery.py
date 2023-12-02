import os

from celery import Celery

APP_NAME = 'backend'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{APP_NAME}.settings')

app = Celery(APP_NAME)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
