from PyQt5.QtCore import pyqtSignal, QModelIndex, QDateTime
from PyQt5.QtSql import QSqlTableModel, QSqlQuery
from PyQt5.QtCore import Qt
from ..lib.Store import Store

class Criteria(QSqlTableModel):
    
    def __init__(self, *args, db=Store().getDB(), **kwargs):        
        super(Criteria, self).__init__(*args, **kwargs)
        self.setTable("project_criterias")
        self.setSort(self.fieldIndex('id'), Qt.AscendingOrder)
        self.select()       

    # def getList(self):        
    #     criteria_list = []
    #     for i in range(self.rowCount()):
    #         _id = self.record(i).value("id")
    #         name = self.record(i).value("name")
    #         criteria_list.append((_id, name))
    #     return criteria_list        