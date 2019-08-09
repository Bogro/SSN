# -*- coding: utf-8 -*-
import os


class function(object):

    @staticmethod
    def get_env_value(key):
        return os.getenv(key)

    @staticmethod
    def is_not_empty(attr):
        return attr if len(attr) > 0 else None
