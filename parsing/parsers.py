from django.core import exceptions
import logging
from datetime import datetime
from base.parsing import parsers
from bs4 import BeautifulSoup
import requests as req


# В данном файле хранятся классы - парсеры


# Парсит фильм по его ID на IMDB
class ImdbParser(parsers.BaseParser):

    default_fields = ['imdb_rate', 'imdb_votes', 'name']
    default_parser = 'lxml'


    def parse_imdb_rate(self, site):
        try:
            div_rating = site.find('div', {'class': 'ratingValue'})
            strong_rating = div_rating.find('strong')
            strong_rating.span.decompose()
            rating_text = strong_rating.attrs['title'][:4].strip()
            return float(rating_text)
        except Exception as e:
            print(e)

    def parse_imdb_votes(self, site):
        try:
            div_rating = site.find('span', {'class': 'small', 'itemprop': 'ratingCount'})
            votes = div_rating.get_text().replace(',','')
            return int(votes)
        except Exception as e:
            print(e)

    def parse_name(self, site):
        try:
            div_title = site.find('div', {'class': 'title_wrapper'})
            h1_title = div_title.find('h1')
            h1_title.span.decompose()
            title_text = h1_title.get_text().strip()
            return [{'name': title_text, 'status': 1}]
        except Exception as e:
            print(e)

class KinoinfoParser(parsers.BaseParser):

    default_fields = ['poster', 'release', 'name']
    default_parser = 'lxml'

    def parse_poster(self, site):
        try:
            div_poster = site.find('div', {'id': 'poster'})
            src = div_poster.img['src']
        except Exception as e:
            src = None
            print(str(e))
        return src

    def parse_release(self, site):
        release = site.find('span', text = 'дата релиза')
        try:
            release = release['title']
        except Exception as e:
            print(str(e))
            return None
        date = datetime.strptime(release, '%d %B %Y')
        release = datetime.strftime(date, '%Y %m %d').replace(' ', '-')
        print(release)
        return [{'release': release}]

    def parse_name(self, site):
        header = site.find('h2', {'id': 'film_name'})
        header.span.decompose()
        name = header.get_text().strip()
        return name
