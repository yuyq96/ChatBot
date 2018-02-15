# -*- coding: utf-8 -*-
import logging

from abc import abstractmethod


class Service:

    def __init__(self):
        self.name = None
        self.running = False

    def start(self):
        self.running = True
        logging.info("%s service started" % self.name)
        self._start()

    def stop(self):
        if not self.running:
            self._stop()
            self.running = False
            logging.error("%s service stopped" % self.name)

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
            return self.text_handler(msg)
        return

    def handle_voice(self, msg):
        if self.voice_handler:
            return self.voice_handler(msg)
        return

    def handle_image(self, msg):
        if self.image_handler:
            return self.image_handler(msg)
        return

    def handle_video(self, msg):
        if self.video_handler:
            return self.video_handler(msg)
        return
