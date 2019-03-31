# coding=utf-8
from django.urls import path
from .views import views

urlpatterns = [
# providers/<int:provider_id>/
    path('',
         views.home,
         name='home'),
    path('<str:x_coord>/<str:y_coord>',
         views.hydropt,
         name='hydropt'),
]
