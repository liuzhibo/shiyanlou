# -*- coding: utf-8 -*-
import scrapy


class CoursesSpider(scrapy.Spider):
    name = 'courses'
    allowed_domains = ['shiyanlou.com']
    start_urls = ['http://shiyanlou.com/']

    def parse(self, response):
        pass
