from django.core import exceptions
import logging

logger = logging.getLogger(__name__)

'''
  Базовые классы строителей
  Нужны для построения обьекта модели в бд из документа json
  С крайне строгой валидацией
  Во избежание появления мусора в бд
'''

# Базовый класс строителя модели
# Хранит в себе возможность расширения,
# валидирует самый базовый и необхоимый функционал
class BaseModelBuilder():
    def build(self):
        raise NotImplementedError('.build() must be overriden')

# Метакласс для каждого дочернего строителя модели
# хранит нуный функционал и методы валидации и обработки ошибок
class ModelBuilder(BaseModelBuilder):
    def __init__(self, *args, **kwargs):
        self.data = kwargs.pop('data', None)
        self.getter_data = kwargs.pop('getter_data', None)
        assert self.serializer_class
        assert self.model

    # Получить обьект по заданным свойствам, если обьектов несколько, получить первый
    # Если обьектов нет - возвращает  none
    def get_object(self):
        try:
            obj = self.model.objects.get(**self.getter_data)
            print(self.getter_data)
            print(obj)
            return obj
        except exceptions.ObjectDoesNotExist:
            return None
        except exceptions.MultipleObjectsReturned as e:
            obj = self.model.objects.filter(**self.getter_data)
            print(obj[0])
            print(self.getter_data)
            return obj[0]

    # Если обьект есть - получить сериализатор с данными и с обьектом
    # (<= для будущего обновления данных обьекта)
    # Если обьекта нету, только с данными, для его создания
    def get_serializer(self, fields, data, object):
        serializer = self.serializer_class(object, data = data, fields = fields)
        if not object:
            serializer = self.serializer_class(data = data, fields = fields)
        if serializer.is_valid():
            return serializer
        raise ValidationError('Serializer is not valid data')

    #  Сохранить или обновить обьект
    def save_model(self, serializer):
        return serializer.save()
