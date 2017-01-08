from django.shortcuts import render
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from app.models import Patient
from .models import Certificat, Courrier, Stomato, Arret
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts  import render_to_response, redirect
from django.shortcuts import get_object_or_404
from django.template import Context
from django.template.loader import get_template #render_to_string
from reportlab.platypus import PageTemplate, BaseDocTemplate, NextPageTemplate, PageBreak
from subprocess import Popen, PIPE
import tempfile
import os
from django.core.files.storage import FileSystemStorage
from io import StringIO
import operator
from django.db.models import Q
from six.moves import reduce
# Create your views here.
import jinja2
#from jinja2 import Template
import weasyprint


# latex_jinja_env = jinja2.Environment(
	# block_start_string = '\BLOCK{',
	# block_end_string = '}',
	# variable_start_string = '\VAR{',
	# variable_end_string = '}',
	# comment_start_string = '\#{',
	# comment_end_string = '}',
	# line_statement_prefix = '%%',
	# line_comment_prefix = '%#',
	# trim_blocks = True,
	# autoescape = False,
	# loader = jinja2.FileSystemLoader(os.path.abspath('.'))
# )


def certificat_pdf(request, pk2, pk1):
    entry = Certificat.objects.get(pk=pk2)
    source = Patient.objects.get(pk=pk1)
    context = Context({ 'certificat': entry, 'patient': source })
    #buffer = BytesIO()
    template = get_template('courrier/certificat.tex')
    rendered_tpl = template.render(context, request).encode('utf-8')
    #Python3 only. For python2 check out the docs!
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


def courrier_pdf(request, pk2, pk1):
    entry = Courrier.objects.get(pk=pk2)
    source = Patient.objects.get(pk=pk1)
    context = Context({ 'courrier': entry, 'patient': source })
    #buffer = BytesIO()
    template = get_template('courrier/courrier.tex')
    rendered_tpl = template.render(context, request).encode('utf-8')
    #Python3 only. For python2 check out the docs!
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


# def courrier_easy(request, pk1, pk2):
#     entry = Courrier.objects.get(pk=pk2)
#     source = Patient.objects.get(pk=pk1)
#     context = Context({ 'courrier': entry, 'patient': source })
#     template = get_template("courrier.html")
#     html = template.render(RequestContext(request, context))
#     response = HttpResponse(mimetype="application/pdf")
#     weasyprint.HTML(string=html, url_fetcher=url_fetcher).write_pdf(response)
#     return response
# def courrier_easy(request, pk1, pk2):
    # entry = Courrier.objects.get(pk=pk2)
    # source = Patient.objects.get(pk=pk1)
    # context = Context({ 'courrier': entry, 'patient': source })
    # template = get_template("courrier.html")
    # html_string = render_to_string('core/pdf_template.html', {'paragraphs': paragraphs})

    # html = weasyprintHTML(string=html_string)
    # html.write_pdf(target='/tmp/mypdf.pdf');

    # fs = FileSystemStorage('/tmp')
    # with fs.open('mypdf.pdf') as pdf:
        # response = HttpResponse(pdf, content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        # return response

    # return response

def courrier_easy(request, pk1, pk2):
    html_template = get_template('courrier.html')
    entry = Courrier.objects.get(pk=pk2)
    source = Patient.objects.get(pk=pk1)
    context = Context({ 'courrier': entry, 'patient': source })
    rendered_html = html_template.render(RequestContext(request, context)).encode(encoding="UTF-8")

    pdf_file = weasyprint.HTML(string=rendered_html).write_pdf(stylesheets=[CSS(settings.STATIC_ROOT +  'css/report.css')])

    http_response = HttpResponse(pdf_file, content_type='application/pdf')
    http_response['Content-Disposition'] = 'filename="report.pdf"'

    return response


def arret_pdf(request, pk2, pk1):
    entry = Arret.objects.get(pk=pk2)
    source = Patient.objects.get(pk=pk1)
    context = Context({ 'arret': entry, 'patient': source })
    #buffer = BytesIO()
    template = get_template('arret.tex')
    rendered_tpl = template.render(context, request).encode('utf-8')
    #Python3 only. For python2 check out the docs!
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


def ordonnance_pdf(request, pk2, pk1):
    entry = Ordonnance.objects.get(pk=pk2)
    source = Patient.objects.get(pk=pk1)
    context = Context({ 'ordonnance': entry, 'patient': source })
    #buffer = BytesIO()
    template = get_template('ordonnance.tex')
    rendered_tpl = template.render(context, request).encode('utf-8')
    #Python3 only. For python2 check out the docs!
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


def stomato_pdf(request, pk2, pk1):
    entry = Stomato.objects.get(pk=pk2)
    source = Patient.objects.get(pk=pk1)
    context = Context({ 'stomato': entry, 'patient': source })
    #buffer = BytesIO()
    template = get_template('courrier/certificat.tex')
    rendered_tpl = template.render(context, request).encode('utf-8')
    #Python3 only. For python2 check out the docs!
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

