from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from . import serializers
from . import models
# Create your views here.

# Классы отображения сериализорваных данных совмещают в себе list, retrieve, update, delete
# Можно задавать дополнительные действия по запросам с помощью декоратора @action()


# Для отобраения краткой информации о фильме в листе и подробной в детальном (films/)=> short (films/{int:pk})=> long
class FilmsViewSet(viewsets.ModelViewSet):
    queryset = models.Films.objects.all()
    serializer_class = serializers.FilmsSerializer
    pagination_class = PageNumberPagination


# Метод выдает пагинированный список фильмов, вывод укороченный
    def list(self, request):
        queryset = models.Films.objects.all()
        page = self.paginate_queryset(queryset)
        serializer = serializers.FilmsSerializer(page, many = True, fields = ('id','kid','imdb_id', 'year'))
        return self.get_paginated_response(serializer.data)
# -/ Александр Караваев
