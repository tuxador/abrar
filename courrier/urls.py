from django.conf.urls import url, include
from django.conf import settings
from .models import Courrier, Certificat, Arret, Stomato, Ordonnance
from .views import courrier_pdf, arret_pdf, ordonnance_pdf, stomato_pdf, certificat_pdf


urlpatterns = [
    url(r'(?P<pk1>\d+)/stomato(?P<pk2>\d+)\.pdf$', stomato_pdf, name='stomato_pdf'),
    url(r'(?P<pk1>\d+)/certificat(?P<pk2>\d+)\.pdf$', certificat_pdf, name='certificat_pdf'),
    url(r'(?P<pk1>\d+)/courrier(?P<pk2>\d+)\.pdf$', courrier_pdf, name='courrier_pdf'),
    url(r'(?P<pk1>\d+)/ordonnance(?P<pk2>\d+)\.pdf$', ordonnance_pdf, name='ordonnance_pdf'),
    url(r'(?P<pk1>\d+)/arret(?P<pk2>\d+)\.pdf$', arret_pdf, name='arret_pdf'),
]

