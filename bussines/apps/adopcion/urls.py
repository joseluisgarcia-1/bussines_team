from django.contrib import admin
from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete
from django.urls import path, re_path, include

urlpatterns = [
    path('', index_adopcion, name='inicio'),
    path('solicitud/listar', SolicitudList.as_view(), name='solicitud_listar'),
    path('solicitud/nueva', SolicitudCreate.as_view(), name='solicitud_crear'),
    path('solicitud/editar/<pk>/', SolicitudUpdate.as_view(), name='solicitud_editar'),
    path('solicitud/eliminar/<pk>/', SolicitudDelete.as_view(), name='solicitud_eliminar'),
]
