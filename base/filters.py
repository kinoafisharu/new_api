from rest_framework import filters

class OrderingFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        by = request.query_params.get('ordering', None)
        filtered = queryset.order_by(by)
        return filtered
