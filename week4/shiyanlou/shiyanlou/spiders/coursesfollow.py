# -*- coding: utf-8 -*-
import scrapy


class CoursesfollowSpider(scrapy.Spider):
    name = 'coursesfollow'
    # allowed_domains = ['shiyanlou.com']
    start_urls = ['https://shiyanlou.com/courses/63']

    def parse(self, response):
        pass
