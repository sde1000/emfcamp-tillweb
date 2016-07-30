"""tillweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

import quicktill.tillweb.urls
import emftill.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^detail/', include(quicktill.tillweb.urls.tillurls),
        {"pubname": "detail"}),
    url(r'^$', emftill.views.frontpage, name="home"),
    url(r'^locations.json$', emftill.views.locations),
    url(r'^location/(?P<location>[\w\- ]+).json$', emftill.views.location),
    url(r'^stock.json$', emftill.views.stock),
]
