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
from rest_framework import status
from . import serializers
from base import models
import logging


class FilmReleaseViewSet(baseviews.MethodModelViewSet):
    queryset = models.FilmsReleaseDate.objects.all()
    serializer_class = serializers_helper.FilmReleaseSerializer
    pagination_class = FivePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, NotNullOrderingFilter]
    filterset_fields = ['id', 'release']
    search_fields = ['id', 'release']
    default_list_fields = ('id','release')
    def create(self, request):
        data = request.data
        kid = request.data.get('kid', None)
        id = request.data.get('id', None)
        if not data:
            return Response({'errors': 'No data provided'})
        serializer = serializers_helper.FilmReleaseSerializer(data = {'release': data['release']})
        if serializer.is_valid():
            obj = serializer.save()
            if id:
                film = models.Films.objects.get(id = id)
                film.release.add(obj)
            elif kid:
                film = models.Films.objects.get(kid = kid)
                film.release.add(obj)
            res_dict = serializer.validated_data.copy()
            res_dict.update({'film': film.id})
            return Response(res_dict)
        return Response({'error': 'Invalid data'}, status = status.HTTP_400_BAD_REQUEST)
