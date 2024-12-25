from django.shortcuts import render
from random import randint
from datetime import datetime
def cubes_view(request):
    rand1 = randint(1, 6)
    rand2 = randint(1, 6)

    context = {
        'rand1': rand1,
        'rand2': rand2
    }


    return render(request, 'cubes.html', context)

def theme_view(request):
    days_of_week = [
        "Понедельник", "Вторник", "Среда",
        "Четверг", "Пятница", "Суббота", "Восвресенье"
    ]

def theme_view(request):
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    string_date = f"{now.day}/{now.month}/{now.year}г"
    string_time = f"{hour}:{minute}"
    string_weekdey = f"{days_of_week[now.weekday()]}"

    context = {
        'date': 
    }

    return render(request, 'theme.html', context)