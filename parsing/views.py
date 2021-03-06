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
