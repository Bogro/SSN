# -*- coding: utf-8 -*-
import os
from Library.Function import function
from Library.ExceptionSystemNotification import ExceptionSystemNotification
from src.Treatment.MessageTreatment import MessageTreatment
from src.Treatment.ContactTreatment import ContactTreatment
from src.Controller.controller_send_email import controller_send_email
from src.Controller.controller_send_sms import controller_send_sms


class App(object):

    def __init__(self, parser):
        if parser == 'send_sms':
            self.controller = controller_send_sms()
            self.type_contact = 'phone'
        elif parser == 'send_email':
            self.controller = controller_send_email()
            self.type_contact = 'email'

        self.message = None
        self.contact = None

    def message_treatment(self, message):
        treatment = MessageTreatment(message.split('=')[1])

        self.message = treatment.result()

    def contact_treatment(self, contact):
        treatment = ContactTreatment(contact.split('=')[1], self.type_contact)
        treatment.treatment_contact()
        self.contact = treatment.result()

    def exec_treatment(self):
        self.controller.action_send_message(self.message, self.contact)
