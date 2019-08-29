from django.contrib import admin
from .models import *

admin.site.register(Libro)
#admin.site.register(Prestamo)
admin.site.register(Ejemplar)
admin.site.register(DetallelPrestamo)

class DetallelPrestamoInline(admin.TabularInline):
    model = DetallelPrestamo

class PrestamoAdmin(admin.ModelAdmin):
    inlines = [
        DetallelPrestamoInline,
    ]

admin.site.register(Prestamo,PrestamoAdmin)