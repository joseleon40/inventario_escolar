from django.contrib import admin
from .models import Equipo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'estado', 'fecha_ingreso', 'ubicacion')
    search_fields = ('nombre', 'categoria', 'ubicacion')
    list_filter = ('categoria', 'estado', 'ubicacion')
