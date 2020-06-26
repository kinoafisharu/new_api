from rest_framework import serializers
from collections import OrderedDict
from django.core import exceptions

# Non-field imports, but public API
from rest_framework.fields import (
     SkipField
)
from rest_framework.relations import PKOnlyObject


# Александр Караваев  ===>
'''
Класс для создания подклассов serializer с динамическим набором полей, описан в документации djangorestframework
'''
class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        self.repfields = kwargs.pop('repfields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    def to_representation(self, instance):
        ret = OrderedDict()
        fields = self._readable_fields
        allowed = set(self.repfields) if self.repfields else None


        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            check_for_none = attribute.pk if isinstance(attribute, PKOnlyObject) else attribute
            if check_for_none is None:
                ret[field.field_name] = None
            else:
                ret[field.field_name] = field.to_representation(attribute)
        retc = ret.copy()
        if allowed:
            for key in ret.keys():
                if key not in allowed:
                    del retc[key]
        return retc

    def get_first_or_create(self, model = None, data = None, **kwargs):
        model = self.Meta.model if not model else model
        try:
            getter_data = kwargs.pop('getter_data', None)
            if getter_data:
                obj = model.objects.get(**getter_data)
            else:
                obj = model.objects.get(**data)
        except exceptions.ObjectDoesNotExist as e:
            obj = model.objects.create(**data)
        except exceptions.MultipleObjectsReturned:
            obj = model.objects.filter(**data)[0]
        return obj if obj else None
#====================================================================================
