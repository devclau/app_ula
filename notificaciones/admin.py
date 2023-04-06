from django.contrib import admin
# Register your models here
from notificaciones.models import Notificacion
class AdminNotificacion(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'link')
admin.site.register(Notificacion, AdminNotificacion)