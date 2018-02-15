# -*- coding: utf-8 -*-
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
        json = {
            "key": TULING_API_KEY,
            "userid": uid,
            "info": question
        }
        r = requests.get(Bot.URL, params=json)
        return r.text
