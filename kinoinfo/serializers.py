
from rest_framework import serializers
from . import models
from .serializers_dic import *
from .mixins import *
from collections import OrderedDict
from .serializers_helper import *
from . import serializer_fields


class PersonSerializer(DynamicFieldsModelSerializer):
    name = NamePersonSerializer(many = True, fields = ('name',))
    country = CountrySerializer(many = False, fields = ('name',))
    class Meta:
        model = models.Person
        fields = '__all__'


class ProfileSerializer(DynamicFieldsModelSerializer):
    person = PersonSerializer(many = False, fields = ('name',))
    class Meta:
        model = models.Profile
        fields = '__all__'

# =================================================================================================

# Александр Караваев ==>
# Вспомогательный класс сериализации для парсинга данных с asteroid (Когда данные будут перенесены, весь код под чертой выше к удалению!)
class AsteroidFilmSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    original_title = serializers.CharField()
    country = serializers.IntegerField()
    year = serializers.CharField()
    company = serializers.IntegerField()
    genre1 = serializers.IntegerField()
    genre2 = serializers.IntegerField()
    genre3 = serializers.IntegerField()
    site = serializers.CharField()
    director1 = serializers.IntegerField()
    director2 = serializers.IntegerField()
    director3 = serializers.IntegerField()
    imdb = serializers.CharField()
    imdb_votes = serializers.IntegerField()
    actor1 = serializers.IntegerField()
    actor2 = serializers.IntegerField()
    actor3 = serializers.IntegerField()
    actor4 = serializers.IntegerField()
    actor5 = serializers.IntegerField()
    actor6 = serializers.IntegerField()
    runtime = serializers.CharField()
    limits = serializers.CharField()
    prokat1 = serializers.IntegerField()
    prokat2 = serializers.IntegerField()
    date = serializers.DateTimeField()
    description = serializers.CharField()
    comment = serializers.CharField()
    country2 = serializers.IntegerField()
    trailers = serializers.CharField()
    idalldvd = serializers.IntegerField()
    datelastupd = serializers.DateTimeField()
