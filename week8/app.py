from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='very secret key',
    SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root:Aa111111@localhost:3306/simpledu?charset=utf8'
))


db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True,
                         index=True, nullable=False)
    publish_courses = db.relationship('Course')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Course(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, index=True, nullable=False)
    # ondelete='CASCADE' 表示如果用户被删除了，那么作者为他的
    # 课程也会被及联删除
    author_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'))
    author = db.relationship('User', uselist=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


@app.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)


@app.route('/admin')
def admin_index():
    return 'admin'


if __name__ == '__main__':
    app.run()
