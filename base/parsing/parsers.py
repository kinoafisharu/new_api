from django.core import exceptions
import logging
from bs4 import BeautifulSoup
import requests as req


# Здесь описаны базовые классы для парсинга


# Базовый метакласс для парсинга
# Служит хранилищем необходимого функционала для любого дочернего парсера
class BaseParser():
    def __init__(self, *args, **kwargs):
        self.item = dict()
        self.relations = dict()
        self.url = kwargs.pop('url', None)
        self.parser = kwargs.pop('parser', None)

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
            return site
        raise ValueError('URL must be present')

    # Получить обьект beautifulsoup с заданным парсером и полученным документом
    def get_parser(self):
        if not self.parser:
            raise ValueError('Parser must be present')
        parsable = self.fetch_data(self.url)
        soup = BeautifulSoup(parsable.text, self.parser)
        return soup

    # Начать парсинг, положить обьект в параметр item и вернуть обьект нужной структуры
    def parse(self):
        raise NotImplementedError('This function (parse) must be implemented')
