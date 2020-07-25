from PyQt5.QtCore import pyqtSignal, QModelIndex
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlQuery
from PyQt5.QtCore import Qt
from ..lib.Store import Store

class Contribution(QSqlRelationalTableModel):
    
    def __init__(self, *args, db=Store().getDB(), **kwargs):
        super(Contribution, self).__init__(*args, **kwargs)
        self.setTable("contributions")
        self.select()