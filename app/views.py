from django.shortcuts import render
from django.shortcuts import reverse
from datetime import datetime
from os import listdir

# import os

# Create your views here.

def home(request):
    file_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    context = {
        'pages': pages
    }
    return render(request, file_name, context)

def time(request):
    file_name = 'app/time.html'
    current_time = datetime.strftime(datetime.now(), "%H:%M:%S")

    context = {
        'time': current_time
    }
    return render(request, file_name, context)


def workdir(request):
    file_name = 'app/workdir.html'
    file_list = [f for f in listdir('./')]
    context = {
        'file_list': file_list,
        'home_url': reverse('home')
    }
    return render(request, file_name, context)    