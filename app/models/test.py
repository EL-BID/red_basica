from PyQt5.QtCore import pyqtSignal
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt
from ..lib.Store import Store

class Test(QSqlTableModel):
    
    def __init__(self, *args, db=Store().getDB(), **kwargs):        
        super(Test, self).__init__(*args, **kwargs)
        self.setTable("todo")
        self.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.select()
        self.setHeaderData(0, Qt.Horizontal, "ID")
        self.setHeaderData(1, Qt.Horizontal, "task")        
        