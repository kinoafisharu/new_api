from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
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



    # Пагинированный список, поля указываются в классе
    def list(self, request):
        queryset = self.filter_queryset(self.queryset)
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many = True, fields = self.list_fields)
        return self.get_paginated_response(serializer.data)


    # Пример запроса somepath/getval/?values=id&ordering=id
    # Метод GET ниже сортирует обьекты в АПИ по любому полю из возможных (кроме вложенных)
    # Принимает параметры values (значения полей которые нужно вывести, строка с разделением запятой, без пробелов)
    # и ordering (как сортировать, принимает стандартные значения функции order_by django) """
    @action(detail = False, name = 'Get Sorted Values')
    def getval(self, request):
        values = request.query_params.get('values', None)
        if not values:
            return Response({'errors': 'Values must not be null'})
        else:
            data = values.split(',')
            try:
                queryset = self.filter_queryset(self.queryset)
            except FieldError as e:
                return Response({'errors': str(e)})
            page = self.paginate_queryset(queryset)
            serializer = self.serializer_class(page, many = True, fields = (data))
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
