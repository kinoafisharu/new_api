from rest_framework.serializers import Field
from . import models

class LikeField(Field):
    def get_attribute(self, instance):
        return instance.likes
    def to_representation(self, value):
        return len(value.all())
    def to_internal_value(self, data):
        # IMPLEMENT DATA COLLECTION AND RETURNING DIFFERENT CLASSES
        pass

class FilmPersonStatusField(Field):
    def get_attribute(self, instance):
        return instance.persons.all()
    def to_representation(self, value):
        def get_person_iter():
            for val in value:
                personobject = {}
                personobject['name'] = [i.name for i in val.person.name.all()]
                personobject['role'] = val.action.name
                yield personobject
        objlist = [i for i in get_person_iter()]
        return objlist
