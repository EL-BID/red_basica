from PyQt5.QtCore import pyqtSignal, QModelIndex, QDateTime
from PyQt5.QtSql import QSqlTableModel, QSqlQuery
from PyQt5.QtCore import Qt
from ..lib.Store import Store

class Parameter(QSqlTableModel):
    
    def __init__(self, *args, db=Store().getDB(), **kwargs):        
        super(Parameter, self).__init__(*args, **kwargs)
        self.setTable("parameters")
        self.select()

    def createEmptyRecord(self):
        lastId = None
        record = self.record()
        record.setValue('project_criteria_id', 1)
        record.setValue('created_at', QDateTime.currentDateTime())
        record.setValue('updated_at', QDateTime.currentDateTime())
        newRecord = self.insertRecord(-1, record)
        if newRecord:
            lastId = self.query().lastInsertId()
        return lastId            
