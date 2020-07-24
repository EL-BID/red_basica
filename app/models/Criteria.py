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
