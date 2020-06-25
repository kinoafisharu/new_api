from rest_framework import serializers
from django.core import exceptions
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
    sourcefilms_set = SourceFilmsSerializer(many = True, repfields = ('name','top250_set'))
    persons = serializer_fields.PersonField(objectattributes = ['name_main'])
    name = FilmNameSerializer(many = True, repfields = ('name',))
    release = FilmReleaseSerializer(many = True, repfields = ('release', 'note'))
    country = CountrySerializer(many = True, repfields = ('name',))
    genre = FilmGenreSerializer(many = True, repfields = ('name',))
    production = ProductionSerializer(many = True)
    distributor = DistributorSerializer(many = True)
    images = ImageSerializer(many = True, repfields = ('file',))
    budget = FilmBudgetSerializer(many = False, repfields = ('budget',))

    # Метод создает обьект если его не существует
    def create(self, validated_data):
        names = validated_data.pop('name', None)
        film = models.Films.objects.create(**validated_data)
        if names:
            for name in names:
                obj = self.get_first_or_create(model = models.NameFilms, data = name)
                print(obj)
                if obj:
                    film.name.add(obj)
                    print(f'One object {obj} added to {film}')
        return film

    # Метод обновляет обьект если он существут
    def update(self, instance, validated_data):
        names = validated_data.pop('name', None)
        instance.imdb_rate = validated_data.get('imdb_rate', instance.imdb_rate)
        instance.imdb_votes = validated_data.get('imdb_votes', instance.imdb_votes)
        instance.imdb_id = validated_data.get('imdb_id', instance.imdb_id)
        instance.save()
        if names:
            for name in names:
                obj = self.get_first_or_create(model = models.NameFilms, data = name)
                print(obj)
                if obj:
                    instance.name.add(obj)
                    print(f'One object {obj} added to {instance}')
        return instance

    class Meta:
        model = models.Films
        fields = '__all__'


# -/ Александр Караваев
