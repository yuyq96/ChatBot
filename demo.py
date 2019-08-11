# -*- coding: utf-8 -*-
from chatbot import ChatBot


if __name__ == "__main__":
    chatbot = ChatBot()
    bot = chatbot.add_bot('elastic')
    # comment below to avoid reloading FQA and other data, o.w. you should wait for a while before using the bot.
    bot.init()
    def text_handler(uid, q):
        return bot.answer(uid, q)
    service = chatbot.add_service('http').set_handler(text_handler).listen(9201)
    try:
        service.start()
    except KeyboardInterrupt:
        service.stop()
