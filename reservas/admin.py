from django.contrib import admin

from reservas.models import Vehiculo, Chofer, Viaje, Pasajero, Reserva

admin.site.register(Vehiculo)
admin.site.register(Chofer)
admin.site.register(Viaje)
admin.site.register(Pasajero)
admin.site.register(Reserva)

############################################################
#Definiciones para creacion de Admin para usuarios no staff#
############################################################

from django.contrib.admin.sites import AdminSite
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import ugettext_lazy
from django.contrib.admin.forms import ERROR_MESSAGE
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
 
class UserAdminAuthenticationForm(AuthenticationForm):
    """
    Same as Django's AdminAuthenticationForm but allows to login
    any user who is not staff.
    """
    this_is_the_login_form = forms.BooleanField(widget=forms.HiddenInput,
                                initial=1,
                                error_messages={'required': ugettext_lazy(
                                "Please log in again, because your session has"
                                " expired.")})
 
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        message = ERROR_MESSAGE
         
        if username and password:
            self.user_cache = authenticate(username=username,password=password)
            if self.user_cache is None:
                if u'@' in username:
                    # Mistakenly entered e-mail address instead of username?
                    # Look it up.
                    try:
                        user = User.objects.get(email=username)
                    except (User.DoesNotExist, User.MultipleObjectsReturned):
                        # Nothing to do here, moving along.
                        pass
                    else:
                        if user.check_password(password):
                            message = _("Your e-mail address is not your "
                                        "username."
                                        " Try '%s' instead.") % user.username
                raise forms.ValidationError(message)
            # Removed check for is_staff here!
            elif not self.user_cache.is_active:
                raise forms.ValidationError(message)
        self.check_for_test_cookie()
        return self.cleaned_data

class UserAdmin(AdminSite):
    login_form = UserAdminAuthenticationForm
    def has_permission(self, request):
        return request.user.is_active
    
user_admin_site = UserAdmin(name='usersadmin')

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
    
class PasajeroAdmin(admin.ModelAdmin):
    fields = (('dni','nombre','fecha_nacimiento'),('email', 'clave'))
    inlines = [ReservaInline,]
    list_display = ['dni','nombre', 'email',]
    list_display_links = ['dni','nombre', 'email',]
    search_fields = ['dni','nombre', 'email',]
    
user_admin_site.register(Pasajero,PasajeroAdmin)
