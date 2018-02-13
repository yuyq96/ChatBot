# -*- coding: utf-8 -*-
import itchat

from .abstract import WechatService


class Wechat(WechatService):

    def _start(self):
        itchat.auto_login(hotReload=False, enableCmdQR=False)
        itchat.run()

    def _stop(self):
        itchat.logout()

    @itchat.msg_register(itchat.content.TEXT)
    def handle_text(self, msg):
        self._handle_text(msg)

    @itchat.msg_register(itchat.content.VOICE)
    def handle_voice(self, msg):
        self._handle_voice(msg)

    @itchat.msg_register(itchat.content.PICTURE)
    def handle_picture(self, msg):
        self._handle_image(msg)

    @itchat.msg_register(itchat.content.VIDEO)
    def handle_video(self, msg):
        self._handle_video(msg)
