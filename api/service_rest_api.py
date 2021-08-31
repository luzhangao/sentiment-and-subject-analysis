# coding:utf8

"""
@author: Zhangao Lu
@contact:
@time: 2021/8/7
@description:
"""

from flask import Flask

from api.interface_functions import *
from utils.decorator_tools import response_json

app = Flask(__name__)


@app.route("/")
@response_json
def hello():
    """
    first API
    :return:
    """
    return api_hello()


@app.route('/models/sentiment')
@response_json
def sentiment():
    """
    :return:
    """
    return get_sentiment()


@app.route('/models/topic')
@response_json
def topic():
    """
    :return:
    """
    return get_topic()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000, debug=True)

