from django.shortcuts import render
from django.http import HttpResponse
from .models import newsPost
# Create your views here.

def index(request):
    newsposts = newsPost.objects.all()
    return render(request,'index.html',{'news' : newsposts})