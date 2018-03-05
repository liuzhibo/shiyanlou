# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import UserItem


class UsersSpider(scrapy.Spider):
    name = 'users'
    # allowed_domains = ['shiyanlou.com']
    start_urls = ['']

    @property
    def start_urls(self):
        """ 实验楼注册的用户数目前大约50几万，为了
        爬虫的效率，取 id 在 524,800~525,000 之间的
        新用户，每间隔 10 取一个，最后大概爬取 20 个
        用户的数据
        """
        return ('https://www.shiyanlou.com/user/{}/'.format(i) for i in range(1, 550000))

    def parse(self, response):
        yield UserItem({
            'user_id': response.url[31:-1],
            'name': response.css('span.username::text').extract_first(),
            'type': response.css('a.member-icon img.user-icon::attr(title)').extract_first(default='普通用户'),
            'status': response.xpath('//div[@class="userinfo-banner-status"]/span[1]/text()').extract_first(),
            'job': response.xpath('//div[@class="userinfo-banner-status"]/span[2]/text()').extract_first(),
            'school': response.xpath('//div[@class="userinfo-banner-status"]/a/text()').extract_first(),
            'join_date': response.css('span.join-date::text').extract_first(),
            'level': response.css('span.user-level::text').extract_first(),
            'learn_courses_num': response.css('span.latest-learn-num::text').extract_first()
        })
