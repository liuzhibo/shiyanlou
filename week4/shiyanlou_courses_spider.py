# -*- coding:utf-8 -*-
import scrapy
# scrapy runspider shiyanlou_courses_spider.py - o data.xml


class ShiyanlouCoursesSpider(scrapy.Spider):
    """ 所有 scrapy 爬虫需要写一个 Spider 类，这个类要继承 scrapy.Spider 类。在这个类中定义要请求的网站和链接、如何从返回的网页提取数据等等。
    """

    # 爬虫标识符号，在 scrapy 项目中可能会有多个爬虫，name 用于标识每个爬虫，不能相同
    name = 'shiyanlou-courses'

    def start_requests(self):
        """ 需要返回一个可迭代的对象，迭代的元素是 `scrapy.Request` 对象，可迭代对象可以是一个列表或者迭代器，这样 scrapy 就知道有哪些网页需要爬取了。`scrapy.Request`
         接受一个 url 参数和一个 callback 参数，url 指明要爬取的网页，callback 是一个回调函数用于处理返回的网页，通常是一个提取数据的 parse 函数。
        """
        # 课程列表页面 url 模版
        url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
        # 所有要爬取的页面
        urls = (url_tmpl.format(i) for i in range(1, 23))
        # 返回一个生成器，生成 Request 对象，生成器是可迭代对象
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """ 这个方法作为 `scrapy.Request` 的 callback，在里面编写提取数据的代码。scrapy 中的下载器会下载 `start_reqeusts` 中定义的每个 `Request` 并且结果封装为一个 response 对象传入这个方法。
        """
        # 遍历每个课程的 div.course-body
        for course in response.css('div.course-body'):
            # 使用 css 语法对每个 course 提取数据
            yield {
                # 课程名称
                'name': course.css('div.course-name::text').extract_first(),
                # 课程描述
                'description': course.css('div.course-desc::text').extract_first(),
                # 课程类型，实验楼的课程有免费，会员，训练营三种，免费课程并没有字样显示，也就是说没有 span.pull-right 这个标签，没有这个标签就代表时免费课程，使用默认值 `免费｀就可以了。
                'type': course.css('div.course-footer span.pull-right::text').extract_first(default='Free'),
                # 注意 // 前面的 .，没有点表示整个文档所有的 div.course-body，有 . 才表示当前迭代的这个 div.course-body
                'students': course.xpath('.//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d+)[^\d]*')
            }
