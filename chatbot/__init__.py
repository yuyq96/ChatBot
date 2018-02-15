# -*- coding: utf-8 -*-
from .bot import elastic
from .bot import tuling
from .settings import *
from .util.service.http import Http
from .util.service.wechat import wechat
from .util.service.wechatmp import wechatmp


class ChatBot:

    def __init__(self):
        self.bots = dict()
        self.services = dict()

    def add_bot(self, name):
        if name.lower() == "elastic":
            self.bots["elastic"] = elastic.Bot()
        elif name.lower() == "tuling":
            self.bots["tuling"] = tuling.Bot()
        return self

    def list_bot(self):
        return self.bots.keys()

    def get_bot(self, key):
        bot = self.bots.get(key)
        if not bot:
            logging.error("Bot %s not exist" % key)
        return bot

    def init(self, key):
        bot = self.get_bot(key)
        if bot:
            bot.init()

    def answer(self, uid, question):
        for _, bot in self.bots.items():
            answer = bot.answer(uid, question)
            if answer != TXT_NO_ANSWER and answer != TXT_MEANINGLESS_ANSWER:
                return answer

    def add_service(self, name):
        if name.lower() == "http":
            self.services["http"] = Http()
        elif name.lower() == "wechat":
            self.services["wechat"] = wechat
        elif name.lower() == "wechatmp":
            self.services["wechatmp"] = wechatmp
        return self

    def list_service(self):
        return self.services.keys()

    def get_service(self, key):
        service = self.services.get(key)
        if not service:
            logging.error("Service %s not exist" % key)
        return service

    def start(self, key):
        service = self.get_service(key)
        if service:
            service.start()

    def stop(self, key):
        service = self.get_service(key)
        if service:
            service.stop()

    def start_all(self):
        for _, service in self.services.items():
            service.start()

    def stop_all(self):
        for _, service in self.services.items():
            service.stop()
