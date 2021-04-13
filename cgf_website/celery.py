import os
from celery import Celery
from celery.utils.log import get_task_logger
from decouple import config

# Initialize celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cgf_website.settings')
celery_log = get_task_logger(__name__)


app = Celery('cgf_website', broker=f'redis://{config("REDIS_HOST")}:{config("REDIS_PORT")}/{config("REDIS_DB")}')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
