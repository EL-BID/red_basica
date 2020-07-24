from PyQt5.QtSql import QSqlTableModel, QSqlRelationalTableModel, QSqlRelation
from PyQt5.QtCore import Qt
from ..lib.Store import Store

class Pipe(QSqlRelationalTableModel):
    
    def __init__(self, *args, db=Store().getDB(), **kwargs):        
        super(Pipe, self).__init__(*args, **kwargs)
        self.setTable("pipes")
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.setSort(self.fieldIndex('id'), Qt.AscendingOrder)                        
        self.setRelation(self.fieldIndex("material_id"), QSqlRelation("materials", "id", "name_es"))
        #headers
        self.setHeaderData(self.fieldIndex("diameter"), Qt.Horizontal, "DN(mm)")
        self.setHeaderData(self.fieldIndex("material_id"), Qt.Horizontal, "Material")        
        self.setHeaderData(self.fieldIndex("manning_suggested"), Qt.Horizontal, "C. Manning n sugerido")
        self.setHeaderData(self.fieldIndex("manning_adopted"), Qt.Horizontal, "C. Manning n adoptado")
        self.select() 