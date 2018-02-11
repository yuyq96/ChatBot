# -*- coding: utf-8 -*-
import logging

import itchat

from .abstract import Service
from chatbot.bot.abstract import Bot


class Wechat(Service):
    def __init__(self, bot):
        self.running = False
        if isinstance(bot, Bot):
            self.bot = bot
        else:
            self.bot = None
            logging.error("%s is not a Bot" % str(bot))

    def bot(self, bot):
        if isinstance(bot, Bot):
            self.bot = bot
            return True
        else:
            return False

    @itchat.msg_register(itchat.content.TEXT)
    def _reply(self, msg):
        if self.bot:
            return self.bot.answer(msg.text)

    def start(self):
        if self.bot:
            itchat.auto_login(hotReload=False, enableCmdQR=False)
            itchat.run()
            self.running = True

    def stop(self):
        if not self.running:
            self.running = False
            itchat.logout()
