"""STEMKonnect URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
import accounts.views as views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^locations/', include('locations.urls', namespace='Locations', app_name='Locations')),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls', namespace="auth")), 
    url(r'^api/v1/', include('hotelsApi.v1.urls')),
    url(r'^accounts/login/$', views.LoginUser.as_view()),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
