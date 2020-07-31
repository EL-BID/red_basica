from PyQt5.QtCore import pyqtSignal, QModelIndex
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlQuery
from PyQt5.QtCore import Qt

class Project(QSqlRelationalTableModel):
    
    def __init__(self, *args, **kwargs):        
        super(Project, self).__init__(*args, **kwargs)
        self.setTable("projects")
        self.select()

    # def refresh(self):
    #     self.dataChanged.emit(QModelIndex(), QModelIndex())
    #     self.select()

    # def getDisplayColumn(self):
    #     return self.nameFieldIndex        

    def getActiveProject(self):
        currentProjectId = None
        query = QSqlQuery("SELECT id FROM projects WHERE active")
        while query.next():
            currentProjectId = query.value(0)
        return self.record(currentProjectId) if currentProjectId else currentProjectId

    @staticmethod
    def getActiveProjectParameter():
        #TODO: check if theres is more than one active project (sqlite does not support query.size()) 
        query = QSqlQuery("select parameter_id from projects where active")                
        if query.first():
            return query.value(0)
        return None            

    @staticmethod
    def setParameterToActive(parameter_id):
        query = QSqlQuery()
        query.prepare("UPDATE projects SET parameter_id = :parameter_id WHERE active and parameter_id is NULL")
        query.bindValue(":parameter_id", parameter_id)
        query.exec_()

    @staticmethod
    def getActiveId():
        query = QSqlQuery("select id from projects where active")                
        if query.first():
            return query.value(0)
        return None    

    def getNameActiveProject(self):
        currentProjectName = None
        query = QSqlQuery("SELECT name FROM projects WHERE active")
        while query.next():
            currentProjectName = query.value(0)
        return str(currentProjectName)

    def setActive(self, id):        
        # current = self.getActiveProject()
        # if current:
        #     current.setValue('active', 0)
        # newActive = self.record(id)
        # newActive.setValue('active', 1)       
        # self.submitAll()                    
        query = QSqlQuery("UPDATE projects SET active = 0")
        queryUpdate = QSqlQuery()
        queryUpdate.prepare("UPDATE projects SET active = 1 WHERE id = :id ")
        queryUpdate.bindValue(":id", id)
        queryUpdate.exec_()
         