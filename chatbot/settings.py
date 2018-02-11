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

CONFIG_FILE = PATH_MODULE + "ChatBot.cfg"
print(os.path.abspath(CONFIG_FILE))
if os.path.exists(CONFIG_FILE):
    config = ConfigParser()
    config.read(CONFIG_FILE)
    # elastic
    PATH_FQA = PATH_DATA + config.get("CUSTOM", "PATH_FQA")
    PATH_RELATED_DIC = PATH_DATA + config.get("CUSTOM", "PATH_RELATED_DIC")
    TXT_NO_ANSWER = config.get("CUSTOM", "TXT_NO_ANSWER")
    TXT_MEANINGLESS_ANSWER = config.get("CUSTOM", "TXT_MEANINGLESS_ANSWER")
    LIMIT_TAGS_MATCH = config.getfloat("CUSTOM", "LIMIT_TAGS_MATCH")
    # http
    TOKEN_WECHAT = config.get("CUSTOM", "TOKEN_WECHAT")
