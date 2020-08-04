from PyQt5.QtCore import Qt, pyqtSignal, QModelIndex,QAbstractTableModel
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlQuery

class Contribution(QSqlRelationalTableModel):
    
    def __init__(self, *args, **kwargs):
        super(Contribution, self).__init__(*args, **kwargs)
        self.setTable("contributions")
        self.select()

    def flags(self, index):
        return QAbstractTableModel.flags(self, index) 