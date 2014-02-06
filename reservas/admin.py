from django.contrib import admin

from reservas.models import Vehiculo, Chofer, Viaje, Pasajero, Reserva

admin.site.register(Vehiculo)
admin.site.register(Chofer)
admin.site.register(Viaje)
admin.site.register(Pasajero)
admin.site.register(Reserva)