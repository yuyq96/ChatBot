# -*- coding: utf-8 -*-
import logging

from .bot import elastic


class QABot:
    def __init__(self, bot_type="elastic"):
        if bot_type == "elastic":
            self.bot = elastic.Bot()

    def get(self):
        return self.bot
