from rest_framework import serializers
from . import models
from .serializers_dic import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Images
        fields = '__all__'


class FilmNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NameFilms
        fields = '__all__'

class NamePersonSerialzier(serializers.ModelSerializer):
    class Meta:
        model = models.NamePerson
        fields = '__all__'

class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    name = NamePersonSerialzier(many = True)
    poster = ImageSerializer(many = True)
    city = CitySerializer(many = False)
    class Meta:
        model = models.Person
        exclude = ['musician',]

class StatusSerializer(serializers.ModelSerializer):
    action = ActionSerializer(many = False)
    person = PersonSerializer(many = False)
    class Meta:
        model = models.RelationFP
        fields = '__all__'


class FilmReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FilmsReleaseDate
        fields = '__all__'


class FilmGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = '__all__'

class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductionsCo
        fields = '__all__'

class NameDistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NameDistributors
        fields = '__all__'

class DistributorSerializer(serializers.ModelSerializer):
    name = NameDistributorSerializer(many = True)
    class Meta:
        model = models.Distributors
        fields = '__all__'


class FilmBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Budget
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Likes
        fields = '__all__'

# Сериализатор класса BaseFilms со всеми указанными в классе полями
class FilmsSerializer(serializers.ModelSerializer):
    likes_set = LikeSerializer(many = True)
    relationfp_set = StatusSerializer(many = True)
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
    # def validate(self, data):
        # if data['runtime'] < 0:
            # raise serializers.ValidationError('Fillm cannot last less than 0 min, your YEAR input contains input['year'] < 0')
        # return data

    # OBJECT CREATING LOGIC ========================>
    # def create(self, validated_data):
    #     obj = models.BaseFilms(**validated_data)
    #     obj.save()


    # OBJECT UPDATING LOGIC =================================>
    # def update(self, instance, validated_data):
    #
    #     instance.field = validated_data.get('field_name', instance.field) # second value as default if no value in dict

# -/ Александр Караваев


# Сериализатор класса BaseFilms с ограниченным набором полей для краткого отображения
class ShortFilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Films
        fields = ['id','year','imdb_id','imdb_votes']
# -/ Александр Караваев
