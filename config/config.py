# coding:utf8

"""
@author: Zhangao Lu
@contact:
@time: 2021/8/7
@description:
config file
"""

# path of email files
email_data_set = r"C:\Users\luzha\Downloads\enron_mail_20150507.tar\maildir"

# raw data
email_raw = "../data/raw.pkl"
email_raw_sample = "../data/raw sample.pkl"

# pre-processing data
pre_processing_path = "../data/pre_processing.pkl"

# TODO
customize_stop_words = [
    "forwarded",
]

# LDA parameters
LDA_para = {
    "num_topics": 20,
    "chunksize": 2000,
    "passes": 20,
    "iterations": 400,
    "eval_every": None
}

# path of the trained LDA model
dictionary_path = "../data/models/dictionary.pkl"
LDA_model_path = "../data/models/LDA.pkl"


if __name__ == '__main__':
    pass
