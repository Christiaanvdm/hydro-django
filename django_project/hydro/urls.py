# coding=utf-8
from django.urls import path
from hydro.views import views

urlpatterns = [
    path('providers/<int:provider_id>/',
         views.home,
         name='show_provider')]
