from django.conf.urls import patterns, include, url
from reservas.admin import user_admin_site

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^vendedores/', include(user_admin_site.urls)),    
    (r'^pasajeros/', include('reservas.urls')),
)
