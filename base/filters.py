from rest_framework import filters
from django.db.models import F, OuterRef, Subquery
from django.utils.timezone import timedelta
import datetime
from django_filters import rest_framework as django_filters


# Фильтрует обьекты ителлектуальной собственности,
# не соответствующие набору обязательных полей
# В классе нужно указать лист полей necessary_fields
class NecessaryFieldsAssurance(filters.BaseFilterBackend):
    def get_fields(self, view, request):
        getattr(view, 'necessary_fields', None)
    def filter_queryset(self, request, queryset, view):
        fields = self.get_fields(view, request)
        return queryset.filter(owner=request.user)

class DateTimeFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        date = request.query_params.get('datetime', None)
        if date:
            date = date.split(',')
            if date[0] == 'laterbackfromnow':
                date = datetime.datetime.now() - datetime.timedelta(int(date[1]))
                return queryset.filter(release__release__gt = date)
        return queryset




# Класс сортировщика с возможностью фильтрования по query expression
# Сортирует значения по нескольким или одному параметрам в порядке убывания или возрастания
# Принимает стандартные значения сортировки order_by
class NotNullOrderingFilter(filters.OrderingFilter):
    def remove_invalid_fields(self, queryset, fields, view, request):
        valid_fields = [item[0] for item in self.get_valid_fields(queryset, view, {'request': request})]

        def term_valid(term):
            if term.startswith("-"):
                term = term[1:]
            if '__' in term:
                return True
            return term in valid_fields

        return [term for term in fields if term_valid(term)]
    def get_ordering(self, request, queryset, view):
        params = request.query_params.get(self.ordering_param)
        if params:
            fields = [param.strip() for param in params.split(',')]
            ordering = self.remove_invalid_fields(queryset, fields, view, request)
            if ordering:
                return ordering
        return self.get_default_ordering(view)

    #создает F запрос ля каждого поля
    def get_f_expression(self, ordering):
        for field in ordering:
            if field.startswith('-'):
                yield F(field.strip('-')).desc(nulls_last = True)
            else:
                yield F(field).asc(nulls_last = True)


    def order_queryset(self, queryset, queries):
        return queryset.order_by(*queries)

    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)
        if ordering:
            queries = self.get_f_expression(ordering)
            queryset = self.order_queryset(queryset, queries)
        return queryset
