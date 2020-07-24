from PyQt5.QtSql import QSqlTableModel, QSqlQuery
from PyQt5.QtCore import Qt
from ..lib.Store import Store

class InspectionDevice(QSqlTableModel):
    
    def __init__(self, *args, db=Store().getDB(), **kwargs):        
        super(InspectionDevice, self).__init__(*args, **kwargs)
        self.setTable("inspection_devices")
        self.setSort(self.fieldIndex('id'), Qt.AscendingOrder)
        self.select()