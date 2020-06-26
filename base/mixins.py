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

    # Глубокое ограничение полей сериализатора (на уровне задания класса)
    # Позволяет сохранять неполные данные, оставляя сериализатор валидным
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

    def create(self, validated_data):
        return self.get_first_or_create(model = self.Meta.model, data = validated_data)

    # Переписанный мтеод реперезентации
    # Возможность динамического отображения полей, без изменения их количества при
    # создании обьекта через десериализацию
    def to_representation(self, instance):
        ret = OrderedDict()
        fields = self._readable_fields
        # Набор полей для отображения в апи
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
        # Копировать исходный словарь с полями для отображения
        retc = ret.copy()
        # Если указано ограничение полей
        if allowed:
            # Для поля в оригинальном словаре
            for key in ret.keys():
                # Если поле не входит в ограниченный набор полей, указанный ранее
                if key not in allowed:
                    # Вычесть поле из скопированного словаря (копируем словарь во избежание ошибки мутации во время итераций)
                    del retc[key]
        # Возвращаем измененный словарь
        return retc

    # Взять значение из бд, если нет создать, если возвращено больше одного - взять первое
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
        assert obj
        return obj if obj else None

#====================================================================================
