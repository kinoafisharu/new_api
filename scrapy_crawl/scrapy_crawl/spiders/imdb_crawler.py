# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule, Spider


class ImdbSpider(Spider):
    name = 'imdb_crawl'

    def __init__(self, *args, **kwargs):
        # We are going to pass these args from our django view.
        # To make everything dynamic, we need to override them inside __init__ method
        self.imdb_id = kwargs.get('imdb_id')
        print(str(self.imdb_id))
        url = 'https://www.imdb.com/title/tt{0}/'.format(self.imdb_id)
        self.start_urls = [url]
        print(url)
        self.allowed_domains = ['imdb.com']

        super(ImdbSpider, self).__init__(*args, **kwargs)

    def __get_title(self, response):
        title = response.css('.title_wrapper > h1::text').get()
        return title.strip() if title else ''

    def parse(self, response):
        title = self.__get_title(response)
        i = {}
        i['title'] = title
        i['imdb_id'] = self.imdb_id
        print(i)
        return i
