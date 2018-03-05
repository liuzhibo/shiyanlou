from datetime import datetime
from sqlalchemy.orm import sessionmaker
from shiyanlou.models import Course, User, engine
from shiyanlou.items import CourseItem, UserItem
from scrapy.exceptions import DropItem


class ShiyanlouPipeline(object):

    def process_item(self, item, spider):
        """ 对不同的 item 使用不同的处理函数
        """
        if isinstance(item, CourseItem):
            self._process_course_item(item)
        else:
            self._process_user_item(item)
        return item

    def _process_course_item(self, item):
        item['students'] = int(item['students'])
        self.session.add(Course(**item))

    def _process_user_item(self, item):
        # 抓取到的数据类似 'L100'，需要去掉 'L' 然后转化为 int
        item['level'] = int(item['level'][1:])
        if item['level'] < 100:
            raise DropItem('level less than 100.')
        item['user_id'] = int(item['user_id'])
        # 抓去到的数据类似 '2017-01-01 加入实验楼'
        # 其中的把日期字符串转换为 date 对象
        item['join_date'] = datetime.strptime(
            item['join_date'].split()[0], '%Y-%m-%d').date()
        # 学习课程数目转化为 int
        item['learn_courses_num'] = int(item['learn_courses_num'])
        # 添加到 session
        self.session.add(User(**item))

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()


'''
    def process_item(self, item, spider):
        # 提取的学习人数是字符串，把它转换成 int
        item['students'] = int(item['students'])
        # 根据 item 创建 Course Model 对象并添加到 session
        # item 可以当成字典来用，所以也可以使用字典解构, 相当于
        # Course(
        #     name=item['name'],
        #     type=item['type'],
        #     ...,
        # )
        # if item['students'] < 1000:
        #     # 对于不需要的 item，raise DropItem 异常
        #     raise DropItem('Course students less than 1000.')
        # else:
        #     self.session.add(Course(**item))

        self.session.add(Course(**item))
        return item

    def open_spider(self, spider):
        """ 在爬虫被开启的时候，创建数据库 session
        """
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        """ 爬虫关闭后，提交 session 然后关闭 session
        """
        self.session.commit()
        self.session.close()
'''
