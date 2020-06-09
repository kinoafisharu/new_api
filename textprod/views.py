from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination, CursorPagination
from rest_framework import filters
from base.pagination import FivePagination
from rest_framework.decorators import action
from base import serializers_helper
from base import views as baseviews
from base import filters as basefilters
from . import serializers
from base import models
import logging

# Классы отображения сериализорваных данных совмещают в себе list, retrieve, update, delete
# Можно задавать дополнительные действия по запросам с помощью декоратора @action()

logger = logging.getLogger(__name__)

'''
Представление, отображающее листинг историй
'''
class StoriesViewSet(baseviews.MethodModelViewSet):
    queryset = models.News.objects.filter(subdomain = 'memoirs')
    serializer_class = serializers.StoriesSerializer
    pagination_class = FivePagination
    filter_backends = [filters.OrderingFilter]
    list_fields = ('id','title','text', 'dtime','author', 'views',)

# -/ Александр Караваев
