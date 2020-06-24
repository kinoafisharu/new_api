from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import exceptions
from . import builders
import logging
import random
from . import parsers
from base import models
from kinoinfo import serializers as kserializers

logger = logging.getLogger(__name__)

# http интерфейс для парсинга фильмов,
# принимает POST запрос с id фильма на imdb
class FilmParseView(APIView):
    def post(self, request):
        imdb_id = request.data.get('imdb_id', None)
        url = 'https://www.imdb.com/title/tt{0}/'.format(imdb_id)
        parser = parsers.ImdbParser(url = url, imdb_id = imdb_id, parser = 'lxml')
        data = parser.parse()
        rels = parser.relations
        print(rels)
        if request.data.get('submit', None) == 'true':
            titlebuilder = builders.NameFilmModelBuilder(
                data = rels['title'],
                getter_data = rels['title']
            )
            filmbuilder = builders.FilmModelBuilder(
                data = data,
                getter_data = {'imdb_id': imdb_id},
                fields = ('imdb_id', 'imdb_votes', 'imdb_rate')
            )
            tobj = titlebuilder.build()
            fobj = filmbuilder.build()
            fobj.name.add(tobj)
            return Response({'updated': True, 'fobj': f'{fobj}', 'tobj': f'{tobj.name}', 'imdb_id': imdb_id, 'results': data})
        if not data:
            return Response({'error': 'Ошибка сервера'})
        return Response([data, rels])
