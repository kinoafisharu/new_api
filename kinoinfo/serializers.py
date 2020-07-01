from rest_framework import serializers
from django.core import exceptions
from base import models
from base.serializers_dic import *
from base.mixins import *
from base import serializers as base_serializers
from base.serializers_helper import *
from base import serializer_fields
from parsing import parsers
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
    poster = serializers.SerializerMethodField()

    def handle_names(self, data, film, **kwargs):
        name = kwargs.pop('name', None)
        names = data.pop('name', None) if not name else name
        if names:
            for name in names:
                obj = self.get_first_or_create(model = models.NameFilms, data = name)
                print(obj)
                if obj:
                    film.name.add(obj)
                    print(f'One object {obj} added to {film}')

    def handle_release(self, data, film, **kwargs):
        release = kwargs.pop('release', None)
        release = data.pop('release', None) if not release else release
        if release:
            serializer = FilmReleaseSerializer(data = release[0])
            if serializer.is_valid():
                relobj = serializer.save()
                try:
                    film = models.Films.objects.distinct('kid').get(kid = kid)
                    if film.release.exists():
                        for rel in film.release.all():
                            rel.delete()
                    film.release.add(relobj)
                except Exception as e:
                    str(e)

    # Метод создает обьект если его не существует
    def create(self, validated_data):
        name = validated_data.pop('name', None)
        release = validated_data.pop('release', None)
        film = self.get_first_or_create(model = models.Films, data = validated_data)
        self.handle_names(validated_data, film, name = name)
        self.handle_release(validated_data, film, release = release)

        return film

    # Метод обновляет обьект если он существут
    def update(self, instance, validated_data):
        self.handle_names(validated_data, instance)
        self.handle_release(validated_data, instance)
        instance.imdb_rate = validated_data.get('imdb_rate', instance.imdb_rate)
        instance.imdb_votes = validated_data.get('imdb_votes', instance.imdb_votes)
        instance.imdb_id = validated_data.get('imdb_id', instance.imdb_id)
        instance.save()
        return instance

    def get_poster(self, obj):
        kid = obj.kid
        if kid:
            url = 'http://kinoinfo.ru/film/{0}/'.format(kid)
            parser = parsers.KinoinfoParser(url = url, parser = 'lxml', fields = ['poster'])
            data = parser.parse()
            return data['poster']

    class Meta:
        model = models.Films
        fields = '__all__'


# -/ Александр Караваев
