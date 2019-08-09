
# -*- coding: utf-8 -*-

from .Logger import Logger


class ExceptionSystemNotification(Exception):
    """
    Exception class for application
    """

    def __init__(self, message):
        Exception.__init__(self, message)

    def logger_message(self):
        log = Logger()
        log.danger(f"{self}")