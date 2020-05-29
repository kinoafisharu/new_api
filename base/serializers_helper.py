
from rest_framework import serializers
from . import models
from . import serializers_dic
from .serializers_dic import *
from . import serializer_fields

"""
!!! WARNING!!!

В данном файле описываются все классы сериализаторов, напрямую не участвующие в рендеринге,
т.е., вложенные сериализаторы, служащие для отбражения собственной информации в других сериализаторах

Все поля сериализаторов имеют динамическое отображение,
 что бы им воспользоваться нужно в аргументах при создании
 поля указать кортеж fields с нужным набором полей
"""


'''
Класс для создания подклассов с динамическим набором полей, описан в документации djangorestframework
'''
class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
#====================================================================================


''' СЕРИАЛИЗАЦИЯ ИЗОБРАЖЕНИЙ, ЕСТЬ ПРИВЯЗКИ К Person И Films '''
class ImageSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.Images
        fields = '__all__'


''' СЕРИАЛИЗАТОР ИМЕНИ ФИЛЬМА, ПРИВЯЗКА К Films '''
class FilmNameSerializer(DynamicFieldsModelSerializer):
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
        mdoel = models.ImportSources
        fields = '__all__'

''' СЕРИАЛИЗАТОР ОТНОШЕНИЯ ИСТОЧНИКОВ К ФИЛЬМАМ '''
class FilmsSourcesSerializer(DynamicFieldsModelSerializer):
    source = SourcesSerializer(many = False)
    class Meta:
        model = models.FilmsSources
        fields = '__all__'

'''СЕРИАЛИЗАТОР ОТНОШЕНИЯ РЕЛИЗОВ К ФИЛЬМАМ'''
class FilmReleaseSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.FilmsReleaseDate
        fields = '__all__'
