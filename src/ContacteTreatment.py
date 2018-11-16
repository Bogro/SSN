import time
import sqlite3

class ContacteTreatment(object):

    database = ''

    def __init__(self, db):
        data = sqlite3.connect(db)
        self.database = data.cursor()


    def __get_contact_in_database(self):
        print('cool')


