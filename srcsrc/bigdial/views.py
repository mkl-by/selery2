
from django.http import HttpResponse

from .tasks import hello as hello_task
from .models import Task

def hello(request):
    # передаем в value из реквеста value иначе даем 0
    value = request.GET.get('value', 0)
    task = Task.objects.create()
    hello_task.delay(task.id, value)
    return HttpResponse(f'hello your task will be done and you can check it id = {task.id}')