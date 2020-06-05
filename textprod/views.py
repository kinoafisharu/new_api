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


logger = logging.getLogger(__name__)

class StoriesViewSet(viewsets.ModelViewSet):
    queryset = models.News.objects.filter(subdomain = 'memoirs')
    serializer_class = serializers.StoriesSerializer
    pagination_class = PageNumberPagination

    def list(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = serializers.StoriesSerializer(page, many = True, fields = ('title','text', 'dtime','visible', 'img', 'videos', 'views',))
        return self.get_paginated_response(serializer.data)

    @action(detail = False)
    def orderby(self, request):
        trunc = lambda n, max_n, min_n: max(min(max_n, n), min_n)
        amount = trunc(int(request.query_params['amount']), 50, 1)
        queryset = self.get_queryset().order_by(request.query_params['by'])[:amount]
        serializer = self.get_serializer(queryset, many = True)
        return Response(serializer.data)
