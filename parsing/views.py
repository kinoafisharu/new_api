from rest_framework.views import APIView
from rest_framework.response import Response
from urllib.parse import urlparse
from django.core import exceptions
import logging
import random
import os
from scrapy_crawl.scrapy_crawl.spiders.imdb_crawler import ImdbSpider
from base import models
from uuid import uuid4
from kinoinfo import serializers as kserializers
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render
from scrapyd_api import ScrapydAPI
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup
import requests as req

logger = logging.getLogger(__name__)

class FilmParseView(APIView):
    def post(self, request):
        imdb_id = request.data.get('imdb_id', None)
        resp = req.get('https://www.imdb.com/title/tt{0}/'.format(imdb_id))
        soup = BeautifulSoup(resp.text, 'lxml')
        title = soup.find('div', {'class': 'title_wrapper'})
        title = title.find('h1')
        title.span.decompose()
        title = title.get_text().strip()
        try:
            film = models.Films.objects.get(imdb_id = imdb_id)
            name = models.NameFilms.objects.create(name = title, status = 1)
            film.name.add(name)
            film.save()
            logger.info(film.name.all())
        except exceptions.ObjectDoesNotExist as e:
            name = models.NameFilms.objects.create(name = title, status = 1)
            film = models.Films.objects.create(id = random.randint(1000000,9999999))
            film.imdb_id = imdb_id
            film.name.add(name)
            film.save()
            logger.info(film.name.all())
        except exceptions.MultipleObjectsReturned as e:
            print(e)
        return Response({'task_id': '1', 'name': str(title)})

    def get(self, request):
        imdb_id = request.query_params.get('imdb_id', None)
        try:
            item = models.Films.objects.get(imdb_id = str(imdb_id))
            serializer = kserializers.FilmsSerializer(item)
            return Response({'data': serializer.data})
        except Exception as e:
            return Response({'error': str(e)})
