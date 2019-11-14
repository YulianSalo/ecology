from django.urls import path
from eco import views

urlpatterns = [
	path("", views.signup, name="signup"),
	]