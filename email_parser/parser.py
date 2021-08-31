# coding:utf8

"""
@author: Zhangao Lu
@contact:
@time: 2021/8/7
@description:
parser emails and save
"""

import os
import email
from email.feedparser import FeedParser
from config import config
from utils.gerenal_tools import open_text, save_pickle


def parser_all(data_set_path):
    """
    parser all files from the data set and save them into hard disk
    :param data_set_path: string
    :return: None
    """
    res = list()
    cnt = 0
    # Traverse a directory
    for dir_path, dir_names, file_names in os.walk(data_set_path):
        if file_names:
            # print(dir_path, dir_names, file_names)  # e.g. C:\Users\xxx\all_documents [] ['100_', '101_', ... ]
            for each_file in file_names:
                print(cnt, dir_path, each_file)
                cnt += 1
                email_path = dir_path + "\\" + each_file
                res.append(parser_string(open_text(email_path, encoding="ISO-8859-1")))
    print(res[: 2])
    save_pickle(res, config.email_raw)


def parser_string(stream):
    """
    parser one email from string stream
    :param stream: string
           The string stream of the email
    :return: body: string
             The body of the email
    """
    msg = email.message_from_string(stream)
    body = ""
    if msg.is_multipart():
        for payload in msg.get_payload():
            body += payload.get_payload()
    else:
        body = msg.get_payload()

    return body


if __name__ == '__main__':
    parser_all(config.email_data_set)
