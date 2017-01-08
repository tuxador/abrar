from django.db import models
from app.models import Patient, Motif
from datetime import datetime
from django.utils import timezone
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify
#
# Create your models here.
class   Ordonnance(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    ordonnance_date = models.DateField("Date", default=timezone.now())
    medoc1 = models.CharField(max_length=50, blank=True, null=True)
    poso1 = models.CharField(max_length=25, blank=True, null=True)
    qsp1 = models.CharField(max_length=10, blank=True, null=True)
    medoc2 = models.CharField(max_length=50, blank=True, null=True)
    poso2 = models.CharField(max_length=25, blank=True, null=True)
    qsp2 = models.CharField(max_length=10, blank=True, null=True)
    medoc3 = models.CharField(max_length=50, blank=True, null=True)
    poso3 = models.CharField(max_length=25, blank=True, null=True)
    qsp3 = models.CharField(max_length=10, blank=True, null=True)
    medoc4 = models.CharField(max_length=50, blank=True, null=True)
    poso4 = models.CharField(max_length=25, blank=True, null=True)
    qsp4 = models.CharField(max_length=10, blank=True, null=True)
    medoc5 = models.CharField(max_length=50, blank=True, null=True)
    poso5 = models.CharField(max_length=25, blank=True, null=True)
    qsp5 = models.CharField(max_length=10, blank=True, null=True)
    medoc6 = models.CharField(max_length=50, blank=True, null=True)
    poso6 = models.CharField(max_length=25, blank=True, null=True)
    qsp6 = models.CharField(max_length=10, blank=True, null=True)
    medoc7 = models.CharField(max_length=50, blank=True, null=True)
    poso7 = models.CharField(max_length=25, blank=True, null=True)
    qsp7 = models.CharField(max_length=10, blank=True, null=True)
    medoc8 = models.CharField(max_length=50, blank=True, null=True)
    poso8 = models.CharField(max_length=25, blank=True, null=True)
    qsp8 = models.CharField(max_length=10, blank=True, null=True)
    medoc9 = models.CharField(max_length=50, blank=True, null=True)
    poso9 = models.CharField(max_length=25, blank=True, null=True)
    qsp9 = models.CharField(max_length=10, blank=True, null=True)
    medoc10 = models.CharField(max_length=50, blank=True, null=True)
    poso10 = models.CharField(max_length=25, blank=True, null=True)
    qsp10 = models.CharField(max_length=10, blank=True, null=True)
    medoc11 = models.CharField(max_length=50, blank=True, null=True)
    poso11 = models.CharField(max_length=25, blank=True, null=True)
    qsp11 = models.CharField(max_length=10, blank=True, null=True)
    medoc12 = models.CharField(max_length=50, blank=True, null=True)
    poso12 = models.CharField(max_length=25, blank=True, null=True)
    qsp12 = models.CharField(max_length=10, blank=True, null=True)
    medoc13 = models.CharField(max_length=50, blank=True, null=True)
    poso13 = models.CharField(max_length=25, blank=True, null=True)
    qsp13 = models.CharField(max_length=10, blank=True, null=True)
    medoc14 = models.CharField(max_length=50, blank=True, null=True)
    poso14 = models.CharField(max_length=25, blank=True, null=True)
    qsp14 = models.CharField(max_length=10, blank=True, null=True)
    medoc15 = models.CharField(max_length=50, blank=True, null=True)
    poso15 = models.CharField(max_length=25, blank=True, null=True)
    qsp15 = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):

        return '%s %s' % (self.patient, self.ordonnance_date)

 #               def get_absolute_url(self):
 #                   return reverse('detail_coronarographie', kwargs={'pk': self.pk})



class Certificat(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    correspondant = models.CharField("Correspondant", max_length=50, blank=True, null=True)
    certificat_date = models.DateField("Date", default=timezone.now())
    motif = models.CharField("Motif", max_length=100, blank=True, null=True)
    declaration = models.CharField("Déclare que", max_length=255, blank=True, null=True)
    closing = models.CharField("Closing", max_length=100, blank=True, null=True)

    def __str__(self):

        return '%s %s' % (self.patient, self.certificat_date)

class Courrier(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    correspondant = models.CharField("Correspondant", max_length=50, blank=True, null=True)
    SALUTATION_CHOICES = (
                     ('C', 'Cher confrère'),
                     ('A', 'Cher ami'),
                     ('S', 'Chère consoeur'),
                     ('B', 'Cher confrère, chère consoeur'),
                     ('M', 'Cher maître'),
                )
    salutation = models.CharField("Salutation", max_length=1, choices=SALUTATION_CHOICES)
    courrier_date = models.DateField("Date", default=timezone.now())
    reponse = models.BooleanField(default=False)
    diagnostic = models.CharField("Diagnostic", max_length=100, blank=True, null=True)
    declaration = models.CharField("Déclare que", max_length=255, blank=True, null=True)

    closing = models.CharField("Closing", max_length=100, blank=True, null=True)

    def __str__(self):

        return '%s %s %s' % (self.patient, self.courrier_date, self.correspondant)


class Stomato(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    stomato_date = models.DateField("Date", default=timezone.now())
    diagnostic = models.CharField("Diagnostic", max_length=100, blank=True, null=True)
    RISK_CHOICES = (
                     ('F', 'faible'),
                     ('M', 'modéré'),
                     ('I', 'important'),
                )
    infectious_risk = models.CharField(verbose_name="Risque infectieux", max_length=1, choices=RISK_CHOICES, default='F')
    thrombotic_risk = models.CharField(verbose_name="Risque thrombo-embolique", max_length=1, choices=RISK_CHOICES, default='F')
    syncopal_risk = models.CharField(verbose_name="Risque syncopal", max_length=1, choices=RISK_CHOICES, default='F')
    inr_cible = models.FloatField(verbose_name="INR Cible", default=1.0)
    avk_interruption = models.NullBooleanField()
    atb = models.NullBooleanField(verbose_name="antibioprophylaxie", default=False)
    prescription = models.CharField("Antbiothérapie", max_length=255, blank=True, null=True)

    def __str__(self):

        return '%s %s' % (self.patient, self.stomato_date)

class Arret(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    arret_date = models.DateField("Date du début", default=timezone.now())
    ARRET_CHOICES = (
                     ('A', 'arrêt de travail'),
                     ('P', 'prolongation'),
                     ('R', 'reprise'),
                )
    type_arret = models.CharField(verbose_name="Type de certifict", max_length=1, choices=ARRET_CHOICES)
    duree = models.PositiveSmallIntegerField("durée", blank=True, null=True)
    redaction_date = models.DateField("délivré le", default=timezone.now())

    def __str__(self):

        return '%s %s' % (self.patient, self.redaction_date)

