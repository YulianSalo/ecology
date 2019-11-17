# Create your models here.
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import sys
sys.path.insert(0, '../accounts')
from accounts import models as accounts_models

class ecoParameterStandard(models.Model):
	ecoParamID = models.AutoField(primary_key=True)
	ecoParamName = models.CharField(max_length=127)
	ecoParamValue = models.CharField(max_length=127)

	def __str__(self):
		return self.ecoParamID


class ecoParameterMeasured(models.Model):
	ecoParamMeasuredID = models.ForeignKey(ecoParameterStandard, on_delete=models.CASCADE)
	ecoParamMeasuredValue = models.CharField(max_length=127)
	ecoParamDate = models.DateField()
	ecoParamMeasuredBy = models.ForeignKey(accounts_models.userProfile, on_delete=models.CASCADE)

class ecoReport(models.Model):
	ecoReportID = models.AutoField(primary_key=True)
	ecoReportParamStd = models.ForeignKey(ecoParameterStandard, on_delete=models.CASCADE)
	ecoReportParamMsr = models.ForeignKey(ecoParameterMeasured, on_delete=models.CASCADE)
	ecoReportToReview = models.ForeignKey(accounts_models.userProfile, on_delete=models.CASCADE)
