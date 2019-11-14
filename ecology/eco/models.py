from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class userProfile(models.Model):
	userClass = models.CharField(max_length=30, default='not_null')
	userLogin = models.CharField(max_length=30, primary_key=True, default='not_null')
	userEmail = models.EmailField(max_length=254, default='not_null')
	userPassword = models.CharField(max_length=30, default='not_null')

    
