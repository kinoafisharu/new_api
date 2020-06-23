from rest_framework.views import APIView
from rest_framework.response import Response
import os
from scrapyd.config import Config
from urllib.parse import urlparse
from base import models
from uuid import uuid4
from kinoinfo import serializers as kserializers
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render
from scrapyd_api import ScrapydAPI
from base.models import Films
conf = Config()
port = conf.get('http_port')
scrapyd = ScrapydAPI('http://0.0.0.0:{0}'.format(port))

class FilmParseView(APIView):
    def post(self, request):
        imdb_id = request.data.get('imdb_id', None)
        if imdb_id:
            task = scrapyd.schedule('default', 'imdb_crawl', imdb_id = imdb_id)
            return Response({'task_id': task, 'status': 'started'})
    def get(self, request):
        task_id = request.query_params.get('task_id', None)
        imdb_id = request.query_params.get('imdb_id', None)
        if not task_id:
            return Response({"errors": ['Missing task ID']})
        status = scrapyd.job_status('default', task_id)
        if not status:
            return Response({'status': 'Wrong id'})
        if status == 'finished':
            try:
                item = models.Films.objects.get(imdb_id = str(imdb_id))
                serializer = kserializers.FilmsSerializer(item)
                return Response({'data': serializer.data})
            except Exception as e:
                return Response({'error': str(e)})
        else:
                return Response({'status': status})
