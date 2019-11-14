from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
	userClass = models.CharField(max_length=30, default='not_null')
	userLogin = models.CharField(primary_key=True, default='not_null')
	userEmail = models.EmailField(max_length=254, default='not_null')
	userPassword = models.CharField(max_length=30, default='not_null')
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()