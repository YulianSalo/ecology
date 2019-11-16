from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class userProfile(models.Model):
	userClass = models.CharField(max_length=30, verbose_name="User class")
	userLogin = models.CharField(max_length=30, primary_key=True, verbose_name="Login")
	userEmail = models.EmailField(max_length=254, verbose_name="E-mail")
	userPassword = models.CharField(max_length=30, verbose_name="Password")


class ecoParameterStandard(models.Model):
	ecoParamID = models.AutoField(primary_key=True)
	ecoParamName = models.CharField(max_length=127)
	ecoParamValue = models.CharField(max_length=127)


#class ecoParameterMeasured(models):
	#pass
	
	


    
