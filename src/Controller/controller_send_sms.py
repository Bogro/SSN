# -*- coding: utf-8 -*-
from .controller import controller

class controller_send_sms(controller):

    def __init__(self):
        controller.__init__(self)

    def action_send_message(self, message, contacts):
        phones = contacts['OK'][:]
        
        print(message, phones)
