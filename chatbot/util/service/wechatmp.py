# -*- coding: utf-8 -*-
import itchatmp

from .abstract import WechatService
from ...settings import *


class _WechatMP(WechatService):

    def _start(self):
        itchatmp.update_config(itchatmp.WechatConfig(
                token=WECHAT_TOKEN,
                appId=WECHAT_APP_ID,
                appSecret=WECHAT_APP_SECRET,
                encryptMode=itchatmp.content.SAFE,
                encodingAesKey=WECHAT_ENCODING_AES_KEY
                ),
            filterRequest=False)
        itchatmp.run()

    def _stop(self):
        pass

wechatmp = _WechatMP()


@itchatmp.msg_register(itchatmp.content.TEXT)
def _handle_text(msg):
    return wechatmp.handle_text(msg)


@itchatmp.msg_register(itchatmp.content.VOICE)
def _handle_voice(msg):
    return wechatmp.handle_voice(msg)


@itchatmp.msg_register(itchatmp.content.IMAGE)
def _handle_image(msg):
    return wechatmp.handle_image(msg)


@itchatmp.msg_register(itchatmp.content.VIDEO)
def _handle_video(msg):
    return wechatmp.handle_video(msg)
