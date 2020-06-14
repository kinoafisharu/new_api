from rest_framework.serializers import Field
from base import serializers_helper
from base import models
from base.models_dic import *


class SourceFilmsField(Field):
    def get_attribute(self, instance):
        return instance.sourcefilms_set.all()
    def to_representation(self, value):
        serializer = serializers_helper.SourceFilmsSerializer(value, many = True, fields = ('name','name_alter','year','imdb','text','extra', 'top250_set'))
        return serializer.data
