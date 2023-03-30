from django.contrib import admin
from notificaciones.models import Notificacion
# Register your models here.
class AdminNotificacio(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'link')
admin.site.register(Notificacion,AdminNotificacio )
