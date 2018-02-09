# -*- coding: utf-8 -*-
from configparser import ConfigParser

import os


def limit(num):
    return slimit(num)


def slimit(num):
    return int(num * LIMIT_TAGS_MATCH + 0.5)


def llimit(num):
    return int(num * LIMIT_TAGS_MATCH)


PATH_MODULE = os.path.dirname(__file__) + "/../"
PATH_DATA = PATH_MODULE + "data/"

CONFIG_FILE = PATH_MODULE + "QABot.cfg"
print(os.path.abspath(CONFIG_FILE))
if os.path.exists(CONFIG_FILE):
    config = ConfigParser()
    config.read(CONFIG_FILE)
    PATH_FQA = PATH_DATA + config.get("CUSTOM", "PATH_FQA")
    PATH_RELATED_DIC = PATH_DATA + config.get("CUSTOM", "PATH_RELATED_DIC")
    TXT_NO_ANSWER = config.get("CUSTOM", "TXT_NO_ANSWER")
    TXT_MEANINGLESS_ANSWER = config.get("CUSTOM", "TXT_MEANINGLESS_ANSWER")
    LIMIT_TAGS_MATCH = config.getfloat("CUSTOM", "LIMIT_TAGS_MATCH")
    # FQA_PATH = config.get("faq_path", "custom")
    # RELATED_DICT_PATH = config.get("related_dictionary_path", "custom")
    # TXT_NO_ANSWER = config.get("txt_no_answer", "custom")
