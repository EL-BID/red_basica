from PyQt5.QtCore import pyqtSignal, QModelIndex
from PyQt5.QtSql import QSqlTableModel, QSqlQuery
from PyQt5.QtCore import Qt
from ..lib.Store import Store

class Project(QSqlTableModel):
    
    def __init__(self, *args, db=Store().getDB(), **kwargs):        
        super(Project, self).__init__(*args, **kwargs)
        self.setTable("projects")
        self.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.nameFieldIndex = self.fieldIndex('name')
        self.activeFieldIndex = self.fieldIndex('active')
        self.setSort(self.activeFieldIndex, Qt.DescendingOrder)
        self.select()

    def refresh(self):
        self.dataChanged.emit(QModelIndex(), QModelIndex())
        self.select()

    def getDisplayColumn(self):
        return self.nameFieldIndex        

    def getActiveProject(self):
        currentProjectId = None
        query = QSqlQuery("SELECT id FROM projects where active")
        while query.next():
            currentProjectId = query.value(0)
        return self.record(currentProjectId) if currentProjectId else currentProjectId

    def setActive(self, id):        
        # current = self.getActiveProject()
        # if current:
        #     current.setValue('active', 0)
        # newActive = self.record(id)
        # newActive.setValue('active', 1)       
        # self.submitAll()                    
        query = QSqlQuery("update projects set active = 0")        
        queryUpdate = QSqlQuery()
        queryUpdate.prepare("update projects set active = 1 where id = :id ")
        queryUpdate.bindValue(":id", id)
        queryUpdate.exec_()        
         