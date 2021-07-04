
from django.http import HttpResponse

from .tasks import hello as hello_task
from .models import Task

# основная вьюха
def hello(request):
    # передаем в value из реквеста value иначе даем 0
    value = int(request.GET.get('value', 0))
    # создаем в базе очередную задачу, текст необязателен в Task,
    # поэтому создаем только id
    task = Task.objects.create()
    # отправляем в таск ид и значение над которым необходимо глумиться
    # @shared_task добавил функции hello_task метод delay
    # запускающий функцию hello_task в рамках отдельного процесса
    hello_task.delay(task.id, value) # как только эта строчка выполнилась, идем в сеттинги
    # даем сигнал брокеру, сохранить task.id и value в редис
    # возвращаем пользователю ответ, чтобы он знал что его задача обрабатывается 15 сек
    return HttpResponse(f'hello your task will be done and you can check it id = {task.id}')

# в ней можно посмотреть результаты выполнения задачи
# возвращает результат выполнения задачи отправленной вьюхой хелло в селери
def check(request, id):
    task = Task.objects.get(id=id)
    result = ''
    if task.text is not None:
        result = task.text
    return HttpResponse(result)