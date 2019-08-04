import sqlite3

class Sqlite(object):
    data = ''
    db = ''
    c = ''

    def __init__(self, db = './sqlite/data.db'):
        self.data = db

    # connection a la base de donnée
    def connectDB(self):
        try:
            self.db = sqlite3.connect(self.data)
            self.c.cursor()
        except:
            print('Error data base not connect')

    # creation de table
    def createTable(self, table, colum):
        req = 'create table %s (%s)' % (table, colum)
        self.executeRequest(req)

    # insertion dans une table
    def insertionInTable(self, table, value=list()):
        list_value = ''
        req = 'insert into %s (%s)' % (table, list_value)
        self.executeRequest(req)

    # execution
    def executeRequest(self, request):
        try:
            self.db.execute(request)
        except:
            print('Error execution request')

    def commit(self):
        try:
            self.db.commit()
            self.c.close()
        except:
            print('Erreur')