# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from eco.models import *
from django.contrib.auth.decorators import login_required

def ecoMeasuredList(request):
    articles = Article.objects.all().order_by('date');
    return render(request, 'eco/article_list.html', { 'articles': articles })

def ecoMeasuredDetail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'eco/article_detail.html', { 'article': article })

@login_required(login_url="/accounts/login/")
def ecoMeasuredNew(request):
    return render(request, 'eco/home.html')