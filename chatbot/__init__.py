# -*- coding: utf-8 -*-
from .settings import *


class ChatBot:

    def __init__(self):
        self.bots = dict()
        self.services = dict()

    def add_bot(self, name):
        name = name.lower()
        assert name in ['elastic', 'tuling']
        if self.bots.get(name) is None:
            if name == 'elastic':
                from .bot import elastic
                bot = elastic.Bot()
            else:
                from .bot import tuling
                bot = tuling.Bot()
            self.bots[name] = bot
        return bot

    def list_bot(self):
        return self.bots.keys()

    def get_bot(self, name):
        name = name.lower()
        bot = self.bots.get(name)
        if not bot:
            logging.error(f'Bot {name} not exist')
        return bot

    def init(self, name):
        bot = self.get_bot(name)
        if bot:
            bot.init()

    def answer(self, uid, question):
        for name, bot in self.bots.items():
            logging.info(f'Answering with {name} bot')
            answer = bot.answer(uid, question)
            if answer != TXT_NO_ANSWER and answer != TXT_MEANINGLESS_ANSWER:
                return answer

    def add_service(self, name):
        name = name.lower()
        assert name in ['http', 'wechat', 'wechatmp']
        if name == 'http':
            from .util.service.http import Http
            service = Http()
        elif name == 'wechat':
            from .util.service.wechat import wechat
            service = wechat
        else:
            from .util.service.wechatmp import wechatmp
            service = wechatmp
        self.services[name] = service
        return service

    def list_service(self):
        return self.services.keys()

    def get_service(self, name):
        name = name.lower()
        service = self.services.get(name)
        if not service:
            logging.error(f'Service {name} not exist')
        return service

    def start(self, name):
        service = self.get_service(name)
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
