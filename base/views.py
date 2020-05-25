from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from . import serializers
from . import models
# Create your views here.

# Классы отображения сериализорваных данных совмещают в себе list, retrieve, update, delete
# Можно задавать дополнительные действия по запросам с помощью декоратора @action()


# Для отобраения краткой информации о фильме в листе и подробной в детальном (films/)=> short (films/{int:pk})=> long
class FilmsViewSet(viewsets.ModelViewSet):
    queryset = models.Films.objects.all()
    serializer_class = serializers.ShortFilmsSerializer

# Переписанный метод ритрив для выдачи сериализатора со всеми полями из укороченного list вывода
    def retrieve(self, request, pk=None):
        queryset = models.Films.objects.all()
        film = get_object_or_404(queryset, pk=pk)
        serializer = serializers.FilmsSerializer(film)
        return Response(serializer.data)
# -/ Александр Караваев
