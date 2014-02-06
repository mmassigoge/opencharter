from django.views.generic.base import TemplateView
from django.contrib import messages
from .models import Pasajero
from django.http.response import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

class HomePageView(TemplateView):
    template_name = 'reservas/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context
    
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        clave = request.POST.get('clave')
        try:
            pasajero = Pasajero.objects.get(email__iexact=email,clave__exact=clave)
            request.session['pasajero_id'] = pasajero.id
            return HttpResponseRedirect('/reservas/reservas_pasajero')
        except ObjectDoesNotExist:
            messages.error(self.request, 'email o clave incorrecta')
            return HttpResponseRedirect('/reservas/reservas')

class ReservasView(TemplateView):
    template_name = 'reservas/reservas.html'

    def get_context_data(self, **kwargs):
        context = super(ReservasView, self).get_context_data(**kwargs)
        pasajero = Pasajero.objects.get(id=self.request.session['pasajero_id'])
        context['reservas_list'] = pasajero.reserva_set.all()
        return context
