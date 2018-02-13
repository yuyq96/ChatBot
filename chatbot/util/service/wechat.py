# -*- coding: utf-8 -*-
import itchat

from .abstract import WechatService


class _Wechat(WechatService):

    def _start(self):
        itchat.auto_login(hotReload=False, enableCmdQR=False)
        itchat.run()

    def _stop(self):
        itchat.logout()

wechat = _Wechat(None)


@itchat.msg_register(itchat.content.TEXT)
def _handle_text(msg):
    return wechat.handle_text(msg)


@itchat.msg_register(itchat.content.VOICE)
def _handle_voice(msg):
    return wechat.handle_voice(msg)


@itchat.msg_register(itchat.content.PICTURE)
def _handle_picture(msg):
    return wechat.handle_image(msg)


@itchat.msg_register(itchat.content.VIDEO)
def _handle_video(msg):
    return wechat.handle_video(msg)
