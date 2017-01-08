from django.contrib import admin
from .models import *
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.



class PatientAdmin(MarkdownModelAdmin):

#        prepopulated_fields = {"slug": ("name","birth")}
        list_display = ("name","birth","adresse", "phone", "first_consultation")
        list_filter = ('adresse', 'gender', 'assurance')
        search_fields = ('name','phone')

class ConsultationAdmin(MarkdownModelAdmin):

        list_display = ("patient", "medecin", "consultation_date", "emergency", "dispositions", "ordonnance")
        list_filter = ('consultation_date', 'emergency', 'medecin','patient',)

class StressAdmin(MarkdownModelAdmin):

        list_display = ("patient", "referent", "stress_date", "maximale", "conclusion", "disposition")
        list_filter = ('stress_date', 'patient',)


admin.site.register(Patient, PatientAdmin)
admin.site.register(Motif)
admin.site.register(Wilaya)
admin.site.register(Consultation, ConsultationAdmin)
admin.site.register(Stress, StressAdmin)
admin.site.register(Tag)
