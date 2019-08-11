# -*- coding: utf-8 -*-
from configparser import ConfigParser

import os

import logging


def limit(num):
    return slimit(num)


def slimit(num):
    return int(num * LIMIT_TAGS_MATCH + 0.5)


def llimit(num):
    return int(num * LIMIT_TAGS_MATCH)


PATH_MODULE = os.path.dirname(__file__) + "/../"
PATH_DATA = PATH_MODULE + "data/"

CONFIG_FILE = PATH_MODULE + "ChatBot.cfg"
if os.path.exists(CONFIG_FILE):
    logging.info("load %s" % os.path.abspath(CONFIG_FILE))
    config = ConfigParser()
    config.read(CONFIG_FILE)
    PATH_FQA = PATH_DATA + config.get("CUSTOM", "PATH_FQA")
    INDEX = config.get("CUSTOM", "INDEX")
    QA_TYPE = config.get("CUSTOM", "QA_TYPE")
    PATH_RELATED_DIC = PATH_DATA + config.get("CUSTOM", "PATH_RELATED_DIC")
    LIMIT_TAGS_MATCH = config.getfloat("CUSTOM", "LIMIT_TAGS_MATCH")
    TULING_API_KEY = config.get("CUSTOM", "TULING_API_KEY")
    WECHAT_TOKEN = config.get("CUSTOM", "WECHAT_TOKEN")
    WECHAT_APP_ID = config.get("CUSTOM", "WECHAT_APP_ID")
    WECHAT_APP_SECRET = config.get("CUSTOM", "WECHAT_APP_SECRET")
    WECHAT_ENCODING_AES_KEY = config.get("CUSTOM", "WECHAT_ENCODING_AES_KEY")
    TXT_NO_ANSWER = config.get("CUSTOM", "TXT_NO_ANSWER")
    TXT_MEANINGLESS_ANSWER = config.get("CUSTOM", "TXT_MEANINGLESS_ANSWER")
else:
    logging.error("%s exist" % os.path.abspath(CONFIG_FILE))
