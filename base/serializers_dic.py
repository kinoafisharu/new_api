from rest_framework import serializers
from . import models
from . import models_dic

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models_dic.Country
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models_dic.City
        fields = '__all__'

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models_dic.Action
        fields = '__all__'
