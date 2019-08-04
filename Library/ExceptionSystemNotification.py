
# -*- coding: utf-8 -*-

from .Logger import Logger


class ExceptionSystemNotification(Exception):
    """
    Exception class for application
    """

    def __init__(self):
        Exception.__init__(self)

    def logger_message(self):
        log = Logger()
        log.danger(f"{self}")