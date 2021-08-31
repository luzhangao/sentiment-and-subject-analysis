# coding:utf8

"""
@author: Zhangao Lu
@contact:
@time: 2021/8/7
@description:
"""

from data.preprocessing import DataPreProcessing
from model.sentiment_model import sentiment_one
from model.LDA_model import LDA
from config import config


dpp = DataPreProcessing()
lda = LDA(config.LDA_model_path, config.dictionary_path)


def format_service_api_response(res):
    """
    format the API response
    :param res: dict
    :return: response: dict
    """
    # TODO try catch, add response if there are some errors
    response = {"status": "200", "error_code": -1, "res": res}
    return response


def check_sentiment_score(require_text):
    """

    :param require_text: string
           raw text
    :return: res, dict
    """
    words = dpp.run(require_text)  # text pre-processing
    # print(words)
    res = sentiment_one(" ".join(words))
    return res


def check_topic(require_text):
    """

    :param require_text: string
           raw text
    :return: res, dict
    """
    need_topics = ["oil", "gas"]
    words = dpp.run(require_text)  # text pre-processing
    lda_topics = lda.get_the_topic_from_single_file(words)  # e.g. ["'0.016*"price" + 0.009*"power"", ...]
    all_topics = " ".join(lda_topics)
    res = dict()
    for topic in need_topics:
        if topic in all_topics:
            res[topic] = "true"
        else:
            res[topic] = "false"
    return res


if __name__ == '__main__':
    pass
