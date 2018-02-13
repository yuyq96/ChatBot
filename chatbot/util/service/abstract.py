# -*- coding: utf-8 -*-
import logging

from abc import abstractmethod

from chatbot.bot.abstract import Bot


class Service:

    def __init__(self, bot):
        self.running = False
        self.bot = None
        self.bot(bot)

    def bot(self, bot):
        if isinstance(bot, Bot):
            self.bot = bot
            return True
        else:
            logging.error("%s is not a Bot" % str(bot))
            return False

    def start(self):
        if self.bot:
            self._start()
            self.running = True
            logging.error("Service started")

    def stop(self):
        if not self.running:
            self._stop()
            self.running = False
            logging.error("Service stopped")

    @abstractmethod
    def _start(self): pass

    @abstractmethod
    def _stop(self): pass


class WechatService(Service):

    @abstractmethod
    def _start(self):
        pass

    @abstractmethod
    def _stop(self):
        pass

    text_handler = None
    voice_handler = None
    image_handler = None
    video_handler = None

    def set_text_handler(self, handler):
        self.text_handler = handler

    def set_voice_handler(self, handler):
        self.voice_handler = handler

    def set_image_handler(self, handler):
        self.image_handler = handler

    def set_video_handler(self, handler):
        self.video_handler = handler

    def handle_text(self, msg):
        if self.text_handler:
            return self.text_handler(msg)
        elif self.bot:
            return self.bot.answer(msg.text)

    def handle_voice(self, msg):
        if self.voice_handler:
            return self.voice_handler(msg)
        elif self.bot:
            pass

    def handle_image(self, msg):
        if self.image_handler:
            return self.image_handler(msg)
        elif self.bot:
            pass

    def handle_video(self, msg):
        if self.video_handler:
            return self.video_handler(msg)
        elif self.bot:
            pass
