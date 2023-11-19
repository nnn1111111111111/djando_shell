from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()

    return render(request, 'main/index.html', {'title':'Главная страница', 'tasks':tasks})


def about(request):
    return render(request, 'main/about-us.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Вы неверно заполнили форму'

    form = TaskForm()
    context = {
        'form':form,
        'error':error
    }
    return render(request, 'main/create.html', context)
# Create your views here.
