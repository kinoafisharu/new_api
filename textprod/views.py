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
class StoriesViewSet(viewsets.ModelViewSet):
    queryset = models.News.objects.filter(subdomain = 'memoirs')
    serializer_class = serializers.StoriesSerializer
    pagination_class = FivePagination
    filter_backends = [filters.OrderingFilter]


    # Метод листинга с пагинацией, ограничение по полям
    def list(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = serializers.StoriesSerializer(page, many = True, fields = ('id','title','text', 'dtime','author', 'views',))
        return self.get_paginated_response(serializer.data)
    # Метод сортировки историй по любому полю GET запросом и ограничение по выводу от 1 до 50
    # Параметр ?amount ограничивает выводимое количествo историй
    # Параметр ?by определяет тип сортировки
    # (принимает стандартные аргументы функции order_by django, пример -dtime (убывание по дате))
    @action(detail = False)
    def getval(self, request):
        r = request.query_params.get('values', None)
        sort = request.query_params.get('ordering', None)
        data = r.split(',')
        queryset = models.News.objects.all().order_by(str(sort))
        page = self.paginate_queryset(queryset)
        serializer = serializers.StoriesSerializer(page, many = True, fields = (data))
        return self.get_paginated_response(serializer.data)

    # Метод принимает значение в виде названий полей модели, отдает результат в апи с обозначеными полями
    @action(detail = False)
    def getval(self, request):
        r = request.query_params.get('values', None)
        order = request.query_params.get('ordering', None)
        data = r.split(',')
        queryset = models.News.objects.all().filter(subdomain = 'memoirs').order_by(str(order))
        page = self.paginate_queryset(queryset)
        serializer = serializers.StoriesSerializer(page, many = True, fields = (data))
        return self.get_paginated_response(serializer.data)
# -/ Александр Караваев
