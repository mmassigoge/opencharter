from django.conf.urls import patterns, url
from .views import HomePageView, ReservasView

urlpatterns = patterns('',
    url(r'^reservas_pasajero', ReservasView.as_view()),
    url(r'^', HomePageView.as_view()),
)