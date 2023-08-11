from django.contrib import admin
from ubicaciones.models import Dependencia
class AdminDependencia(admin.ModelAdmin):
    list_display = ('id_dep', 'nom_dep', 'longitud','latitud')
admin.site.register(Dependencia, AdminDependencia)
