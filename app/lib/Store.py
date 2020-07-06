import os
from PyQt5.QtSql import QSqlDatabase,QSqlQuery

class Store():
    def __init__(self):
        file_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'sanibid.db')
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(file_path)
        self.initialize()
        
    def initialize(self):
        if self.db.open():
            print("open DB success")
            if not self.db.tables():
                print( "No tables found")
                self.createTables()
                self.db.close()
            else:
                print("Tables already exist")                
        else:
            print("Error openind database")

    def createTables(self):
        print("creating tables ...")
        query = QSqlQuery()        

        query.exec_("CREATE TABLE IF NOT EXISTS projects\
            (id integer primary key autoincrement,\
            parameter_id integer,\
            name text unique not null,\
            country text,\
            city text,\
            microsystem text,\
            author text,\
            active boolean,\
            date date,\
            created_at datetime,\
            updated_at datetime)")
                    

    def getDB(self):
        return self.db