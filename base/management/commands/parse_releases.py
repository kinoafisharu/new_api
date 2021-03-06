from django.core.management.base import BaseCommand, CommandError
from django.core import exceptions
import requests as req
from bs4 import BeautifulSoup
from parsing import parsers
from datetime import datetime
from base import serializers_helper
from base import models

# Парсит даты релизов с kinoinfo
class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('kids.txt', 'r') as f:
            urls = [{'url': f'http://kinoinfo.ru/film/{i}/', 'id': i} for i in f.read().split(',')]
            for url in urls:
                resp = req.get(url['url'])
                soup = BeautifulSoup(resp.text, 'lxml')
                parser = parsers.KinoinfoParser()
                releasedate = parser.parse_release(soup)
                if releasedate:
                    date = datetime.strptime(str(releasedate), '%d %B %Y')
                    date = datetime.strftime(date, '%Y %m %d').replace(' ', '-')
                    print(date)
                    serializer = serializers_helper.FilmReleaseSerializer(data = {'release': date})
                    if serializer.is_valid():
                        relobj = serializer.save()
                        try:
                            film = models.Films.objects.filter(kid = url['id'])[0]
                            if film.release.exists():
                                for rel in film.release.all():
                                    rel.delete()
                            film.release.add(relobj)
                            self.stdout.write(f'Added on release {relobj.release} to the film {film}')
                        except Exception as e:
                            self.stdout.write(str(e))
