from django.views.generic.base import TemplateView
from django.contrib import messages
from datetime import datetime
from django.http.response import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Pasajero

class HomePageView(TemplateView):
    template_name = 'reservas/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context
    
    def post(self, request, *args, **kwargs):
        if('pasajero_id' in request.session):
            del request.session['pasajero_id']
        email = request.POST.get('email')
        clave = request.POST.get('clave')
        try:
            pasajero = Pasajero.objects.get(email__iexact=email,clave__exact=clave)
            request.session['pasajero_id'] = pasajero.id
            return HttpResponseRedirect('/reservas/reservas_pasajero')
        except ObjectDoesNotExist:
            messages.error(request, 'email o clave incorrecta')
            return HttpResponseRedirect('/reservas')

class ReservasView(TemplateView):
    template_name = 'reservas/reservas.html'

    def get_context_data(self, **kwargs):
        context = super(ReservasView, self).get_context_data(**kwargs)
        if('pasajero_id' in self.request.session):
            pasajero = Pasajero.objects.get(id=self.request.session['pasajero_id'])
            now = datetime.now()
            context['reservas_list'] = pasajero.reserva_set.filter(viaje__fecha_hora__gte=now)
        else:
            messages.error(self.request, 'pasajero no identificado')
            context['reservas_list'] = []
        return context
