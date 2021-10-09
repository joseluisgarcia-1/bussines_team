from django.contrib import admin
from apps.adopcion.views import index_adopcion
from django.urls import path, re_path, include

urlpatterns = [
    path('', index_adopcion),
]
