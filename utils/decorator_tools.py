# coding:utf8

"""
@author: Zhangao Lu
@contact:
@time: 2021/8/7
@description:
"""


import json
from functools import wraps
from flask import Response


def response_json(func):
    """
    Decorator: return JSON
    Content-Type=application/json
    charset=utf-8
    :param func: function
    :return:
    """

    @wraps(func)
    def set_response(*args, **kwargs):
        res = func(*args, **kwargs)
        if type(res) is not dict:
            return res
        else:
            return Response(json.dumps(res), content_type="application/json; charset=utf-8")
    return set_response


if __name__ == '__main__':
    pass
