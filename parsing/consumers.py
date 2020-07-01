import json
from . import parsers
from base import serializers_helper, models
from kinoinfo import serializers as kserializers
from datetime import datetime, date
from channels.db import database_sync_to_async as db_async_conn
from base.consumers import ModAsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer

class ParseDataConsumer(WebsocketConsumer):


    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def get_urls(self, qset):
        for film in qset:
            obj = {
                'url': f'http://kinoinfo.ru/film/{film.kid}/',
                'kid': film.kid,
                'imdb': film.imdb_id,
            }
            yield obj

    def process_url(self, url):
        imdb_id_wrong = url.get('imdb', None)
        parser = parsers.KinoinfoParser(
            url = url['url'],
            fields = ['release'],
            extra = {
                'kid': url['kid'],
            }
        )
        data = parser.parse()
        if imdb_id_wrong:
            imdb_id = imdb_id_wrong if len(url['imdb']) >= 7 else '0' * 7 - len(url['imdb']) + url['imdb']
            imdb_url = f'https://www.imdb.com/title/tt{imdb_id}'
            parser_imdb = parsers.ImdbParser(
                url = imdb_url,
            )
            data_imdb = parser_imdb.parse()
            data.update(data_imdb)
        return data

    def on_start_parsing(self, text_json):
        year_f = int(text_json['year_from'])
        year_t = int(text_json['year_to'])

        if text_json['timecut_by'] == 'year':
            qset = models.Films.objects.distinct(
                'kid'
            ).filter(
                year__range = (year_f, year_t)
            )
        elif text_json['timecut_by'] == 'release':
            date_f = date(year_f, 1, 1)
            date_t = date(year_t, 1, 1)
            qset = models.Films.objects.distinct(
                'kid'
            ).filter(
                release__release__range = (date_f, date_t)
            )

        urls = self.get_urls(qset)

        for url in urls:
            data = self.process_url(url)
            self.send(text_data = json.dumps(data))

    def on_submit_result(self, text_json):
        data = text_json.get('data', None)
        print(data)
        for film in data:
            serializer = kserializers.FilmsSerializer(
                    data = film['data'],
                    fields = (film['data'].keys())
                )
            print(serializer.initial_data)
            if serializer.is_valid():
                d = serializer.save()
                print('saved', d)
            else:
                print(serializer.errors)


    def receive(self, text_data):
        text_json = json.loads(text_data)
        action = text_json['action']
        if action == 'start':
            self.on_start_parsing(text_json)
        elif action == 'submit':
            self.on_submit_result(text_json)
