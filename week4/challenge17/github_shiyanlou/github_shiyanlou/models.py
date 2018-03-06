from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import DateTime

engine = create_engine(
    'mysql://root:@localhost/shiyanlou?charset=utf8')
Base = declarative_base()


class Repository(Base):
    __tablename__ = 'github'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    update_time = Column(DateTime)
    commits = Column(Integer)
    branches = Column(Integer)
    releases = Column(Integer)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
