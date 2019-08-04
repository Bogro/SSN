# -*- coding: utf-8 -*-
import os


class function(object):

    @staticmethod
    def get_env_value(key):
        return os.getenv(key)
