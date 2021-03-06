"""bacon_oil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'webapp.views.home'),
    url(r'^story/$', 'webapp.views.story'),
    url(r'^contact/$', 'webapp.views.contact'),
    url(r'^safety/$', 'webapp.views.safety'),
    url(r'^blog/$', 'webapp.views.blog'),
    url(r'^product/$', 'webapp.views.product'),
    url(r'^recipes/$', 'webapp.views.recipes'),
    url(r'^store/$', 'webapp.views.store'),
]

urlpatterns += staticfiles_urlpatterns()
