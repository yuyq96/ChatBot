# -*- coding: utf-8 -*-
import logging

from abc import abstractmethod

from chatbot.bot.abstract import Bot


class Service:

    def __init__(self):
        self.running = False
        self.bot = None

    def set_bot(self, bot):
        if isinstance(bot, Bot):
            self.bot = bot
            return self
        else:
            logging.error("%s is not a Bot" % str(bot))
            return None

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
        return self

    def set_voice_handler(self, handler):
        self.voice_handler = handler
        return self

    def set_image_handler(self, handler):
        self.image_handler = handler
        return self

    def set_video_handler(self, handler):
        self.video_handler = handler
        return self

    def handle_text(self, msg):
        if self.text_handler:
            return self.text_handler(self.bot, msg)
        elif self.bot:
            return self.bot.answer(msg['FromUserName'], msg['Content'])

    def handle_voice(self, msg):
        if self.voice_handler:
            return self.voice_handler(self.bot, msg)
        elif self.bot:
            pass

    def handle_image(self, msg):
        if self.image_handler:
            return self.image_handler(self.bot, msg)
        elif self.bot:
            pass

    def handle_video(self, msg):
        if self.video_handler:
            return self.video_handler(self.bot, msg)
        elif self.bot:
            pass
