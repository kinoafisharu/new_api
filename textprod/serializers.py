
from rest_framework import serializers
from base import models
from base.serializers_dic import *
from base.mixins import *
from base.serializers_helper import *
from base import serializer_fields


# -/ Александр Караваев =>
'''
Здесь определяются классы сериализаторов для конкретных моделей
Необходим для преобразования данных из бд, привязанной к ОРМ джанго в нативные типы данных
и дальнейшего их рендера в апи в формате джейсон
'''


class StoriesSerializer(DynamicFieldsModelSerializer):
    tags = NewsTagsSerializer(many = True, fields = ('name',))
    class Meta:
        model = models.News
        fields = '__all__'
