from . import models
from . import serializers_helper

def save_film_namedata(namedata, fields):
    serializer = FilmNameSerializer(data = namedata, fields = fields)
    if serializer.is_valid():
        name = serializer.save()
        return name
