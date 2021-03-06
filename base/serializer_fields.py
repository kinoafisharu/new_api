from rest_framework.serializers import Field
from . import serializers_helper
from . import models
from .models_dic import *
from django.utils.translation import gettext_lazy as _

"""
Поля собирают нужные данные с отношений и атрибутов модели и возвращают данные в апи,
структура данных на выходе полностью настраиваемая
"""

'''
Поле для отображения нужных атрибутов персоны,
в сериализаторе модели, связанной с моделью персон
Принимает в качестве аттрибута - objectattributes, что является списком необходимых параметров
'''
class PersonField(Field):
    default_error_messages = {
        'invalid': _('Not a valid string.'),
        'blank': _('This field may not be blank.'),
    }
    initial = ''

    def __init__(self, **kwargs):
        self.objectattributes = kwargs.pop('objectattributes', None)
        super().__init__(**kwargs)

    def get_attribute(self, instance):
        return instance.persons.all()

    def to_representation(self, value):
        def get_person_iter():
            for val in value:
                if self.objectattributes:
                    personobject = {}
                    namelist = [i for i in val.person.name.all()]
                    if 'allnames' in self.objectattributes:
                        personobject['names'] = [i.name for i in namelist]
                    if 'name_main' in self.objectattributes:
                        personobject['name_main'] = [i.name for i in namelist if i.status == 1]
                    if 'name_alt' in self.objectattributes:
                        personobject['name_alt'] = [i.name for i in namelist if i.status == 2]
                    if 'role' in self.objectattributes:
                        personobject['role'] = val.action.name
                    if 'gender' in self.objectattributes:
                        personobject['gender'] = 'male' if val.person.male else 'female'
                    if 'country' in self.objectattributes:
                        personobject['country'] = val.person.country
                    yield personobject
                else:
                    return None
        if get_person_iter():
            objlist = [i for i in get_person_iter()]
            return objlist
        else:
            # TO IMPLEMENT!!!!! ==================================================================
            return None
    def to_internal_value(self, data):
        # CONVERT INCOMING STRING POST REQUEST TO INTERNAL VALUE
        pass
