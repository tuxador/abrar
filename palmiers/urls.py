"""palmiers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from courrier import models, views
from app import models, views
from django.contrib.auth.views import login, logout
import courrier.urls
#import profiles.urls
#import accounts.urls
import app.urls

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login, {'template_name': 'admin/login.html'}),
    url(r'^logout/$',logout),
#    url(r'^users/', include(profiles.urls, namespace='profiles')),
#    url('^markdown/', include( 'django_markdown.urls')),
#    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^patients/', include(app.urls, namespace='clinique')),
    url(r'^courrier/', include(courrier.urls, namespace='courrier')),
]

#urlpatterns += patterns('django.contrib.auth',
#    (r'^accounts/login/$','views.login', {'template_name': 'admin/login.html'}),
#    (r'^accounts/logout/$','views.logout'),
#)
