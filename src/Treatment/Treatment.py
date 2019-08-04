# -*- coding: utf-8 -*-

import os

class Treatment(object):

    def __init__(self, data):
        self.data = data

    def get_data(self, contacts):
        
        if '-' not in contacts:
            return [contacts]
        else:
            return [contact for contact in contacts.split('-')]

    def get_country_email(self):
        coun = os.getenv('COUNTRY_EMAIL')
        return coun if len(coun) > 0 else None
    
    def get_country_phone(self):
        coun = os.getenv('COUNTRY_PHONE')
        return coun if len(coun) > 0 else None

    def get_country_code(self):
        code = os.getenv('CODE_PHONE')
        return code if len(code) > 0 else None


    def result(self):
        return self.data