from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from django.core.exceptions import FieldError
from django.db.models import F

"""
 В этом файле содержатся родительские классы viewsets с расширенным спектром возможностей
"""


# Родительский класс хранящий методы характерные для интеллектуальных продуктов
class MethodModelViewSet(viewsets.ModelViewSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    #Принудительная фильтрация для всех методов
    def filter_queryset(self, queryset):
        filter_backends = self.filter_backends
        for backend in list(filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, view=self)
        return queryset


    def get_list_field_values(self, request):
        flds = request.query_params.get('values', None)
        if flds:
            return flds.strip().strip(' ').split(',')

    # Пагинированный список, поля указываются в классе
    def list(self, request):
        flds = self.get_list_field_values(request)
        self.list_fields = flds if flds else self.default_list_fields
        queryset = self.filter_queryset(self.queryset)
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many = True, fields = self.list_fields)
        return self.get_paginated_response(serializer.data)


    #Возвращает топ фильмов по идентификационному полю рейтинга указываемого в конкретном представлении
    @action(detail = False)
    def top250(self, request):
        i = self.top_identifier
        istr = i.strip('-')
        queryset = eval('self.queryset.filter({0}__isnull = False).order_by("{1}")'.format(istr,i))
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many = True)
        return self.get_paginated_response(serializer.data)
