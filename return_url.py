# -*- coding:utf-8 -*-
from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    url1 = (url_for('news', id='10086'))
    return "URL反转内容为:{}".format(url1)


@app.route('/news/<id>')
def news(id):
    return u'您请求的参数是: {}'.format(id)


if __name__ == "__main__":
    app.run()
