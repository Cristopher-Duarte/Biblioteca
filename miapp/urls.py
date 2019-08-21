
from django.urls import path
from miapp.views import *

urlpatterns = [
    path('',cargar_inicio, name='Inicio'),
    path('libro/',LibroList.as_view(), name='Listar_libros'),
    path('libro/nuevo/',LibroCreate.as_view(),name='Nuevo_libro'),
]
