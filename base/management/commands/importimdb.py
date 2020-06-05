
from django.core.management.base import BaseCommand, CommandError
from base import models, models_dic
from base import serializers
from django.core import exceptions
import io
import json
from rest_framework.parsers import JSONParser

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('data.json', 'r') as f:
            file = json.load(f)
            counter = 0
            errors = 0
            for i in file:
                serializer = serializers.AsteroidFilmSerializer(data = i)
                serializer.is_valid()
                sdata = serializer.data
                try:
                    try:
                        film = models.Films.objects.get(imdb_id = sdata['idalldvd'])
                    except exceptions.ObjectDoesNotExist:
                        if sdata['id']:
                            film = models.Films.objects.get(kid = sdata['id'])
                    except exceptions.MultipleObjectsReturned:
                        if sdata['id']:
                            film = models.Films.objects.get(kid = sdata['id'])

                    except:
                        self.stdout.write('error')

                    try:
                        if sdata.get('idalldvd', None):
                            film.imdb_id = sdata['idalldvd']
                            film.save()
                    except:
                        errors += 1
                except KeyboardInterrupt:
                    break
                except:
                    errors += 1
                counter += 1
                self.stdout.write(f'{counter} ||| {errors}')
