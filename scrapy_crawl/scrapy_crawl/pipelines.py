import logging
import random
from base import models
from django.core import exceptions
import json

logger = logging.getLogger(__name__)

class ScrapyCrawlPipeline(object):
    def __init__(self, *args, **kwargs):
        self.items = {}


    def close_spider(self, spider):
        try:
            film = models.Films.objects.get(imdb_id = self.items['imdb_id'])
            name = models.NameFilms.objects.create(name = self.items['title'], status = 1)
            film.name.add(name)
            film.save()
            logger.info(film.name.all())
        except exceptions.ObjectDoesNotExist as e:
            name = models.NameFilms.objects.create(name = self.items['title'], status = 1)
            film = models.Films.objects.create(id = random.randint(1000000,9999999))
            film.imdb_id = self.items['imdb_id']
            film.name.add(name)
            film.save()
            logger.info(film.name.all())
        except exceptions.MultipleObjectsReturned as e:
            print(e)


    def process_item(self, item, spider):
        self.items['title'] = item['title']
        self.items['imdb_id'] = item['imdb_id']
        return item
