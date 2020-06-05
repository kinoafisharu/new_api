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
                        if sdata['country']:
                            country = models_dic.Country.objects.get(id = sdata['country'])
                            film.country.add(country)
                    except:
                        self.stdout.write('error')
                    try:
                        if sdata['country2']:
                            country = models_dic.Country.objects.get(id = sdata['country'])
                            film.country.add(country)
                    except:
                        self.stdout.write('error')

                    try:
                        if sdata['actor1']:
                            person = models.Person.objects.get(kid = sdata['actor1'])
                            relation = models.RelationFP.objects.get(person = person)
                            film.persons.add(relation)
                            film.creators.add(person)
                            relobj = models.RelationFP.objects.get(film = film)
                            if not relobj.action:
                                relobj.action = models.Action.objects.get(name = 'актер/актриса')
                    except:
                        self.stdout.write('person field errored')
                        errors += 1
                    try:
                        if sdata['actor2']:
                            person = models.Person.objects.get(kid = sdata['actor2'])
                            relation = models.RelationFP.objects.get(person = person)
                            film.persons.add(relation)
                            film.creators.add(person)
                            relobj = models.RelationFP.objects.get(film = film)
                            if not relobj.action:
                                relobj.action = models.Action.objects.get(name = 'актер/актриса')
                    except:
                        self.stdout.write('person field errored')
                        errors += 1
                    try:
                        if sdata['actor3']:
                            person = models.Person.objects.get(kid = sdata['actor3'])
                            relation = models.RelationFP.objects.get(person = person)
                            film.persons.add(relation)
                            film.creators.add(person)
                            relobj = models.RelationFP.objects.get(film = film)
                            if not relobj.action:
                                relobj.action = models.Action.objects.get(name = 'актер/актриса')
                    except:
                        self.stdout.write('person field errored')
                        errors += 1
                    try:
                        if sdata['actor4']:
                            person = models.Person.objects.get(kid = sdata['actor4'])
                            relation = models.RelationFP.objects.get(person = person)
                            film.persons.add(relation)
                            film.creators.add(person)
                            relobj = models.RelationFP.objects.get(film = film)
                            if not relobj.action:
                                relobj.action = models.Action.objects.get(name = 'актер/актриса')
                    except:
                        self.stdout.write('person field errored')
                        errors += 1
                    try:
                        if sdata['actor5']:
                            person = models.Person.objects.get(kid = sdata['actor5'])
                            relation = models.RelationFP.objects.get(person = person)
                            film.persons.add(relation)
                            film.creators.add(person)
                            relobj = models.RelationFP.objects.get(film = film)
                            if not relobj.action:
                                relobj.action = models.Action.objects.get(name = 'актер/актриса')
                    except:
                        self.stdout.write('person field errored')
                        errors += 1
                    try:
                        if sdata['actor6']:
                            person = models.Person.objects.get(kid = sdata['actor6'])
                            relation = models.RelationFP.objects.get(person = person)
                            film.persons.add(relation)
                            film.creators.add(person)
                            relobj = models.RelationFP.objects.get(film = film)
                            if not relobj.action:
                                relobj.action = models.Action.objects.get(name = 'актер/актриса')
                    except:
                        self.stdout.write('person field errored')
                        errors += 1
                    try:
                        if sdata['genre1']:
                            genre = models_dic.Genre.objects.get(kid = sdata['genre1'])
                            film.Genre.add(genre)
                    except:
                        self.stdout.write('shit')
                        self.stdout.write(sdata['genre1'])
                    try:
                        if sdata['genre2']:
                            genre = models_dic.Genre.objects.get(kid = sdata['genre2'])
                            film.Genre.add(genre)
                    except:
                        self.stdout.write('shit')
                        self.stdout.write(sdata['genre2'])
                    try:
                        if sdata['genre3']:
                            genre = models_dic.Genre.objects.get(kid = sdata['genre3'])
                            film.Genre.add(genre)
                    except:
                        self.stdout.write('shit')
                        self.stdout.write(sdata['genre3'])
                except:
                    pass
                counter += 1
                self.stdout.write(f'iteration {counter} ======> {errors}')
