from base.models import Films
from django.core import exceptions
import json

class ScrapyCrawlPipeline(object):
    def __init__(self, *args, **kwargs):
        self.items = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls

    def close_spider(self, spider):
        try:
            film = Films.objects.get(imdb_id = self.items.imdb_id)
            film.update(data = json.dumps(self.items))
            film.save()
        except exceptions.ObjectDoesNotExist as e:
            film = Films()
            film.data = json.dumps(self.items)
        except exceptions.MultipleObjectsReturned as e:
            print(e)



    def process_item(self, item, spider):
        self.items.append(item['title'])
        self.items.append(item['imdb_id'])
        return item
