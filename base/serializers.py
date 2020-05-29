
from rest_framework import serializers
from . import models
from .serializers_dic import *
from .serializers_helper import *
from . import serializer_fields


# -/ Александр Караваев =>
'''
Здесь определяются классы сериализаторов для конкретных моделей
Необходим для преобразования данных из бд, привязанной к ОРМ джанго в нативные типы данных
и дальнейшего их рендера в апи в формате джейсон
'''

'''
Структура класса сериализатора - перед обозначением метакласса указываются вложенные и реляционные отношения,
затем метакласс с названием модели и составом полей, затем методы сериализатора
'''



# Сериализатор класса Films со всеми указанными в классе полями
'''
Используется в детальном отображении фильма в апи, описан в файлах: views.py
Поддерживает динамическое изменение полей при передаче аргумента fields (кортеж с полями)
'''
class FilmsSerializer(DynamicFieldsModelSerializer):

    likes = serializer_fields.LikeField()
    sources = FilmsSourcesSerializer(many = True)
    persons = serializer_fields.PersonField(objectattributes = ['allnames', 'role'])
    name = FilmNameSerializer(many = True, fields = ('name',))
    release = FilmReleaseSerializer(many = True, fields = ('release', 'note'))
    country = CountrySerializer(many = True, fields = ('name',))
    genre = FilmGenreSerializer(many = True, fields = ('name',))
    production = ProductionSerializer(many = True)
    distributor = DistributorSerializer(many = True)
    images = ImageSerializer(many = True, fields = ('file',))
    budget = FilmBudgetSerializer(many = False, fields = ('budget',))
    class Meta:
        model = models.Films
        fields = '__all__'
# -/ Александр Караваев
