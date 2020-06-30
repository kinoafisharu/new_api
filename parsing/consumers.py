import json
from . import parsers
from base import serializers_helper, models
from datetime import datetime, date
from channels.generic.websocket import WebsocketConsumer

class ParseDataConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_json = json.loads(text_data)
        action = text_json['action']
        if action == 'start':
            year_f = int(text_json['year_from'])
            year_t = int(text_json['year_to'])

            if text_json['timecut_by'] == 'year':
                qset = models.Films.objects.distinct('kid').filter(year__range = (year_f, year_t))
            elif text_json['timecut_by'] == 'release':
                date_f = date(year_f, 1, 1)
                date_t = date(year_t, 1, 1)
                qset = models.Films.objects.distinct('kid').filter(release__release__range = (date_f, date_t))
            urls = [{'url': f'http://kinoinfo.ru/film/{film.kid}/', 'kid': film.kid} for film in qset]
            for url in urls:
                parser = parsers.KinoinfoParser(
                    url = url['url'],
                    parser = 'lxml',
                    fields = ['release', 'name'],
                    extra = {'kid': url['kid']}
                )
                data = parser.parse()
                self.send(text_data = json.dumps(data))

        elif text_json['action'] == 'submit':
            data = text_json['data']
            for datestr in data:
                dateparsed = datestr.get('data').get('release', None)
                kid = datestr.get('data').get('kid', None)
                print(dateparsed, kid)
                if dateparsed:
                    date = datetime.strptime(dateparsed, '%d %B %Y')
                    date = datetime.strftime(date, '%Y %m %d').replace(' ', '-')
                else:
                    date = None
                serializer = serializers_helper.FilmReleaseSerializer(data = {'release': date})
                if serializer.is_valid():
                    relobj = serializer.save()
                    try:
                        film = models.Films.objects.distinct('kid').get(kid = kid)
                        if film.release.exists():
                            for rel in film.release.all():
                                rel.delete()
                        film.release.add(relobj)
                    except Exception as e:
                        str(e)
