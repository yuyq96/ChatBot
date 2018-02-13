# -*- coding: utf-8 -*-
import itchatmp

from .abstract import WechatService
from ...settings import *


class WechatMP(WechatService):

    def _start(self):
        itchatmp.update_config(itchatmp.WechatConfig(
                token=WECHAT_TOKEN,
                appId=WECHAT_APP_ID,
                appSecret=WECHAT_APP_SECRET),
            filterRequest=True)
        itchatmp.run()

    def _stop(self):
        pass

    @staticmethod
    @itchatmp.msg_register(itchatmp.content.TEXT)
    def _handle_text(msg):
        return WechatService.handle_text(WechatService(super), msg)

    @staticmethod
    @itchatmp.msg_register(itchatmp.content.VOICE)
    def _handle_voice(msg):
        return WechatService.handle_voice(WechatService(super), msg)

    @staticmethod
    @itchatmp.msg_register(itchatmp.content.IMAGE)
    def _handle_image(msg):
        return WechatService.handle_image(WechatService(super), msg)

    @staticmethod
    @itchatmp.msg_register(itchatmp.content.VIDEO)
    def _handle_video(msg):
        return WechatService.handle_video(WechatService(super), msg)
