from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import exceptions
from . import builders
import logging
import random
from . import parsers
from base import models, serializers_helper
import requests as req
from bs4 import BeautifulSoup
from datetime import datetime
from kinoinfo import serializers as kserializers

logger = logging.getLogger(__name__)

# http интерфейс для парсинга фильмов,
# принимает POST запрос с id фильма на imdb
class FilmDotParseView(APIView):
    def post(self, request):
        if request.data.get('id_type', None) == 'imdb':
            imdb_id = request.data.get('imdb_id', None)
            url = 'https://www.imdb.com/title/tt{0}/'.format(imdb_id)
            parser = parsers.ImdbParser(
                url = url,
                parser = 'lxml',
                extra = {'imdb_id': imdb_id}
            )
        elif request.data.get('id_type', None) == 'kinoinfo':
            kid = request.data.get('kid', None)
            url = 'http://kinoinfo.ru/film/{0}/'.format(kid)
            parser = parsers.KinoinfoParser(url = url, parser = 'lxml', fields = ['poster'])
        data = parser.parse()

        if request.data.get('submit', None) == 'true':

            filmbuilder = builders.FilmModelBuilder(
                data = data,
                getter_data = {'imdb_id': imdb_id},
                fields = ('imdb_id', 'imdb_votes', 'imdb_rate', 'name')
            )

            fobj = filmbuilder.build()

            return Response([data, {'fobj': str(fobj)}])
        if not data:
            return Response({'error': 'Ошибка сервера'})
        return Response(data)

class FilmStreamParseView(APIView):

    def post(self, request):
        start = request.data.get('start', None)
        if start == 'true':
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
                                film = models.Films.objects.distinct('kid').filter(kid = url['id'])[0]
                                film.release.add(relobj)
                                string = (
                                    f'Добавлена одна дата релиза {relobj.release} к фильму {film}\n'
                                    f'с существующими датами релизов {[release.release for release in film.release.all()]}\n\n'
                                )
                                with open('result.txt', 'a') as result:
                                    result.write(string)
                            except Exception as e:
                                continue
            return Response({'processed': 'true'})
        return Respones({'errors': 'No args provided'})
    def get(self, request):
        with open('result.txt', 'r') as f:
            return Response({'data': f.read()[:10000]})
