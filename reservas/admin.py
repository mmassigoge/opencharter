from django.contrib import admin

from reservas.models import Vehiculo, Chofer, Viaje, Pasajero, Reserva
from django.forms.models import BaseInlineFormSet

from datetime import datetime
class ViajeInlineFormset(BaseInlineFormSet):
    def get_queryset(self):
        if not hasattr(self, '_queryset'):
            qs = super(ViajeInlineFormset, self).get_queryset().filter(viaje__fecha_hora__gte=datetime.now())
            self._queryset = qs
        return self._queryset
    
    def add_fields(self, form, index):
        super(ViajeInlineFormset, self).add_fields(form, index)

        form.fields['viaje'].queryset = Viaje.objects.filter(fecha_hora__gte=datetime.now())

class ReservaInline(admin.TabularInline):
    model = Reserva
    formset = ViajeInlineFormset
    #fields = ['viaje',]
    
class PasajeroAdmin(admin.ModelAdmin):
    fields = (('dni','nombre','fecha_nacimiento'),('email', 'clave'))
    inlines = [ReservaInline,]
    list_display = ['dni','nombre', 'email',]
    list_display_links = ['dni','nombre', 'email',]
    search_fields = ['dni','nombre', 'email',]

admin.site.register(Vehiculo)
admin.site.register(Chofer)
admin.site.register(Viaje)
admin.site.register(Pasajero,PasajeroAdmin)
admin.site.register(Reserva)