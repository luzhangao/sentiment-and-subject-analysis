# coding:utf8

"""
@author: Zhangao Lu
@contact:
@time: 2021/8/7
@description:
"""
from flask import request

from api.register_services import format_service_api_response, check_sentiment_score, check_topic


def api_hello():
    """
    :return:
    """
    return {"current_version": "V1.0.0"}


def get_sentiment():
    """
    :return:
    """
    require_args = ["Email"]
    require_text = request.args.get(require_args[0], "")
    return format_service_api_response(check_sentiment_score(require_text))


def get_topic():
    """
    :return:
    """
    require_args = ["Email"]
    require_text = request.args.get(require_args[0], "")
    return format_service_api_response(check_topic(require_text))






if __name__ == '__main__':
    pass
