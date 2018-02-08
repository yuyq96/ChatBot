# -*- coding: utf-8 -*-
from configparser import ConfigParser

import os

CONFIG_FILE = "QABot.cfg"
if os.path.exists(CONFIG_FILE):
    config = ConfigParser()
    config.read(CONFIG_FILE)
    PATH_FQA = config.get("CUSTOM", "PATH_FQA")
    PATH_RELATED_DIC = config.get("CUSTOM", "PATH_RELATED_DIC")
    TXT_NO_ANSWER = config.get("CUSTOM", "TXT_NO_ANSWER")
    # FQA_PATH = config.get("faq_path", "custom")
    # RELATED_DICT_PATH = config.get("related_dictionary_path", "custom")
    # TXT_NO_ANSWER = config.get("txt_no_answer", "custom")
