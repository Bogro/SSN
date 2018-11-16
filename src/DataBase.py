import sqlite3


class DataBase(object):
    data = ''
    db = ''

    def __init__(self, db='./sqlite/data.db'):
        self.data = db

    def __connect_db__(self):
        try:
            self.db = sqlite3.connect(self.data)
        except:
            print('Erreur data base connect')

    def __create_table__(self, table, colum):
        req = 'create table %s (%s)' % (table, colum)
        self.__execute_request__(req)

    def __execute_request__(self, request):
        self.db.execute(request)
