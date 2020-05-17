from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models
# Create your views here.

class BaseFilmsViewSet(viewsets.ModelViewSet):
    queryset = models.BaseFilms.objects.all()
    serializer_class = serializers.BaseFilmsSerializer
