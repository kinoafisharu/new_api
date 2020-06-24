from rest_framework import serializers
from . import models
from . import serializers_dic
from . import serializer_fields
from .mixins import *

"""
!!! WARNING!!!

В данном файле описываются все классы сериализаторов, напрямую не участвующие в рендеринге,
т.е., вложенные сериализаторы, служащие для отбражения собственной информации в других сериализаторах

Все поля сериализаторов имеют динамическое отображение,
 что бы им воспользоваться нужно в аргументах при создании
 поля указать кортеж fields с нужным набором полей
"""




class NewsTagsSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.NewsTags
        fields = '__all__'

"""
 Сериализация лайков, ниже валидация того что значение лайка число в промежутке от 1 до 5
 и валидация существования фильма
 Отображaet количествo лайков во вложенной реперезентации вместо всех лайков в виде списка их обьектов
"""
class LikeSerializer(DynamicFieldsModelSerializer):
    def to_representation(self, instance):
        likes = instance.filter(evaluation__in = [1,2,3])
        dislikes = instance.filter(evaluation__in = [4,5])
        return {'likes': likes.count(),'dislikes': dislikes.count()}
    class Meta:
        model = models.Likes
        fields = '__all__'

    def validate_evaluation(self, value):
        if value and not 1 <= value <= 5:
            raise serializers.ValidationError('Your evaluation must be bigger than 1 and less than 5')
        elif not isinstance(value, int):
            raise serializers.ValidationError('Evaluation must be an integer')
        return value
    def validate_filmobject(self, value):
        if not value:
            raise serializers.ValidationError("There's no film you're trying to like")
        return value


''' СЕРИАЛИЗАЦИЯ ИЗОБРАЖЕНИЙ, ЕСТЬ ПРИВЯЗКИ К Person И Films '''
class ImageSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.Images
        fields = '__all__'


''' СЕРИАЛИЗАТОР ИМЕНИ ФИЛЬМА, ПРИВЯЗКА К Films '''
class FilmNameSerializer(DynamicFieldsModelSerializer):
    def create(self, validated_data):
        return models.NameFilms.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.status = validated_data.get('status', instance.name)
        instance.save()
        return instance
    class Meta:
        model = models.NameFilms
        fields = '__all__'

''' СЕРИАЛИЗАТОР ИМЕН ПЕРСОН, ПРИВЯЗКА К Person '''
class NamePersonSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.NamePerson
        fields = '__all__'


"""СЕРИАЛИЗАТОР ЖАНРА ФИЛЬМА"""
class FilmGenreSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = models.Genre
        fields = '__all__'

''' СЕРИАЛИЗАТОР ПРОИЗВОДИТЕЛЯ ФИЛЬМА, ПРИВЯЗКА К Films '''
class ProductionSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.ProductionsCo
        fields = '__all__'

''' СЕРИАЛИЗАТОР ИМЕНИ ДИСТРИБЬЮТОРА '''
class NameDistributorSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = models.NameDistributors
        fields = '__all__'

''' СЕРИАЛИЗАТОР ДИСТРИБЬЮТОРА '''
class DistributorSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.Distributors
        fields = '__all__'

''' СЕРИАЛИЗАТОР БЮДЖЕТА ФИЛЬМА (ЗАМЕНИТЬ ВЫДЕЛЕННЫМ ПОЛЕМ) '''
class FilmBudgetSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.Budget
        fields = '__all__'

''' СЕРИАЛИЗАТОР ИСТОЧНИКОВ '''
class SourcesSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.ImportSources
        fields = '__all__'

class Top250Serializer(DynamicFieldsModelSerializer):

    class Meta:
        model = models.Top250
        fields  = '__all__'



class SourceFilmsSerializer(DynamicFieldsModelSerializer):
    def to_representation(self, instance):
        try:
            rev = instance.top250_set.reverse()[0]
        except:
            rev = None
        if rev:
            ser = Top250Serializer(rev)
            data = ser.data
            ser.is_valid()
            print(data)
            return({'':data})
        else:
            return {}
    class Meta:
        model = models.SourceFilms
        fields = '__all__'

'''СЕРИАЛИЗАТОР ОТНОШЕНИЯ РЕЛИЗОВ К ФИЛЬМАМ'''
class FilmReleaseSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.FilmsReleaseDate
        fields = '__all__'
