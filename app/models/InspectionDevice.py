from PyQt5.QtSql import QSqlTableModel, QSqlQuery, QSqlRelationalTableModel
from PyQt5.QtCore import Qt
from ..lib.Store import Store

class InspectionDevice(QSqlTableModel):
    
    def __init__(self, *args, db=Store().getDB(), **kwargs):        
        super(InspectionDevice, self).__init__(*args, **kwargs)        
        self.setTable("inspection_devices")
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.setSort(self.fieldIndex('id'), Qt.AscendingOrder)                        
        #headers
        self.setHeaderData(self.fieldIndex("type_es"), Qt.Horizontal, "Tipo")
        self.setHeaderData(self.fieldIndex(""), Qt.Horizontal, "Prof. máxima (m)")        
        self.setHeaderData(self.fieldIndex(""), Qt.Horizontal, "DN Máximo (mm)")
        
        self.select() 