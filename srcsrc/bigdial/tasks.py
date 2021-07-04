from celery import shared_task

from time import sleep
from json import dumps

from .models import Task


@shared_task
def hello(task_id, value):
    task = Task.objects.get(id=task_id)
    task.text = dumps({"result": value ** 5})
    task.save()
    sleep(15)