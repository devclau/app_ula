from django.contrib import admin

from pre_frecuentes.models import Pregunta
admin.site.site_header = 'Administracion App-Ulagos'
# Register your models here.
class PersonalizarPreguntas(admin.ModelAdmin):

    list_display = ('titulo', 'respuesta')

admin.site.register(Pregunta, PersonalizarPreguntas)
