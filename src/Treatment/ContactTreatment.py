# -*- coding: utf-8 -*-

import os

from ..Model.Contact import Contact
from .Treatment import Treatment
from phone_email_verifier.phone_verifier import phone_verifier as Phone
from phone_email_verifier.email_verifier import email_verifier as Email


class ContactTreatment(Treatment):

    def __init__(self, list_contact, type_contact):
        Treatment.__init__(self, list_contact)
        self.type_contact = type_contact

    def treatment_contact(self):
    
        if self.type_contact == 'phone':

            phone = Phone()
            phone.set_phone_list(self.get_data(self.data), self.get_country_phone(), self.get_country_code())

            self.data = phone.exec()
            
        else:

            email = Email()
            email.set_email_list(self.get_data(self.data), self.get_country_email())

            self.data = email.exec()