from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from conetnt_api.models import Item
from conetnt_api.serializers import ItemSerializer



# Create your views here.

class ItemSet(viewsets.ModelViewSet):
	queryset=Item.objects.all()
	serializer_class=ItemSerializer

