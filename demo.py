# -*- coding: utf-8 -*-
from chatbot import ChatBot


def text_handler(bot, msg):
    uid = msg['FromUserName']
    text = str(msg['Content'])
    answer = bot.answer(uid, text)
    return answer.replace("<br />", "\n")

if __name__ == "__main__":
    chatbot = ChatBot("elastic")
    # comment below to avoid reloading FQA and other data, o.w. you should wait for a while before using the bot.
    chatbot.reload()
    service = chatbot.service("wechatmp").set_text_handler(text_handler)
    try:
        service.start()
    except KeyboardInterrupt:
        service.stop()
