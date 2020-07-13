from PyQt5.QtCore import pyqtSignal, QModelIndex
from PyQt5.QtSql import QSqlTableModel, QSqlQuery
from PyQt5.QtCore import Qt
from ..lib.Store import Store

class Country(QSqlTableModel):
    
    def __init__(self, *args, db=Store().getDB(), **kwargs):        
        super(Country, self).__init__(*args, **kwargs)
        self.setTable("countries")
        self.nameFieldIndex = self.fieldIndex('name_es')
        self.setSort(self.nameFieldIndex, Qt.AscendingOrder)        
        self.select()
         