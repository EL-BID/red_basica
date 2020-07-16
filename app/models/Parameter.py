from PyQt5.QtCore import pyqtSignal, QModelIndex, QDateTime
from PyQt5.QtSql import QSqlTableModel, QSqlRelationalTableModel, QSqlQuery, QSqlRelation
from PyQt5.QtCore import Qt
from ..lib.Store import Store

class Parameter(QSqlTableModel):
    
    def __init__(self, *args, db=Store().getDB(), **kwargs):        
        super(Parameter, self).__init__(*args, **kwargs)
        self.setTable("parameters")
        #self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        #self.setRelation(1, QSqlRelation("project_criterias", "id", "name"))
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

    def getCurrentData(self):
        data = None
        strQuery = "select p.id, c.id from parameters p join \
                    project_criterias c on p.project_criteria_id = c.id \
                    where p.id in (select parameter_id from projects where active)"
        query = QSqlQuery(strQuery)
        while query.next():
            data = { 'parameter_id': query.value(0), 'criteria_id': query.value(1) }
        return data