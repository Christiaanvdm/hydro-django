import json
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    render_to_response
)
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')
