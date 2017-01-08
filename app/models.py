from django.db import models
from datetime import datetime
from django.utils import timezone
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify
# Create your models here.

class   Wilaya(models.Model):
                wilaya = models.CharField(max_length=25)

                def __str__(self):
                    return(self.wilaya)


class   Motif(models.Model):
                motif = models.CharField(verbose_name="motif d'admission", max_length=25)

                def __str__(self):
                    return(self.motif)

class   Tag(models.Model):
                tag = models.CharField(max_length=50, blank=True)

                def __str__(self):
                    return(self.tag)


class   Patient(models.Model):
                name = models.CharField(verbose_name="Nom et prénoms", max_length=50)
                birth = models.DateField(verbose_name="date de naissance")

                GENDER_CHOICES = (
                     ('M', 'Masculin'),
                     ('F', 'Féminin'),
                )
                gender = models.CharField(verbose_name="sexe", max_length=1, choices=GENDER_CHOICES)
                adresse = models.ForeignKey(Wilaya, on_delete=models.CASCADE,blank=True, null=True)
                phone = models.CharField("Téléphone", max_length=10, default='0550123456')
                PROFESSION_CHOICES = (
                     ('F', 'fonctionnaire'),
                     ('E', 'employé'),
                     ('C', 'commerçant'),
                     ('Y', 'femme au foyer'),
                     ('T', 'étudiant'),
                     ('D', 'cadre'),
                     ('L', 'profession libérale'),
                     ('O', 'au chômage'),
                )
                profession = models.CharField(verbose_name="Profession", max_length=1, choices=PROFESSION_CHOICES)

                ASSURANCE_CHOICES = (
                     ('N', 'CNAS'),
                     ('S', 'CASNOS'),
                     ('A', 'Autre'),
                     ('O', 'Non assuré'),
                )
                assurance = models.CharField(verbose_name="Assurance sociale", max_length=1, choices=ASSURANCE_CHOICES)
                correspondant = models.CharField("Médecin correspondant", max_length=255, blank=True)
                first_consultation = models.DateField("première consultation", default=timezone.now)
# antécedents et FDR
                hypertension = models.BooleanField("hypertendu(e)", default=True)
                diabete = models.BooleanField("diabétique", default=True)
                dyslipidemia = models.BooleanField("dyslipidémie", default=True)
                smoker = models.BooleanField("tabagique", default=False)
                weight = models.PositiveSmallIntegerField(verbose_name="poids", blank=True)
                lenght = models.DecimalField(max_digits=3, decimal_places=2, default=1.70)
                #bmi = weight/lenght*lenght
                obesity = models.BooleanField("obèse", default=True)
                sedentarity = models.BooleanField("sédentarité", default=True)
                heredity = models.BooleanField("hérédité coronarienne", default=False)
                history = models.TextField("antécedents")
                allergy = models.CharField("allergie connue", max_length=50, blank=True)
                tags = models.ManyToManyField(Tag, default="cardio")

              #  def save(self, *args, **kwargs):
              #                  super(Patient, self).save(*args, **kwargs)
              #                  if not self.slug:
              #                                  self.slug = slugify("%s %s",(self.name,self.id))
               #                                 self.save()


                class Meta:
                    ordering = ['name']

                def get_absolute_url(self):
                    return reverse('detail_patient', kwargs={'pk': self.pk})

                def __str__(self):
                    return(self.name)

class   Consultation(models.Model):

# données générales et symptomatologie

                patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
                consultation_date = models.DateField("date de consultation")
                medecin = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True)
                emergency = models.BooleanField("urgence", default=False)
                motif_consultation = models.ManyToManyField(Motif)
                fever = models.BooleanField("fièvre", default=False)
                dyspnea_nyha = models.PositiveSmallIntegerField("stade NYHA", default='1')
                angina_scc = models.PositiveSmallIntegerField("stade d'angor", default='1')
                syncope = models.BooleanField("Syncope", default=False)
                histoire = models.CharField("Histoire de la maladie", max_length=255 ,null=True, blank=True)

# examen clinique

                systolic_bp = models.PositiveSmallIntegerField(blank=True, null=True)
                diastolic_bp = models.PositiveSmallIntegerField(blank=True, null=True)
                heart_rate = models.PositiveSmallIntegerField(blank=True, null=True)
                auscultation = models.CharField(max_length=50, blank=True, null=True)
                ivg = models.BooleanField(default=False)
                ivd = models.BooleanField(default=False)
                pulse = models.CharField(max_length=50, blank=True)
                telethorax = models.CharField(max_length=50, blank=True, null=True)

                # ECG

                RYTHM_CHOICES = (
                    ('S', 'Sinusal'),
                    ('F', 'Atrial Fibrillation'),
                    ('R', 'Atrial Flutter'),
                    ('P', 'Pace Maker'),
                    ('T', 'TV')
                )
                rythm = models.CharField(max_length=1, choices=RYTHM_CHOICES)
                freq = models.PositiveSmallIntegerField(default='70')
                BLOCK_CHOICES = (
                    ('D', 'BBD'),
                    ('G', 'BBG')
                    )
                bundle_block = models.CharField(max_length=1, choices=BLOCK_CHOICES, blank=True, null=True)

                hypertrophy = models.NullBooleanField(default=False)
                TERRITORY = (
                    ('N', 'Null'),
                    ('S', 'Septal'),
                    ('A', 'Anterior'),
                    ('L', 'Lateral'),
                    ('P', 'Posterior'),
                )
                necrosis = models.CharField(max_length=1, choices=TERRITORY)
                ischaemia = models.CharField(max_length=1, choices=TERRITORY)
                lesion = models.CharField(max_length=1, choices=TERRITORY)
                t_inversion = models.CharField(max_length=1, choices=TERRITORY)
                corrected_qt = models.IntegerField(default=400)
#echocoeur
                echocoeur = models.TextField("échocardiographie", null=True, blank=True)
                date_echo = models.DateField("Date de l'écho", default=timezone.now)
                eto = models.TextField("échocardiographie trans-oesophagienne", null=True, blank=True)

                fevg = models.PositiveSmallIntegerField("FeVG", blank=True, null=True)

#evolution

                resume = models.TextField("résumé clinique", null=True)

# ordonnance de sortie
                dispositions = models.CharField("dispositions complémentaires", max_length=255, blank=True)
                ordonnance = models.TextField("ordonnance", blank=True, null=True)


                def __str__(self):

                    return '%s %s' % (self.patient, self.consultation_date)
               # def get_absolute_url(self):
                #    return reverse('detail_consultation', kwargs={'pk':self.pk})


class   Stress(models.Model):

# données générales et symptomatologie

                patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
                stress_date = models.DateField("Date du stress-echo", default=timezone.now)
                referent = models.CharField("Médecin référent", max_length=50, blank=True)
                medecin = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True)
                motif_stress = models.ManyToManyField(Motif)
                medication = models.CharField("traitement habituel", max_length=255, blank=True)
                OBJECTIF_CHOICES = (
                    ('I', 'Ischémie'),
                    ('V', 'Viabilité'),
                    ('R', 'Réserve contractile'),
                    ('G', 'Gradient trans-aortique'),
                    ('M', 'Fuite mitrale')
                )
                objectif = models.CharField(max_length=1, choices=OBJECTIF_CHOICES)
# examen de base

                base_systolic_bp = models.PositiveSmallIntegerField("PAS base", blank=True, null=True)
                base_diastolic_bp = models.PositiveSmallIntegerField("PAD base", blank=True, null=True)
                base_heart_rate = models.PositiveSmallIntegerField("FC base", blank=True, null=True)
                base_ecg = models.CharField("ECG base", max_length=255, blank=True, null=True)
                base_echo = models.CharField("écho de base", max_length=255, blank=True, null=True)
# low dose
                low_symptoma = models.CharField("Symptômes low dose", max_length=255, blank=True, null=True)
                low_systolic_bp = models.PositiveSmallIntegerField("PAS low dose", blank=True, null=True)
                low_diastolic_bp = models.PositiveSmallIntegerField("PAD low dose", blank=True, null=True)
                low_heart_rate = models.PositiveSmallIntegerField("FC low dose", blank=True, null=True)
                low_ecg = models.CharField("ECG low dose", max_length=255, blank=True, null=True)
                low_echo = models.CharField("écho low dose", max_length=255, blank=True, null=True)
# peak dose
                peak_symptoma = models.CharField("Symptômes peak dose", max_length=255, blank=True, null=True)
                peak_systolic_bp = models.PositiveSmallIntegerField("PAS peak dose", blank=True, null=True)
                peak_diastolic_bp = models.PositiveSmallIntegerField("PAD peak dose", blank=True, null=True)
                peak_heart_rate = models.PositiveSmallIntegerField("FC peak dose", blank=True, null=True)
                peak_ecg = models.CharField("ECG low dose", max_length=255, blank=True, null=True)
                peak_echo = models.CharField("écho peak dose", max_length=255, blank=True, null=True)
# Récupération
                recup_symptoma = models.CharField("Symptômes low dose", max_length=255, blank=True, null=True)
                recup_systolic_bp = models.PositiveSmallIntegerField("PAS low dose", blank=True, null=True)
                recup_diastolic_bp = models.PositiveSmallIntegerField("PAD low dose", blank=True, null=True)
                recup_heart_rate = models.PositiveSmallIntegerField("FC low dose", blank=True, null=True)
                recup_ecg = models.CharField("ECG low dose", max_length=255, blank=True, null=True)
                recup_echo = models.CharField("écho de récupération", max_length=255, blank=True, null=True)

#evolution

                maximale = models.BooleanField("épreuve maximale", default=True)
                conclusion = models.TextField("Conclusion", blank=True)
                DISPOSITION_CHOICES = (
                    ('M', 'Traitement médical'),
                    ('C', 'Coronarographie diagnostique'),
                    ('R', 'Coronarographie et éventuel geste de revascularisation'),
                    ('N', 'Non concluante'),
                )
                disposition = models.CharField("Dispositions complémentaires", max_length=1, choices=DISPOSITION_CHOICES, default='M')


                def __str__(self):

                    return '%s %s' % (self.patient, self.stress_date)
