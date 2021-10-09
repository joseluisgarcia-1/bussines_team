from django.contrib import admin
from apps.mascota.views import index
from django.urls import path, re_path, include

urlpatterns = [
    path('', index, name='index'),
]
