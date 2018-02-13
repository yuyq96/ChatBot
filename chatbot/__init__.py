# -*- coding: utf-8 -*-
from .bot import elastic
from .util.service.http import Http
from .util.service.wechat import wechat
from .util.service.wechatmp import wechatmp


class ChatBot:

    def __init__(self, name="elastic"):
        if name.lower() == "elastic":
            self.bot = elastic.Bot()

    def get(self):
        return self.bot

    def reload(self):
        if isinstance(self.bot, elastic.Bot):
            self.bot.init_elastic()

    def service(self, name):
        if name.lower() == "http":
            return Http(self.bot)
        elif name.lower() == "wechat":
            return wechat.set_bot(self.bot)
        elif name.lower() == "wechatmp":
            return wechatmp.set_bot(self.bot)
