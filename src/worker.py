import os

from celery import Celery

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config')

app = Celery(
    'tasks',
    broker=settings.CELERY_BROKER_URL,
    backend=settings.RESULT_BACKEND_URL,
)
app.autodiscover_tasks()
