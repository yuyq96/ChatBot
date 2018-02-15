# -*- coding: utf-8 -*-
import json
import requests

from .abstract import Bot as AbstractBot
from ..settings import *


class Bot(AbstractBot):

    URL = 'http://www.tuling123.com/openapi/api'

    def __init__(self):
        pass

    def init(self):
        pass

    def answer(self, uid, question):
        params = {
            "key": TULING_API_KEY,
            "userid": uid,
            "info": question
        }
        r = requests.get(Bot.URL, params=params)
        return json.loads(r.text)["text"]
