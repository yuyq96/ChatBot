# -*- coding: utf-8 -*-
from chatbot import ChatBot


def text_handler(bot, msg):
    uid = msg['FromUserName']
    text = str(msg['Content'])
    answer = bot.answer(uid, text)
    return answer.replace("<br />", "\n")


if __name__ == "__main__":
    chatbot = ChatBot()
    bot = chatbot.add_bot('elastic')
    # comment below to avoid reloading FQA and other data, o.w. you should wait for a while before using the bot.
    bot.init()
    service = chatbot.add_service('http').set_handler(text_handler).listen(9201)
    try:
        service.start()
    except KeyboardInterrupt:
        service.stop()
