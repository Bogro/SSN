import sys
import os
import datetime
from .sqlite.Sqlite import Sqlite


class Model(object):

    sql = None
    id = ''
    create_at = ''
    update_at = ''

    def __init__(self):
        self.sql = Sqlite()

    def __get_id__(self):
        return self.id

    def __get_create_at__(self):
        return self.create_at

    def __get_update_at__(self):
        return self.update_at
