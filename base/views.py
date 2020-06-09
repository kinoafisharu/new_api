from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from django.core.exceptions import FieldError

"""
 В этом файле содержатся родительские классы viewsets с расширенным спектром возможностей
"""



class MethodModelViewSet(viewsets.ModelViewSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Пагинированный список, поля указываются в классе
    def list(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many = True, fields = self.list_fields)
        return self.get_paginated_response(serializer.data)

# ример запроса somepath/getval/?values=id&ordering=id
# Метод GET ниже сортирует обьекты в АПИ по любому полю из возможных (кроме вложенных)
# Принимает параметры values (значения полей которые нужно вывести, строка с разделением запятой, без пробелов)
# и ordering (как сортировать, принимает стандартные значения функции order_by django) """
    @action(detail = False, name = 'Get Sorted Values')
    def getval(self, request):
        sort = request.query_params.get('ordering', None)
        val = request.query_params.get('values', None)
        if not val:
            return Response({'errors': 'Values must not be null'})
        else:
            data = val.split(',')
            try:
                if sort:
                    queryset = self.queryset.order_by(str(sort))
                else:
                    queryset = self.queryset
                page = self.paginate_queryset(queryset)
            except FieldError as e:
                return Response({'errors': str(e)})
            serializer = self.serializer_class(page, many = True, fields = (data))
        return self.get_paginated_response(serializer.data)
