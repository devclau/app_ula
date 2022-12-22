from django.contrib import admin
from ubicaciones.models import *

admin.site.register(Sede)
class DiasHorasInline(admin.TabularInline):
    model = DiasHora
    extra = 1
    autocomplete_fields = ['diasemamna']


class DiaSemanaAdmin(admin.ModelAdmin):
    
    search_fields = ('nombre'),
    ordering = ['nombre']
    
    def has_module_permission(self, request):
        return False
    
admin.site.register(DiaSemana, DiaSemanaAdmin)


admin.site.register(Reparticion)
admin.site.register(Ciudad)
admin.site.register(Espacio)
admin.site.register(Servicio)
admin.site.register(Contacto)


class SedeReparticionAdmin(admin.ModelAdmin):
    inlines = [DiasHorasInline,]
    list_display = ('sede', 'reparticion','ciudad','espacio', 'servicio', 'contacto')
    
    fieldsets = (
        (None, {
            'fields': ('sede', 'reparticion', 'espacio')
        }),
        ('Servicios y Contacto', {
            'fields': ('servicio', 'contacto')
        }),
    )
    
admin.site.register(SedeRaparticion, SedeReparticionAdmin)

