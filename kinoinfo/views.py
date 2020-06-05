from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from base import serializers_helper
from . import serializers
from base import models
import logging


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

# Метод добавляет один лайк к фильму с ид взятым из <int:pk>  по запросу POST https:/|host|/films/<int:pk>/like
    @action(detail = True, methods = ['post'], url_path = 'like', url_name = 'like')
    def like(self, request, pk = None):
        # Внимание!! Крайне важен порядок в словаре передаваемых данных в сериализатор
        # Построение отношения между обьектами происходит автоматически, при десериализации достаточно передать значение pk (ID)
        serializer = serializers_helper.LikeSerializer(data = {'evaluation': request.data['evaluation'], 'filmobject': pk} , fields = ('evaluation', 'filmobject'))
        if serializer.is_valid():
            like = serializer.save()
            return Response({'liked':True}, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
# -/ Александр Караваев
