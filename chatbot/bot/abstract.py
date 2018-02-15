# -*- coding: utf-8 -*-
from abc import abstractmethod


class Bot:

    @abstractmethod
    def init(self): pass

    @abstractmethod
    def answer(self, uid, question): pass
