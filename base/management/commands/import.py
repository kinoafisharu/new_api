from django.core.management.base import BaseCommand, CommandError
from base import models, models_dic
from base import serializers
from django.core import exceptions
import io
import datetime
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
            deleted = 0
            created = 0
            for i in file:
                serializer = serializers.AsteroidFilmSerializer(data = i)
                serializer.is_valid()
                sdata = serializer.data
                try:
                    try:

                        idalldvd = sdata.get('idalldvd', None)
                        kid = sdata.get('id', None)
                        try:
                            if idalldvd:
                                d = models.Films.objects.get(imdb_id = idalldvd)
                        except exceptions.MultipleObjectsReturned:
                            filteredmult = models.Films.objects.filter(imdb_id = idalldvd)[0]
                            filteredmult.delete()
                            deleted += 1
                            if idalldvd:
                                d = models.Films.objects.get(imdb_id = idalldvd)
                        except exceptions.ObjectDoesNotExist:
                            try:
                                if kid:
                                    d = models.Films.objects.get(kid = kid)
                            except exceptions.MultipleObjectsReturned:
                                filteredmult = models.Films.objects.filter(kid = kid)[0]
                                filteredmult.delete()
                                deleted += 1
                            except exceptions.ObjectDoesNotExist:
                                self.stdout.write('DOESNOTEXISTERROR !!!!!!!!!!!!!!!! DOES NOT EXIST!!! CREATING!')
                                if idalldvd:
                                    d = models.Films.objects.create(kid = kid, imdb_id = idalldvd)
                                    created += 1
                                else:
                                    d = models.Films.objects.create(kid = kid)
                                    created += 1


                        if d:
                            try:
                                if sdata['name']:
                                    name1 = models.NameFilms.objects.create(name = sdata['name'], status = 1)
                                    d.name.add(name1)
                            except Exception as e:
                                errors += 1
                                self.stdout.write(f'keyerrorname {str(e)}')

                            try:
                                if sdata['original_title']:
                                    name2 = models.NameFilms.objects.create(name = sdata['original_title'], status = 1)
                                    d.name.add(name2)
                            except Exception as e:
                                errors += 1
                                self.stdout.write(f'keyerrorname {str(e)}')



                        if d:
                            try:
                                if sdata['actor1']:
                                    d.persons.add(models.RelationFP.objects.get(person = models.Person.objects.get(id = sdata['actor1'])))
                                    d.creators.add(models.Person.objects.get(id = sdata['actor1']))
                                    relobj = models.RelationFP.objects.get(film = d)
                                    if not relobj.action:
                                        relobj.action = models.Action.objects.get(name = 'актер/актриса')
                            except Exception as e:
                                self.stdout.write(f'person field errored {str(e)}')
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

                        if d:
                            try:
                                d.year = int(sdata['year'])
                            except:
                                errors += 1
                                self.stdout.write('yearerror')
                        if d:
                            try:
                                d.site = str(sdata['site'])
                            except:
                                errors += 1
                                self.stdout.write('siterror')
                        if d:
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
                        if d:
                            try:
                                d.imdb_votes = int(sdata['imdb_votes'])
                            except:
                                errors += 1
                                self.stdout.write('imdbvoteserr')
                        if d:
                            try:
                                if sdata['runtime']:
                                    d.runtime = int(sdata['runtime'])
                            except:
                                errors += 1
                                self.stdout.write('runtimerr')
                        if d:
                            try:
                                d.limits = str(sdata['limits'])
                            except:
                                errors += 1
                                self.stdout.write('limiter')
                        if d:
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
                        if d:
                            try:
                                d.imdb_id = sdata['idalldvd']
                            except KeyError:
                                self.stdout.write(Exception)
                                errors += 1
                                self.stdout.write('imdberror')

                        if d:
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
                        if d:
                            try:
                                d.kid = str(sdata['id'])
                            except:
                                errors += 1
                                self.stdout.write('kiderror!@')
                        if not d.release.all():
                            try:
                                daterel = sdata.get('date', None)
                                if daterel:
                                    dt = datetime.datetime.strptime(daterel, "%Y-%m-%dT%H:%M:%S%z")
                                    releasedate = models.FilmsReleaseDate.objects.create(release = dt)
                                    d.release.add(releasedate)
                            except Exception as e:
                                self.stdout.write('DATETIME ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                self.stdout.write(str(e))
                                errors += 1
                        d.save()
                        processed += 1
                        self.stdout.write(f'Changed one object | iteration: {counter} | errors: {errors} | processed {processed} | n/e {dne} | deleted {deleted} | created {created}')
                    except exceptions.ObjectDoesNotExist:
                        dne += 1
                        self.stdout.write('dneerror')
                    except exceptions.MultipleObjectsReturned:
                        errors += 1
                        self.stdout.write('multipleobjerror')
                except KeyboardInterrupt:
                    break
                except Exception as error:
                    self.stdout.write(f'UNCAUGHT ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! HELPPPPP!!!! || iteration{counter}')
                    self.stdout.write(str(error))
                    continue
                finally:
                    counter += 1
            self.stdout.write(f'Processed {counter} objects | success {processed} | errors {errors} | notexist {dne}')
