# -*- coding: utf-8 -*-
from abc import abstractmethod


class Bot:

    @abstractmethod
    def answer(self, question): pass
