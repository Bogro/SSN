# -*- coding: utf-8 -*-

import sys

from App.Parser import Parser
from Library.ExceptionSystemNotification import ExceptionSystemNotification
from src.App import App


def main():
    kernel = Kernel(sys.argv)

    kernel.exec()


class Kernel(object):

    def __init__(self, argv):
        self.parser = Parser(argv[1:])

    def exec(self):
        self.parser.treatment_parser()
        #app = App(list_parser)

        #app.exec_treatment()


class Configuration(object):
    pass
