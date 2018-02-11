from flask import Flask, render_template, abort

import json


class getJsonfromFile:
    def _getjson(self, path):
        with open(path) as f:
            _json = json.loads(f.read())
        return _json

    @property
    def getshiyanlou(self):
        return self._getjson('/Users/liuzhibo/Code/python/shiyanlou/week2/challenge1/files/helloshiyanlou.json')

    @property
    def gethelloworld(self):
        return self._getjson('/Users/liuzhibo/Code/python/shiyanlou/week2/challenge1/files/helloworld.json')


gJ = getJsonfromFile()
app = Flask(__name__)


@app.route('/')
def index():
    data = {'helloshiyanlou': '/files/helloshiyanlou',
            'helloworld': '/files/helloworld'}
    return render_template('index.html', data=data)


@app.route('/files/<filename>')
def file(filename):
    if filename == 'helloshiyanlou':
        data = gJ.getshiyanlou
    elif filename == 'helloworld':
        data = gJ.gethelloworld
    else:
        abort(404)
    return render_template('file.html', data=data)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
