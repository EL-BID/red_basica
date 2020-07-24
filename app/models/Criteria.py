from PyQt5.QtCore import pyqtSignal, QModelIndex, QDateTime
from PyQt5.QtSql import QSqlTableModel, QSqlRelationalTableModel, QSqlQuery
from PyQt5.QtCore import Qt
from ..lib.Store import Store

class Criteria(QSqlTableModel):
    
    def __init__(self, *args, db=Store().getDB(), **kwargs):        
        super(Criteria, self).__init__(*args, **kwargs)
        self.setTable("project_criterias")
        self.setSort(self.fieldIndex('id'), Qt.AscendingOrder)
        self.select()

    def getValueBy(self, column):
        query = QSqlQuery("SELECT pc."+column+" FROM project_criterias pc LEFT JOIN parameters pa ON pa.project_criteria_id = pc.id LEFT JOIN projects pr ON pr.parameter_id = pa.id WHERE pr.active")
        if query.first():
            return query.value(0)