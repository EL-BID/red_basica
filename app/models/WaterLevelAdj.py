from PyQt5.QtCore import pyqtSignal, QModelIndex
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel
from PyQt5.QtCore import Qt

class WaterLevelAdj(QSqlRelationalTableModel):
    
    def __init__(self, *args, **kwargs):
        super(WaterLevelAdj, self).__init__(*args, **kwargs)
        self.setTable("wl_adj")
        self.select()