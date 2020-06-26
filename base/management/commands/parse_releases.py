from django.core.management.base import BaseCommand, CommandError
from django.core import exceptions
import requests as req
from bs4 import BeautifulSoup
from parsing import parsers
from datetime import datetime
from base import serializers_helper
from base import models

class Command(BaseCommand):
    def handle(self, *args, **options):
        urls = [{'url': f'http://kinoinfo.ru/film/{i}/', 'id': i} for i in range(35000, 42000)]
        for url in urls:
            resp = req.get(url['url'])
            soup = BeautifulSoup(resp.text, 'lxml')
            parser = parsers.KinoinfoParser()
            releasedate = parser.parse_releases(soup)
            if releasedate:
                date = datetime.strptime(str(releasedate), '%d %B %Y')
                date = datetime.strftime(date, '%Y %m %d').replace(' ', '-')
                print(date)
                serializer = serializers_helper.FilmReleaseSerializer(data = {'release': date})
                if serializer.is_valid():
                    relobj = serializer.save()
                    try:
                        film = models.Films.objects.distinct('kid').filter(kid = url['id'])[0]
                    except Exception as e:
                        continue

                    film.release.add(relobj)
                    self.stdout.write(f'Added one release {relobj} to the film {film}')
