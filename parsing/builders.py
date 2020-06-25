from base.parsing import builders
from base import models
import logging
from django.core import exceptions
from base import serializers_helper
from kinoinfo import serializers as kserializers

logger = logging.getLogger(__name__)


 # Файл содержит классы - строители для строгой валидации
 # и записи json файлов в SQL базу данных с помощью
 # сериализаторов и ORM django

# Создает обьекты фильмов
class FilmModelBuilder(builders.ModelBuilder):
    model = models.Films
    serializer_class = kserializers.FilmsSerializer
    def __init__(self, *args, **kwargs):
        self.fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)
    def build(self):
        object = self.get_object()
        serializer = self.get_serializer(fields = self.fields, data = self.data, object = object)
        if serializer:
            obj = serializer.save()
        return obj
