from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views


urlpatterns = [
    #re_path(r'^$', login_required(eco_views.home.as_view()), name='home'),
    #re_path(r'^login/$', eco_views.login, name='login'),
    re_path(r'^login/$', auth_views.LoginView, {'template_name': 'login.html'}, name='login'),
    re_path(r'^logout/$', auth_views.LogoutView, {'next_page': 'login'}, name='logout'),
    re_path(r'^signup/$', accounts_views.signup, name='signup'),
]