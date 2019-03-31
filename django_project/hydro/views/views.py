
from django.shortcuts import (
    render,
)
from django.http import HttpResponse


# Create your views here.


def home(request):
    return render(request, 'home.html')


def hydropt(request, x_coord, y_coord):
    x = x_coord
    y = y_coord

    context = {'x': x, 'y': y}

    return HttpResponse(request, 'home.html', context=context)


