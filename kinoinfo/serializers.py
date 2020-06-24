from rest_framework import serializers
from base import models
from base.serializers_dic import *
from base.mixins import *
from base import serializers as base_serializers
from base.serializers_helper import *
from base import serializer_fields
from . import serializer_fields as local_fields


# -/ Александр Караваев =>
'''
Здесь определяются классы сериализаторов для конкретных моделей
Необходим для преобразования данных из бд, привязанной к ОРМ джанго в нативные типы данных
и дальнейшего их рендера в апи в формате JSON
'''
#
# Сериализатор класса Films со всеми указанными в классе полями
'''
Используется в детальном отображении фильма в апи, описан в файлах: views.py
Поддерживает динамическое изменение полей при передаче аргумента fields (кортеж с полями)
'''
class FilmsSerializer(DynamicFieldsModelSerializer):
    votes = LikeSerializer()
    sourcefilms_set = SourceFilmsSerializer(many = True, fields = ('name','top250_set'))
    persons = serializer_fields.PersonField(objectattributes = ['name_main'])
    name = FilmNameSerializer(many = True, fields = ('name',))
    release = FilmReleaseSerializer(many = True, fields = ('release', 'note'))
    country = CountrySerializer(many = True, fields = ('name',))
    genre = FilmGenreSerializer(many = True, fields = ('name',))
    production = ProductionSerializer(many = True)
    distributor = DistributorSerializer(many = True)
    images = ImageSerializer(many = True, fields = ('file',))
    budget = FilmBudgetSerializer(many = False, fields = ('budget',))

    def create(self, validated_data):
        return models.Films.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imdb_rate = validated_data.get('imdb_rate', instance.imdb_rate)
        instance.imdb_votes = validated_data.get('imdb_votes', instance.imdb_votes)
        instance.save()
        return instance

    class Meta:
        model = models.Films
        fields = '__all__'


# -/ Александр Караваев
