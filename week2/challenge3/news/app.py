# -*- coding: utf-8 -*-
#!/usr/bin.env python3

from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from datetime import datetime

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'liuzhibo',
    'host': '127.0.0.1',
    'port': 27017
}

db = MongoEngine(app)


class Files(db.Document):
    meta = {
        'collection': 'files',
        'ordering': ['-create_at'],
        'strict': False,
    }
    file_id = db.IntField()
    title = db.StringField()
    category = db.IntField()
    tag = db.ListField()
    content = db.StringField()
    create_time = db.DateTimeField(default=datetime.now)


class Category(db.Document):
    meta = {
        'collection': 'category',
        'ordering': ['-create_at'],
        'strict': False,
    }

    cid = db.IntField()
    category = db.StringField()


class Tag(db.Document):
    meta = {
        'collection': 'tag',
        'ordering': ['-create_at'],
        'strict': False,
    }

    tid = db.IntField()
    tag = db.StringField()


@app.route('/', methods=['GET'])
def index():
    files = Files.objects().all()
    tlist = []
    flist = []
    for f in files:
        for t in f['tag']:
            tlist.append(Tag.objects(tid=t)[0]['tag'])
        flist.append([f, tlist, Category.objects(
            cid=f['category'])[0]['category']])
        tlist = []
    # print(flist)
    return render_template('index.html', files=flist)


@app.route('/file/<int:file_id>')
def file(file_id):
    files = Files.objects(file_id=file_id)
    return render_template('file.html', files=files[0])


@app.route('/add')
def add():
    f1 = Files(file_id=1, title='HI first !', category=1,
               tag=[1], content='first content')
    f2 = Files(file_id=2, title='HI second !', category=2,
               tag=[2], content='second content')
    f3 = Files(file_id=3, title='HI third !', category=2,
               tag=[1, 2], content='third content')
    c1 = Category(cid=1, category='category_1')
    c2 = Category(cid=2, category='category_2')
    t1 = Tag(tid=1, tag='tag_1')
    t2 = Tag(tid=2, tag='tag_2')

    f1.save()
    f2.save()
    f3.save()
    c1.save()
    c2.save()
    t1.save()
    t2.save()

    return "<p>add succssfully! <a href='/'>Home</a></p>"


if __name__ == "__main__":
    app.run()
