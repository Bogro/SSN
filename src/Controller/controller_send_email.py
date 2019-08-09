# -*- coding: utf-8 -*-
from .controller import controller


class controller_send_email(controller):
    
    def __init__(self):
        controller.__init__(self)

    def action_send_message(self, message, contacts):
        email = contacts['OK'][:]

        print(message, email)

    