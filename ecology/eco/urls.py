from django.conf.urls import url
from eco import views

app_name = 'eco'

urlpatterns = [
    url(r'^$', views.ecoMeasuredList, name="list"),
    url(r'^create/$', views.ecoMeasuredNew, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.ecoMeasuredDetail, name="detail"),
]