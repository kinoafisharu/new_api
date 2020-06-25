from django.core import exceptions
import logging
from base.parsing import parsers
from bs4 import BeautifulSoup
import requests as req


# В данном файле хранятся классы - парсеры


# Парсит фильм по его ID на IMDB
class ImdbParser(parsers.BaseParser):
    def __init__(self, *args, **kwargs):
        self.imdb_id = kwargs.pop('imdb_id')
        super().__init__(*args, **kwargs)

    def parse_rating(self, site):
        div_rating = site.find('div', {'class': 'ratingValue'})
        strong_rating = div_rating.find('strong')
        strong_rating.span.decompose()
        rating_text = strong_rating.attrs['title'][:4].strip()
        return float(rating_text)

    def parse_votes(self, site):
        div_rating = site.find('span', {'class': 'small', 'itemprop': 'ratingCount'})
        votes = div_rating.get_text().replace(',','')
        return int(votes)

    def parse_title(self, site):
        div_title = site.find('div', {'class': 'title_wrapper'})
        h1_title = div_title.find('h1')
        h1_title.span.decompose()
        title_text = h1_title.get_text().strip()
        return [{'name': title_text, 'status': 1}]

    def parse(self):
        site = self.get_parser()
        self.item['name'] = self.parse_title(site)
        self.item['imdb_id'] = self.imdb_id
        self.item['imdb_votes'] = self.parse_votes(site)
        self.item['imdb_rate'] = self.parse_rating(site)
        return self.item

class KinoinfoParser(parsers.BaseParser):

    def parse_poster(self, site):
        div_poster = site.find('div', {'id': 'poster'})
        src = div_poster.img['src']
        return src

    def parse(self):
        site = self.get_parser()
        self.item['poster'] = self.parse_poster(site)
        return self.item
