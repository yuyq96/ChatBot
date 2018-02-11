# -*- coding: utf-8 -*-
from chatbot import ChatBot

if __name__ == "__main__":
    bot = ChatBot("elastic")
    # comment below to avoid reloading FQA and other data, o.w. you should wait for a while before using the bot.
    bot.reload()
    service = bot.service("http")
    try:
        service.start()
    except KeyboardInterrupt:
        service.stop()
