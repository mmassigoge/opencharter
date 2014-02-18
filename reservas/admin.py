from django.contrib import admin

from reservas.models import Vehiculo, Chofer, Viaje, Pasajero, Reserva


class ReservaInline(admin.TabularInline):
    model = Reserva
    fields = ['viaje',]
    
class PasajeroAdmin(admin.ModelAdmin):
    fields = (('dni','nombre','fecha_nacimiento'),('email', 'clave'))
    inlines = [
        ReservaInline,
    ]
    list_display = ['dni','nombre', 'email',]
    list_display_links = ['dni','nombre', 'email',]
    search_fields = ['dni','nombre', 'email',]

admin.site.register(Vehiculo)
admin.site.register(Chofer)
admin.site.register(Viaje)
admin.site.register(Pasajero,PasajeroAdmin)
admin.site.register(Reserva)