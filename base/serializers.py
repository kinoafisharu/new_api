from rest_framework import serializers
from . import models
from .serializers_dic import *
from . import serializer_fields

# -/ Александр Караваев =>

''' СЕРИАЛИЗАЦИЯ ИЗОБРАЖЕНИЙ, ЕСТЬ ПРИВЯЗКИ К Person И Films '''
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Images
        fields = '__all__'

class FilmSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Session
        fields = '__all__'

''' СЕРИАЛИЗАТОР ИМЕНИ ФИЛЬМА, ПРИВЯЗКА К Films '''
class FilmNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NameFilms
        fields = '__all__'

''' СЕРИАЛИЗАТОР ИМЕН ПЕРСОН, ПРИВЯЗКА К Person '''
class NamePersonSerialzier(serializers.ModelSerializer):
    class Meta:
        model = models.NamePerson
        fields = '__all__'
        
''' СЕРИАЛИЗАТОР МУЗЫКАНТОВ, В МОДЕЛИ ОТСЫЛКА M2M К SELF '''
class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = '__all__'

'''СЕРИАЛИЗАТОР ПЕРСОНЫ, ЕСТЬ ПРИВЯЗКА К Films '''
class PersonSerializer(serializers.ModelSerializer):
    name = NamePersonSerialzier(many = True)
    poster = ImageSerializer(many = True)
    city = CitySerializer(many = False)
    country = CountrySerializer(many = False)
    class Meta:
        model = models.Person
        exclude = ['musician',]


''' СЕРИАЛИЗАТОР ДАННЫХ ПО ДАТЕ РЕЛИЗА ФИЛЬМА (ЗАМЕНИТЬ НА ВЫДЕЛЕННОЕ ПОЛЕ) '''
class FilmReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FilmsReleaseDate
        fields = '__all__'


''' СЕРИАЛИЗАТОР ЖАНРА ФИЛЬМА (ЗАМЕНИТЬ НА ВЫДЕЛЕННОЕ ПОЛЕ) '''
class FilmGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = '__all__'

''' СЕРИАЛИЗАТОР ПРОИЗВОДИТЕЛЯ ФИЛЬМА, ПРИВЯЗКА К Films '''
class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductionsCo
        fields = '__all__'

''' СЕРИАЛИЗАТОР ИМЕНИ ДИСТРИБЬЮТОРА '''
class NameDistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NameDistributors
        fields = '__all__'

''' СЕРИАЛИЗАТОР ДИСТРИБЬЮТОРА '''
class DistributorSerializer(serializers.ModelSerializer):
    name = NameDistributorSerializer(many = True)
    class Meta:
        model = models.Distributors
        fields = '__all__'

''' СЕРИАЛИЗАТОР БЮДЖЕТА ФИЛЬМА (ЗАМЕНИТЬ ВЫДЕЛЕННЫМ ПОЛЕМ) '''
class FilmBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Budget
        fields = '__all__'

''' СЕРИАЛИЗАТОР ИСТОЧНИКОВ '''
class SourcesSerializer(serializers.ModelSerializer):
    class Meta:
        mdoel = models.ImportSources
        fields = '__all__'
''' СЕРИАЛИЗАТОР ОТНОШЕНИЯ ИСТОЧНИКОВ К ФИЛЬМАМ '''
class FilmsSourcesSerializer(serializers.ModelSerializer):
    source = SourcesSerializer(many = False)
    class Meta:
        model = models.FilmsSources
        fields = '__all__'
        
        
# Сериализатор класса Films со всеми указанными в классе полями
class FilmsSerializer(serializers.ModelSerializer):
    likes = serializer_fields.LikeField()
    sources = FilmsSourcesSerializer(many = True)
    persons = serializer_fields.FilmPersonStatusField()
    name = FilmNameSerializer(many = True)
    creators = PersonSerializer(many = True)
    release = FilmReleaseSerializer(many = True)
    country = CountrySerializer(many = True)
    genre = FilmGenreSerializer(many = True)
    production = ProductionSerializer(many = True)
    distributor = DistributorSerializer(many = True)
    images = ImageSerializer(many = True)
    budget = FilmBudgetSerializer(many = False)
    class Meta:
        model = models.Films
        fields = '__all__'

    # VALIDATION FOR EVERY SINGLE FIELD ===================>
    # def validate_(field_name):
        #some actions

    #OBJECT LEVEL VALIDATION =========================>
    def validate(self, data):
        if data['runtime'] and data['runtime'] < 0:
            raise serializers.ValidationError('Fillm cannot last less than 0 min, your YEAR input contains input value YEAR < 0')
        return data

    # OBJECT CREATING LOGIC ========================>
    def create(self, validated_data):
        obj = models.BaseFilms(**validated_data)
        obj.save()


    # OBJECT UPDATING LOGIC =================================>
    # def update(self, instance, validated_data):
    #     instance.field = validated_data.get('field_name', instance.field) # second value as default if no value in dict

# -/ Александр Караваев


# Сериализатор класса Films с ограниченным набором полей для краткого отображения
class ShortFilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Films
        fields = ['id','year','imdb_id','kid']
# -/ Александр Караваев
