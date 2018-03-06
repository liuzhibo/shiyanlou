import scrapy


class CoursesFollowSpider(scrapy.Spider):
    name = 'courses_follow'
    start_urls = ['https://shiyanlou.com/courses/63']

    def parse(self, response):
        yield {
            'name': response.xpath('//h4[@class="course-infobox-title"]/span/text()').extract_first(),
            'author': response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()
        }
        # 不需要 extract 了
        for url in response.xpath('//div[@class="sidebox-body course-content"]/a/@href'):
            # 不需要构造全 url 了
            yield response.follow(url, callback=self.parse)


# scrapy runspider coursesfollow.py - o data.json
