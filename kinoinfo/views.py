import datetime
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from base.pagination import FivePagination
from django_filters.rest_framework import DjangoFilterBackend
from base.filters import NotNullOrderingFilter, DateTimeFilter
from parsing import parsers
from rest_framework.decorators import action
from rest_framework import filters
from base import serializers_helper
from base import models
from base import views as baseviews
from . import serializers
from base import models
import logging


# Классы отображения сериализорваных данных совмещают в себе list, retrieve, update, delete
# Можно задавать дополнительные действия по запросам с помощью декоратора @action()


# Для отобраения краткой информации о фильме в листе и подробной в детальном (films/)=> short (films/{int:pk})=> long
class FilmsViewSet(baseviews.MethodModelViewSet):
    queryset = models.Films.objects.all().order_by('id')
    serializer_class = serializers.FilmsSerializer
    pagination_class = FivePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, NotNullOrderingFilter, DateTimeFilter]
    filterset_fields = ['id', 'imdb_id', 'year']
    search_fields = ['id']
    top_identifier = '-imdb_rate'
    default_list_fields = ('id','kid','imdb_id','year','poster')


# Метод добавляет один лайк к фильму с ид взятым из <int:pk>  по запросу POST https:/|host|/films/<int:pk>/like
    @action(detail = True, methods = ['post'], url_path = 'like', url_name = 'like')
    def like(self, request, pk = None):
        # Внимание!! Крайне важен порядок в словаре передаваемых данных в сериализатор
        # Построение отношения между обьектами происходит автоматически, при сериализации достаточно передать значение pk (ID)
        serializer = serializers_helper.LikeSerializer(data = {'evaluation': request.data['evaluation'], 'filmobject': pk} , fields = ('evaluation', 'filmobject'))
        if serializer.is_valid():
            like = serializer.save()
            return Response({'liked':True}, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
# -/ Александр Караваев
