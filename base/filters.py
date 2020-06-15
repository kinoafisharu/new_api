from rest_framework import filters
from django.db.models import F


# Фильтрует обьекты ителлектуальной собственности,
# не соответствующие набору обязательных полей
# В классе нужно указать лист полей necessary_fields
class NecessaryFieldsAssurance(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        fields = self.necessary_fields
        queryset.filter()
        return queryset.filter(owner=request.user)

# Класс сортировщика с возможностью фильтрования по query expression
# Сортирует значения по нескольким или одному параметрам в порядке убывания или возрастания
# Принимает стандартные значения сортировки order_by
class NotNullOrderingFilter(filters.OrderingFilter):
    def get_ordering(self, request, queryset, view):
        params = request.query_params.get(self.ordering_param)
        if params:
            fields = [param.strip() for param in params.split(',')]

            ordering = self.remove_invalid_fields(queryset, fields, view, request)
            if ordering:
                return ordering
        return self.get_default_ordering(view)

    # Создает F запрос для каждого поля
    def order_by_exp(self, ordering, queryset):
        queries = []
        for field in ordering:
            if field.startswith('-'):
                queries.append(F(field.strip('-')).desc(nulls_last = True))
            else:
                queries.append(F(field).asc(nulls_last = True))
        queryset = queryset.order_by(*queries)
        return queryset

    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)
        if ordering:
            queryset = self.order_by_exp(ordering, queryset)
        return queryset
