from django.contrib import admin

from pre_frecuentes.models import *
admin.site.site_header = 'Administración App-Ulagos'
# Register your models here.
class PersonalizarPreguntas(admin.ModelAdmin):

    list_display = ('titulo', 'respuesta', 'categoria')

admin.site.register(Pregunta, PersonalizarPreguntas)
admin.site.register(Categoria)
