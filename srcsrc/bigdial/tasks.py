from celery import shared_task

from time import sleep
from json import dumps

from .models import Task

# создаем задачу которую получили от вьюхи
# запускаем отдельный процесс для ее решения селери
@shared_task
def hello(task_id, value):
    # получили данные для записи результата в базу по id
    task = Task.objects.get(id=task_id)
    # пишем результат решения задачи в поле текст таска
    task.text = dumps({"result": value ** 5})
    sleep(15)
    task.save()
