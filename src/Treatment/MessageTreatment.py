# -*- coding: utf-8 -*-
from src.Treatment.Treatment import Treatment


class MessageTreatment(Treatment):

    def __init__(self, message):
        Treatment.__init__(self, message)
