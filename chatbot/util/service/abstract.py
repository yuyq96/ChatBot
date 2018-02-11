# -*- coding: utf-8 -*-
from abc import abstractmethod


class Service:

    @abstractmethod
    def start(self): pass

    @abstractmethod
    def stop(self): pass
