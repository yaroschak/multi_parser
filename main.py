import os

from celery import Celery
from celery.utils.log import get_task_logger

from parser import f

RABBITMQ_USER = os.getenv("RABBITMQ_USER")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS")
RABBITMQ_SERVER = os.getenv("RABBITMQ_SERVER")
RABBITMQ_PORT = os.getenv("RABBITMQ_PORT")

RABBITMQ_URI = f'amqp://{RABBITMQ_USER}:{RABBITMQ_PASS}@{RABBITMQ_SERVER}:{RABBITMQ_PORT}'

celery = Celery('worker', broker=RABBITMQ_URI)
celery.conf.timezone = 'Europe/Kiev'
celery_log = get_task_logger(__name__)


@celery.task(bind=True, default_retry_delay=10)
def pars(self, url: str) -> None:
    try:
        is_done = f(url)
        if not is_done:
            raise Exception()
    except Exception as ex:
        print(f'Error: {url}')
        self.retry(exc=ex)
