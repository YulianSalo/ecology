# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from eco.models import *
from django.contrib.auth.decorators import login_required

#@login_required(login_url="/accounts/login/")
def ecoMeasuredList(request):
	ecoMeasures = ecoParameterMeasured.objects.all().order_by('date')
	context = {
	'ecoMeasures': ecoMeasures
	}
	return render(request, 'eco/home.html', context)

def ecoMeasuredDetail(request, pk):
# return HttpResponse(slug)
	ecoMeasure = ecoParameterMeasured.objects.get(pk=pk)
	context = {
	'ecoMeasure': ecoMeasure
	}
	return render(request, 'eco/ecoMeasurementDetail.html',context)

@login_required(login_url="/accounts/login/")
def ecoMeasuredNew(request):
	return render(request, 'eco/home.html')