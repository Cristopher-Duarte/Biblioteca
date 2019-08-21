from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Libro

def cargar_inicio(request):
    return render(request,"miapp/index.html")

class LibroList(ListView):
    model = Libro 
    template_name = 'miapp/lista_libros.html'


def perro(request):
    return HttpResponse("<h1><center>Guau</center></h1>")
