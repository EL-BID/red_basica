from PyQt5.QtCore import pyqtSignal, QModelIndex, QDateTime
from PyQt5.QtSql import QSqlTableModel, QSqlRelationalTableModel, QSqlQuery, QSqlRelation
from PyQt5.QtCore import Qt
from ..lib.Store import Store

class Parameter(QSqlTableModel):
    
    def __init__(self, *args, db=Store().getDB(), **kwargs):        
        super(Parameter, self).__init__(*args, **kwargs)
        self.setTable("parameters")
        self.select()

    def getValueBy(self, column):
        query = QSqlQuery("SELECT p."+column+"\
                        FROM parameters p\
                        LEFT JOIN projects pr ON p.id = pr.parameter_id\
                        WHERE pr.active")
        if query.first():
            return query.value(0)