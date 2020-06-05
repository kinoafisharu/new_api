from rest_framework import serializers
from .mixins import *
from . import models
from . import models_dic

"""
В этом файле описываются все модели - словари
"""
class CountrySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models_dic.Country
        fields = '__all__'

class CitySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models_dic.City
        fields = '__all__'

class ActionSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models_dic.Action
        fields = '__all__'
