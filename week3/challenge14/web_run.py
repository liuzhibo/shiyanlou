# -*- coding: UTF-8 -*-

from flask import request
from flask import Flask
from flask import render_template
from ele import ele_red_packet


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    phone_number = request.form.get('phone')
    print(phone_number)
    get_red_packet = ele_red_packet(phone_number)
    print(get_red_packet)
    # return render_template('index.html')
    return render_template('index.html', phone_number=get_red_packet)


if __name__ == '__main__':
    app.run()
