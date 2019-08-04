# -*- coding: utf-8 -*-

from src.Model.Model import model as Model


class Contact(Model):

    def __init__(self):
        Model.__init__(self, 'contacts')