import os

from celery import Celery

from shared.infra.celery import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config')

app = Celery(
    'tasks',
    broker=config.CELERY_BROKER_URL,
    backend=config.RESULT_BACKEND_URL,
)
app.autodiscover_tasks()
