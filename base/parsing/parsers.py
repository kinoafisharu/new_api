from django.core import exceptions
import logging
from bs4 import BeautifulSoup
import requests as req
from urllib3.exceptions import HTTPError


# Здесь описаны базовые классы для парсинга


# Базовый метакласс для парсинга
# Служит хранилищем необходимого функционала для любого дочернего парсера
class BaseParser():
    def __init__(self, *args, **kwargs):
        cparser = kwargs.pop('parser', None)
        self.item = dict()
        self.relations = dict()
        self.url = kwargs.pop('url', None)
        self.fields = kwargs.pop('fields', None)
        self.extra = kwargs.pop('extra', None)
        self.parser = cparser if cparser else self.default_parser

    # Хранение данных в парсере в виде параметра
    @property
    def data(self):
        if not hasattr(self, 'item'):
            msg = (
                'Parsed item is empty or incorrectly overriden'
            )
            raise AssertionError(msg)
        return self.item


    # Выаолнить http запрос по заданному url, если такого нет - ошибка
    def fetch_data(self, url):
        if url:
            site = req.get(url)
            if site.status_code != 200:
                raise HTTPError(f'Request error with status code {site.status_code}')
            return site
        raise ValueError('URL must be present')

    # Получить обьект beautifulsoup с заданным парсером и полученным документом
    def get_parser(self):
        if not self.parser:
            raise ValueError('Parser must be present set default parser or use custom as arg')
        parsable = self.fetch_data(self.url)
        soup = BeautifulSoup(parsable.text, self.parser)
        return soup

    # Получить функции парсинга, выполнить их
    def parse_fields(self, fields, site):
        for field in fields:
            method = getattr(self, 'parse_{0}'.format(field))
            result = method(site)
            if result:
                self.item[field] = result

    # Начать парсинг, положить обьект в параметр item и вернуть обьект нужной структуры
    def parse(self):
        fields = self.fields
        if not fields:
            fields = self.default_fields
        # Если есть доп данные для аннотации обьекта, добавить их в обьект
        if self.extra:
            self.item.update(self.extra)
        site = self.get_parser()
        self.parse_fields(fields, site)
        return self.item
