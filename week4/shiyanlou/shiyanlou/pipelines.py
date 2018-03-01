from sqlalchemy.orm import sessionmaker
from shiyanlou.models import Course, engine


class ShiyanlouPipeline(object):

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
