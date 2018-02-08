# -*- coding: utf-8 -*-
from qabot import QABot

if __name__ == "__main__":
    bot = QABot("elastic").get()
    # uncomment below to load FQA in the first time, you may wait for the elastic loading (async)
    # bot.create(delete_if_exist=True)
    # bot.load()
    print("QABot running, ask some questions! (Type 'exit' to exit)")
    question = input("Q: ")
    while question != "exit":
        answer = bot.answer(question)
        print("A: %s" % answer)
        question = input("Q: ")
