from imaplib import IMAP4
from smtplib import SMTP
from email import message_from_string

class SendNotificationTreatment(object):
    def __init__(self):
        print('sent')