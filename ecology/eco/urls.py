from django.conf.urls import url
from eco import views
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

app_name = 'eco'

urlpatterns = [
    url(r'^$', views.ecoMeasuredList, name="list"),
    url(r'^create/$', views.ecoMeasuredNew, name="create"),
    url(r'^(?P<pk>[\w-]+)/$', views.ecoMeasuredDetail, name="detail"),
]