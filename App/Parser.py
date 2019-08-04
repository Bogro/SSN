# -*- coding: utf-8 -*-

"""
Auteur : christian BOGRO
Date : 04/08/2019
"""
from src.App import App
from Library.ExceptionSystemNotification import ExceptionSystemNotification
from App.Config import config


class Parser(object):

    def __init__(self, argv):
        """
        Constructor
        :param argv:
        """
        self.argv = argv
        self.command = None

    def treatment_parser(self):
        
        try:

            if len(self.argv) > 3:
                raise ExceptionSystemNotification('ERROR: ')

            treatement = self.argv[0]
            contact = self.argv[1]
            message = self.argv[2]
            
            app = App(treatement)

            if 'message' in message:
                app.message_treatment(message)
                
            if 'contact' in contact:
                app.contact_treatment(contact)

            app.exec_treatment()

        except ExceptionSystemNotification as E:
            E.logger_message()
