from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from .models import Patient, Consultation, Stress
from courrier.models import Courrier, Certificat, Arret, Stomato #, Ordonnance
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.shortcuts  import render_to_response, redirect
from django.shortcuts import get_object_or_404
from django.template import Context
from django.template.loader import get_template #render_to_string
from reportlab.platypus import PageTemplate, BaseDocTemplate, NextPageTemplate, PageBreak
from subprocess import Popen, PIPE
import tempfile
import os
from io import StringIO
import operator
from django.db.models import Q
from six.moves import reduce
# Create your views here.

class HomePage(TemplateView):
    template_name = "index.html"


class AboutPage(TemplateView):
    template_name = "about.html"


class ListPatients(ListView):
    model = Patient
    context_object_name = 'patients'

class CreatePatient(CreateView):
    model = Patient
    fields = '__all__'
    template_name = "app/create_patient.html"
    success_url = reverse_lazy('clinique:patients')

class DetailPatient(DetailView):
    model = Patient
    context_object_name = 'patient'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetailPatient, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
#        context['admissions'] = Admission.objects.filter(patient=self.object)
        context['consultations'] = Consultation.objects.filter(patient=self.object)
#        context['ordonnances'] = Ordonnance.objects.filter(patient=self.object)
        context['stomatos'] = Stomato.objects.filter(patient=self.object)
        context['courriers'] = Courrier.objects.filter(patient=self.object)
        context['certificats'] = Certificat.objects.filter(patient=self.object)
        context['arrets'] = Arret.objects.filter(patient=self.object)
        context['stresses'] = Stress.objects.filter(patient=self.object)
#        context['coronarographies'] = Coronarographie.objects.filter(patient=self.object)
#        context['stimulations'] = Stimulation.objects.filter(patient=self.object)
        return context


class PatientSearchListView(ListPatients):
    """
    Display the patient List page filtered by the search query.
    """
    paginate_by = 10

    def get_queryset(self):
        result = super(PatientSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(phone__icontains=q) for q in query_list))
                # reduce(operator.and_,
                       # (Q(tags__icontains=q) for q in query_list))
            )

        return result

def consultation_pdf(request, pk2, pk1):
    entry = Consultation.objects.get(pk=pk2)
    source = Patient.objects.get(pk=pk1)
    context = Context({ 'consultation': entry, 'patient': source })
    template = get_template('app/consultation.tex')
    rendered_tpl = template.render(context, request).encode('utf-8')
    # Python3 only. For python2 check out the docs!
    with tempfile.TemporaryDirectory() as tempdir:
        # Create subprocess, supress output with PIPE and
        # run latex twice to generate the TOC properly.
        # Finally read the generated pdf.
        for i in range(2):
            process = Popen(
                ['xelatex', '-output-directory', tempdir],
                stdin=PIPE,
                stdout=PIPE,
            )
            process.communicate(rendered_tpl)
        with open(os.path.join(tempdir, 'texput.pdf'), 'rb') as f:
            pdf = f.read()
    r = HttpResponse(content_type='application/pdf')
    r.write(pdf)
    return r


# def alternative_pdf(request, pk2, pk1):
#     title = get_object_or_404(Consultation, pk=pk2).patient

#     template_file = 'app/consultation.tex'
#     t = get_template(template_file)
#     entry = Certificat.objects.get(pk=pk2)
#     source = Patient.objects.get(pk=pk1)
#     context = Context({ 'certificat': entry, 'patient': source })
#         f.write(smart_str(t.render(context)))
#     return HttpResponseRedirect('/app/%s.pdf' % consultation.patient)


# Reportlab stuff
#
# def headerFooterLayout(canvas, doc):
#     canvas.saveState()
#     canvas.setPageSize(self.pagesize)
#     # add header/footer
#     canvas.restoreState()

# def emptyLayout(canvas, doc):
#     canvas.saveState()
#     canvas.setPageSize(self.pagesize)
#     canvas.restoreState()

# pHeight, pWidth = self.pagesize
# myFrame = Frame(0, 0, pHeight, pWidth, id='myFrame')

# headerFooterTemplate = PageTemplate(id='headerFooterTemplate',
#                                     frames=[myFrame],
#                                     onPage=headerFooterLayout)

# emptyTemplate = PageTemplate(id='emptyTemplate',
#                              frames=[myFrame],
#                              onPage=emptyLayout)

# elements = []
# elements.append(Paragraph('blah', style)
# elements.append(NextPageTemplate('emptyTemplate'))
# elements.append(PageBreak())
# elements.append(Paragraph('last page', style)

# doc = BaseDocTemplate(buffer,
#                       rightMargin=72,
#                       leftMargin=72,
#                       topMargin=72,
#                       bottomMargin=72)

# doc.addPageTemplates([headerFooterTemplate, emptyTemplate])

# doc.build(elements)





#from django.http import HttpResponse
#from reportlab.pdfgen import canvas

#def invoice_to_response(request, invoice):
#    response = HttpResponse(mimetype='application/pdf')
#    p = canvas.Canvas(response, pagesize=A4, pageCompression = 0)
#    # here I draw on 'p' like p.setFillColor(black)
#    p.showPage()
#    p.save()
#    return response
