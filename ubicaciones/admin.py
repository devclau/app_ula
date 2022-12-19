from django.contrib import admin
from ubicaciones.models import *

# Register your models here.



class SedeReparticionAdmin(admin.ModelAdmin):
    list_display = ('sede', 'reparticion')
admin.site.register(SedeRaparticion, SedeReparticionAdmin)




admin.site.register(Sede)


class DiasHorasInline(admin.TabularInline):
    model = DiasHora
    extra = 1
    autocomplete_fields = ['diasemamna']


class DiaSemanaAdmin(admin.ModelAdmin):
    inlines = (DiasHorasInline,)
    search_fields = ('nombre'),
    ordering = ['nombre']
    
    def has_module_permission(self, request):
        return False
    
admin.site.register(DiaSemana, DiaSemanaAdmin)


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
    inlines = [DiasHorasInline,]
    list_display = ('reparticion_sede', 'espacio', 'servicio', 'contacto')
    
    fieldsets = (
        (None, {
            'fields': ('reparticion_sede', 'espacio')
        }),
        ('Servicios y Contacto', {
            'fields': ('servicio', 'contacto')
        }),
    )
admin.site.register(ReparticionEspacio, ReparticionEspacioAdmin)
