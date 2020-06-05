from django.core.management.base import BaseCommand, CommandError
from base import models, models_dic
from base import serializers
from django.core import exceptions
import io
import json
from rest_framework.parsers import JSONParser

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('data.json', 'r') as f:
            file = json.load(f)
            counter = 0
            errors = 0
            processed = 0
            dne = 0
            for i in file:
                serializer = serializers.AsteroidFilmSerializer(data = i)
                serializer.is_valid()
                sdata = serializer.data
                try:
                    try:


                        try:
                            d = models.Films.objects.get(imdb_id = sdata['idalldvd'])
                        except exceptions.ObjectDoesNotExist:
                            if sdata['id']:
                                d = models.Films.objects.get(kid = sdata['id'])
                        except exceptions.MultipleObjectsReturned:
                            if sdata['id']:
                                d = models.Films.objects.get(kid = sdata['id'])




                        if not d.name.all():
                            try:
                                if sdata['name']:
                                    name1 = models.NameFilms.objects.create(name = sdata['name'], status = 1)
                                    d.name.add(name1)
                            except:
                                errors += 1
                                self.stdout.write('keyerrorname')

                            try:
                                if sdata['original_title']:
                                    name2 = models.NameFilms.objects.create(name = sdata['original_title'], status = 1)
                                    d.name.add(name2)
                            except:
                                errors += 1
                                self.stdout.write('keyerrorname')



                        if not d.persons.all():
                            try:
                                if sdata['actor1']:
                                    d.persons.add(models.RelationFP.objects.get(person = models.Person.objects.get(id = sdata['actor1'])))
                                    d.creators.add(models.Person.objects.get(id = sdata['actor1']))
                                    relobj = models.RelationFP.objects.get(film = d)
                                    if not relobj.action:
                                        relobj.action = models.Action.objects.get(name = 'актер/актриса')
                            except:
                                self.stdout.write('person field errored')
                                errors += 1

                            try:
                                if sdata['actor2']:
                                    d.persons.add(models.RelationFP.objects.get(person = models.Person.objects.get(id = sdata['actor2'])))
                                    d.creators.add(models.Person.objects.get(id = sdata['actor2']))
                                    relobj = models.RelationFP.objects.get(film = d)
                                    if not relobj.action:
                                        relobj.action = models.Action.objects.get(name = 'актер/актриса')
                            except:
                                self.stdout.write('person field errored')
                                errors += 1


                            try:
                                if sdata['actor3']:
                                    d.persons.add(models.RelationFP.objects.get(person = models.Person.objects.get(id = sdata['actor3'])))
                                    d.creators.add(models.Person.objects.get(id = sdata['actor3']))
                                    relobj = models.RelationFP.objects.get(film = d)
                                    if not relobj.action:
                                        relobj.action = models.Action.objects.get(name = 'актер/актриса')
                            except:
                                self.stdout.write('person field errored')
                                errors += 1

                            try:
                                if sdata['actor4']:
                                    d.persons.add(models.RelationFP.objects.get(person = models.Person.objects.get(id = sdata['actor4'])))
                                    d.creators.add(models.Person.objects.get(id = sdata['actor4']))
                                    relobj = models.RelationFP.objects.get(film = d)
                                    if not relobj.action:
                                        relobj.action = models.Action.objects.get(name = 'актер/актриса')
                            except:
                                self.stdout.write('person field errored')
                                errors += 1


                            try:
                                if sdata['actor5']:
                                    d.persons.add(models.RelationFP.objects.get(person = models.Person.objects.get(id = sdata['actor5'])))
                                    d.creators.add(models.Person.objects.get(id = sdata['actor5']))
                                    relobj = models.RelationFP.objects.get(film = d)
                                    if not relobj.action:
                                        relobj.action = models.Action.objects.get(name = 'актер/актриса')
                            except:
                                self.stdout.write('person field errored')
                                errors += 1


                            try:
                                if sdata['actor6']:
                                    d.persons.add(models.RelationFP.objects.get(person = models.Person.objects.get(id = sdata['actor6'])))
                                    d.creators.add(models.Person.objects.get(id = sdata['actor6']))
                                    relobj = models.RelationFP.objects.get(film = d)
                                    if not relobj.action:
                                        relobj.action = models.Action.objects.get(name = 'актер/актриса')
                            except:
                                self.stdout.write('person field errored')
                                errors += 1



                            try:
                                if sdata['director1']:
                                    d.creators.add(models.Person.objects.get(id = sdata['director1']))
                            except:
                                self.stdout.write('director not added')
                                errors += 1



                            try:
                                if sdata['director2']:
                                    d.creators.add(models.Person.objects.get(id = sdata['director2']))
                            except:
                                self.stdout.write('director not added')
                                errors += 1


                            try:
                                if sdata['director3']:
                                    d.creators.add(models.Person.objects.get(id = sdata['director3']))
                            except:
                                self.stdout.write('director not added')
                                errors += 1

                        if not d.year:
                            try:
                                d.year = int(sdata['year'])
                            except:
                                errors += 1
                                self.stdout.write('yearerror')
                        if not d.site:
                            try:
                                d.site = str(sdata['site'])
                            except:
                                errors += 1
                                self.stdout.write('siterror')
                        if not d.imdb_rate:
                            try:
                                if sdata['imdb']:
                                    d.imdb_rate = float(sdata['imdb'].replace(',','.').replace(':','.'))
                            except ValueError:
                                self.stdout.write(sdata['imdb'])
                                errors += 1
                                self.stdout.write('imdberrVALUE')
                            except AttributeError:
                                errors += 1
                                self.stdout.write(sdata['imdb'])
                                self.stdout.write('imdberr')
                        if not d.imdb_votes:
                            try:
                                d.imdb_votes = int(sdata['imdb_votes'])
                            except:
                                errors += 1
                                self.stdout.write('imdbvoteserr')
                        if not d.runtime:
                            try:
                                if sdata['runtime']:
                                    d.runtime = int(sdata['runtime'])
                            except:
                                errors += 1
                                self.stdout.write('runtimerr')
                        if not d.limits:
                            try:
                                d.limits = str(sdata['limits'])
                            except:
                                errors += 1
                                self.stdout.write('limiter')
                        if not d.description:
                            try:
                                d.description = str(sdata['description'])
                            except:
                                errors += 1
                                self.stdout.write('descripterror')
                        if not d.comment:
                            try:
                                d.comment = str(sdata['comment'])
                            except:
                                errors += 1
                                self.stdout.write('commenterror')
                        if not d.imdb_id:
                            try:
                                d.imdb_id = sdata['idalldvd']
                            except KeyError:
                                self.stdout.write(Exception)
                                errors += 1
                                self.stdout.write('imdberror')

                        if not d.genre.all():
                            try:
                                if sdata['genre1']:
                                    d.genre.add(models_dic.Genre.objects.get(id = sdata['genre1']))
                            except:
                                errors += 1
                                self.stdout.write('genreerror')
                            try:
                                if sdata['genre2']:
                                    d.genre.add(models_dic.Genre.objects.get(id = sdata['genre2']))
                            except:
                                errors += 1
                                self.stdout.write('genreerror')
                            try:
                                if sdata['genre3']:
                                    d.genre.add(models_dic.Genre.objects.get(id = sdata['genre3']))
                            except:
                                errors += 1
                                self.stdout.write('genreerror')
                        if not d.kid:
                            try:
                                d.kid = sdata['id']
                            except:
                                errors += 1
                                self.stdout.write('kiderror!@')
                        d.save()
                        processed += 1
                        self.stdout.write(f'Changed one object | iteration: {counter} | errors: {errors} | processed {processed} | n/e {dne}')
                    except exceptions.ObjectDoesNotExist:
                        dne += 1
                        self.stdout.write('dneerror')
                    except exceptions.MultipleObjectsReturned:
                        errors += 1
                        self.stdout.write('multipleobjerror')
                except KeyboardInterrupt:
                    break
                except:
                    self.stdout.write(f'UNCAUGHT ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! HELPPPPP!!!! || iteration{counter}')
                    continue
                finally:
                    counter += 1
            self.stdout.write(f'Processed {counter} objects | success {processed} | errors {errors} | notexist {dne}')
