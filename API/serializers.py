from rest_framework import serializers
from . import models

# Сериализатор класса BaseFilms со всеми указанными в классе полями
class BaseFilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BaseFilms
        fields = '__all__'
# -/ Александр Караваев


# Сериализатор класса BaseFilms с ограниченным набором полей для краткого отображения
class ShortBaseFilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BaseFilms
        fields = ['id','year','imdb_id','imdb_votes']
# -/ Александр Караваев
