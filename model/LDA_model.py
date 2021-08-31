# coding:utf8

"""
@author: Zhangao Lu
@contact:
@time: 2021/8/7
@description:
LDA
"""

import gensim
from gensim.corpora import Dictionary

from config import config
from config.config import LDA_para
from utils.gerenal_tools import open_pickle, save_pickle
from data.preprocessing import DataPreProcessing


dpp = DataPreProcessing()


def train_LDA(pre_processing_path, lda_path, dictionary_path):
    """
    :param pre_processing_path: string
          the path of the pre-processing data
    :param lda_path: string
           the path of the LDA model
    :param dictionary_path: string
           the path of the dictionary
    :return: None
    """
    docs = open_pickle(pre_processing_path)

    # docs = docs[: 100]
    dictionary = Dictionary(docs)
    save_pickle(dictionary, dictionary_path)
    corpus = [dictionary.doc2bow(doc) for doc in docs]
    print(corpus)

    lda = gensim.models.LdaModel(corpus=corpus,
                                 id2word=dictionary,
                                 num_topics=LDA_para["num_topics"],
                                 iterations=LDA_para["iterations"],
                                 )
    save_pickle(lda, lda_path)

# TODO optimize the model by using Compute Coherence Score or Compute Perplexity


class LDA(object):
    def __init__(self, lda_path, dictionary_path):
        """
        use the model to predict documents
        :param lda_path: string
               the path of the LDA model
        :param dictionary_path: string
               the path of the dictionary
        """
        self.dictionary = open_pickle(dictionary_path)
        self.lda = open_pickle(lda_path)
        self.topics = dict()
        for elem in self.lda.print_topics():
            self.topics[elem[0]] = elem[1]

    def get_the_topic_from_single_file(self, words):
        """

        :param words: list
               e.g. ["tree", "apple", "boy"]
        :return: topics list
        """
        topics = list()
        other_corpus = self.dictionary.doc2bow(words)
        doc_topics, word_topics, phi_values = self.lda.get_document_topics(other_corpus, per_word_topics=True)
        for elem in doc_topics:
            # print(self.topics[elem[0]], elem[1])
            # e.g. 0.019*"enron" + 0.005*"agreement" + 0.005*"subject" + 0.005*"need" + 0.005*"know" + 0.004*"mark" +
            # 0.004*"market" + 0.004*"business" + 0.004*"work" + 0.004*"change" 0.45153937
            topics.append(self.topics[elem[0]])
        return topics


if __name__ == '__main__':
    train_LDA(config.pre_processing_path, config.LDA_model_path, config.dictionary_path)

