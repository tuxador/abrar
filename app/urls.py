from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from .views import ListPatients, DetailPatient, CreatePatient, consultation_pdf
from .models import Patient, Consultation
urlpatterns = [
    url(r'^$', ListPatients.as_view(), name='patients'),
    url(r'(?P<pk>\d+)/$', DetailPatient.as_view(), name='detail_patient'),
    url(r'nouveau/patient/$', CreatePatient.as_view(), name='create_patient'),
#    url('^markdown/', include( 'django_markdown.urls')),
    url(r'(?P<pk1>\d+)/consultation(?P<pk2>\d+)\.pdf$', consultation_pdf, name='consultation_pdf'),
  #  url(r'patient/(?P<pk1>\d+)/alternative(?P<pk2>\d+)\.pdf$', alternative_pdf, name='alternative_pdf'),
##    url(r'^(?P<slug>[\w\-]+)$', views.ShowProfile.as_view(),name='patient'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
