from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
	return HttpResponse('<marquee><h1>Hello world !</h1><marquee>')

def show(request):
	'''post=Stud.objects.all()
	return 'data=%s'%post
	#return HttpResponse('<marquee><h1>Hello world !</h1><marquee>') '''
	return HttpResponse('<b>NITION AROTE...</b>')

	