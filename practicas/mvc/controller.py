# -*- coding: utf-8 -*-

from model import Todo

class Controller:
    taks = []
    def add_taks(self, todo):
        self.taks.append(todo)

    def list_taks(self):
        return (len(self.taks))