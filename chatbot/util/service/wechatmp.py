# -*- coding: utf-8 -*-
import itchatmp

from .abstract import WechatService
from ...settings import *


class _WechatMP(WechatService):

    def _start(self):
        itchatmp.update_config(itchatmp.WechatConfig(
                token=WECHAT_TOKEN,
                appId=WECHAT_APP_ID,
                appSecret=WECHAT_APP_SECRET),
            filterRequest=True)
        itchatmp.run()

    def _stop(self):
        pass

wechatmp = _WechatMP(None)


@itchatmp.msg_register(itchatmp.content.TEXT)
def _handle_text(msg):
    return wechatmp.handle_text(msg['text'])


@itchatmp.msg_register(itchatmp.content.VOICE)
def _handle_voice(msg):
    return wechatmp.handle_voice(msg['voice'])


@itchatmp.msg_register(itchatmp.content.IMAGE)
def _handle_image(msg):
    return wechatmp.handle_image(msg['image'])


@itchatmp.msg_register(itchatmp.content.VIDEO)
def _handle_video(msg):
    return wechatmp.handle_video(msg['video'])
