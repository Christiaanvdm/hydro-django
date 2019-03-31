
from django.shortcuts import (
    render,
)

# Create your views here.


def home(request):
    return render(request, 'home.html')


def hydropt(request, x_coord, y_coord):
    x = x_coord
    y = y_coord
    context = {'x': x, 'y': y}
    return render(request, 'home.html', context=context)
