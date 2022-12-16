from django.contrib import admin
from ubicaciones.models import *

# Register your models here.



class SedeReparticionAdmin(admin.ModelAdmin):
    list_display = ('sede', 'reparticion')
admin.site.register(SedeRaparticion, SedeReparticionAdmin)



class UsoAdmin(admin.ModelAdmin):
 def has_module_permission(self, request):
        return False
admin.site.register(Uso, UsoAdmin)


admin.site.register(Sede)

class ReparticionAdmin(admin.ModelAdmin):
 def has_module_permission(self, request):
        return False
admin.site.register(Reparticion,ReparticionAdmin)

class EspacioAdmin(admin.ModelAdmin):
 def has_module_permission(self, request):
        return False
admin.site.register(Espacio, EspacioAdmin)

class ServicioAdmin(admin.ModelAdmin):
 def has_module_permission(self, request):
        return False
admin.site.register(Servicio, ServicioAdmin)

class ContactoAdmin(admin.ModelAdmin):
 def has_module_permission(self, request):
        return False
admin.site.register(Contacto, ContactoAdmin)

class ReparticionEspacioAdmin(admin.ModelAdmin):
    list_display = ('reparticion_sede', 'espacio', 'contacto', 'uso', 'servicio')
admin.site.register(ReparticionEspacio, ReparticionEspacioAdmin)
