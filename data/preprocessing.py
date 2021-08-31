# coding:utf8

"""
@author: Zhangao Lu
@contact:
@time: 2021/8/7
@description:
data pre-processing
"""

import re
import spacy
from config import config
from utils.gerenal_tools import open_pickle, save_pickle


class DataPreProcessing(object):
    def __init__(self):
        self.spacy_model = spacy.load("en_core_web_sm")
        self.sw_spacy = self.spacy_model.Defaults.stop_words

    @staticmethod
    def regex(stream):
        """
        handle the stream with regression expression
        :param stream: string
        :return: stream
        """
        # TODO add more rules
        # remove hyperlinks
        stream = re.sub(r"(http|www)\S+", "", stream, flags=re.MULTILINE)
        # remove email address
        stream = re.sub(r"[\S]+@[\S]+", "", stream, flags=re.MULTILINE)

        return stream

    @staticmethod
    def tokenizer(doc):
        """
        tokenizer
        :param doc: spacy object
        :return: words: list
        """

        words = [str(token) for token in doc if not token.is_punct]  # Remove punctuations
        words = [re.sub(r"[^A-Za-z@]", "", word) for word in words]  # Remove non words
        words = [word.lower() for word in words if len(word) >= 2]  # Remove empty and too short strings
        return words

    def remove_stop_words(self, words):
        """
        Remove stop words
        :param words: list
        :return: words: list
        """
        words = [word for word in words if word not in self.sw_spacy and word not in config.customize_stop_words]
        return words

    def lemmatization(self, words):
        """
        lemmatization
        :param words: list
        :return: words: list
        """
        words = self.spacy_model(" ".join(words))
        words = [str(word.lemma_) for word in words]
        return words

    def run(self, stream):
        """
        run pre-processing
        :param stream: string
        :return: words list
        """
        stream = self.regex(stream)
        doc = self.spacy_model(stream)
        words = self.tokenizer(doc)
        words = self.remove_stop_words(words)
        words = self.lemmatization(words)
        return words


def save_pre_processing_results(raw_path, pre_processing_path):
    """

    :param raw_path: string
           the path of raw.pkl
    :param pre_processing_path: string
           the path used to save the pre-processing data
    :return: None
    """
    dpp = DataPreProcessing()
    docs = list()
    raw = open_pickle(raw_path)
    cnt = 0
    for stream in raw:
        cnt += 1
        print(cnt)
        words = dpp.run(stream)
        docs.append(words)
    save_pickle(docs, pre_processing_path)


if __name__ == '__main__':
    save_pre_processing_results(config.email_raw_sample, config.pre_processing_path)


