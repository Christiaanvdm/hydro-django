import json
from django.shortcuts import (
    render,
)
from django.http import HttpResponse
from hydro.views.hydropts import get_geojson
from hydro.models import


# Create your views here.


def home(request):
    return render(request, 'home.html')


def hydropt(request, x_coord, y_coord):
    x = x_coord
    y = y_coord
    response = json.dumps(get_geojson())
    return HttpResponse(response)
    # return HttpResponse(get_geojson())
    # context = {'x': x, 'y': y}
    # return render(request, 'home.html')

