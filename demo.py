# -*- coding: utf-8 -*-
from chatbot import ChatBot

if __name__ == "__main__":
    bot = ChatBot("elastic")
    # uncomment below to reload FQA and other data, you should wait for a while before using the bot.
    bot.reload()
    service = bot.service("http")
    try:
        service.start()
    except KeyboardInterrupt:
        service.stop()
