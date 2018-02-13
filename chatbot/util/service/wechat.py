# -*- coding: utf-8 -*-
import itchat

from .abstract import WechatService


class Wechat(WechatService):

    def _start(self):
        itchat.auto_login(hotReload=False, enableCmdQR=False)
        itchat.run()

    def _stop(self):
        itchat.logout()

    @staticmethod
    @itchat.msg_register(itchat.content.TEXT)
    def _handle_text(msg):
        return WechatService.handle_text(WechatService(super), msg)

    @staticmethod
    @itchat.msg_register(itchat.content.VOICE)
    def _handle_voice(msg):
        return WechatService.handle_voice(WechatService(super), msg)

    @staticmethod
    @itchat.msg_register(itchat.content.PICTURE)
    def _handle_picture(msg):
        return WechatService.handle_image(WechatService(super), msg)

    @staticmethod
    @itchat.msg_register(itchat.content.VIDEO)
    def _handle_video(msg):
        return WechatService.handle_video(WechatService(super), msg)
