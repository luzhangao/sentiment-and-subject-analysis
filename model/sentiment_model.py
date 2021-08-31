# coding:utf8

"""
@author: Zhangao Lu
@contact:
@time: 2021/8/7
@description:
Sentiment analysis
"""

from textblob import TextBlob
from config import config
from utils.gerenal_tools import open_pickle
from data.preprocessing import DataPreProcessing


dpp = DataPreProcessing()


def sentiment_all(pre_processing_path):
    """
    Test all emails
    :param pre_processing_path: string
          the path of the pre-processing data
    :return:
    """
    pre_processing = open_pickle(pre_processing_path)
    for stream in pre_processing:
        print(sentiment_one(stream))


def sentiment_one(stream):
    """
    get the sentiment score for string stream
    :param stream: string
    :return: res: dict
    """
    testimonial = TextBlob(stream)
    res = {"polarity": testimonial.sentiment.polarity, "subjectivity": testimonial.sentiment.subjectivity}
    return res


if __name__ == '__main__':
    sentiment_all(config.pre_processing_path)
