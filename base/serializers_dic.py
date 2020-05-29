from rest_framework import serializers
from . import models
from . import models_dic
from .serializers_helper import DynamicFieldsModelSerializer

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
