
from rest_framework import serializers
from . import models
from .serializers_dic import *
from .mixins import *
from .serializers_helper import *
from . import serializer_fields


# -/ Александр Караваев =>
'''
Здесь определяются классы сериализаторов для конкретных моделей
Необходим для преобразования данных из бд, привязанной к ОРМ джанго в нативные типы данных
и дальнейшего их рендера в апи в формате джейсон
'''


class NewsSerializer(DynamicFieldsModelSerializer):
    tags = NewsTagsSerializer(many = True, fields = ('name',))
    class Meta:
        model = models.News
        fields = '__all__'


# Сериализатор класса Films со всеми указанными в классе полями
'''
Используется в детальном отображении фильма в апи, описан в файлах: views.py
Поддерживает динамическое изменение полей при передаче аргумента fields (кортеж с полями)
'''
class FilmsSerializer(DynamicFieldsModelSerializer):

    votes = serializer_fields.LikeField()
    sources = FilmsSourcesSerializer(many = True)
    persons = serializer_fields.PersonField(objectattributes = ['allnames', 'role'])
    name = FilmNameSerializer(many = True, fields = ('name',))
    release = FilmReleaseSerializer(many = True, fields = ('release', 'note'))
    country = CountrySerializer(many = True, fields = ('name',))
    genre = FilmGenreSerializer(many = True, fields = ('name',))
    production = ProductionSerializer(many = True)
    distributor = DistributorSerializer(many = True)
    images = ImageSerializer(many = True, fields = ('file',))
    budget = FilmBudgetSerializer(many = False, fields = ('budget',))
    class Meta:
        model = models.Films
        fields = '__all__'
# -/ Александр Караваев





# =================================================================================================

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
