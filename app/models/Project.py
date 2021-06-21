from PyQt5.QtCore import pyqtSignal, QModelIndex
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlQuery
from PyQt5.QtCore import Qt
from qgis.core import QgsProject

class Project(QSqlRelationalTableModel):
    
    def __init__(self, *args, **kwargs):        
        super(Project, self).__init__(*args, **kwargs)
        self.setTable("projects")
        self.select()

    def getActiveProject(self):
        currentProjectId = None
        query = QSqlQuery("SELECT id FROM projects WHERE active")
        while query.next():
            currentProjectId = query.value(0)
        return self.record(currentProjectId) if currentProjectId else currentProjectId

    def getValueBy(self, column, projectId, where=None):
        sql = "SELECT {}\
                FROM projects\
                WHERE id = {}".format(column, projectId)
        if where != None:
            sql = sql + " AND {}".format(where)
        query = QSqlQuery(sql)
        if query.first():
            return query.value(0)
        else:
            return None

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

    @staticmethod
    def deleteAll():
        query = QSqlQuery()
        query.exec("PRAGMA foreign_keys=on;")           
        a = query.exec("delete from parameters;")
        b = query.exec("delete from projects;")
        query.exec("VACUUM;")
        return (a and b)
    
    def deleteProject(self, id):
        """ delete cascade project by id """
        query = QSqlQuery()
        query.exec("PRAGMA foreign_keys=on;")           
        a = query.exec("delete from parameters where id in (select parameter_id from projects where id = {});".format(id))
        b = query.exec("delete from projects where id = {};".format(id))
        query.exec("VACUUM;")
        return (a and b)
   
    def getNameActiveProject(self):
        currentProjectName = None
        query = QSqlQuery("SELECT name FROM projects WHERE active")
        while query.next():
            currentProjectName = query.value(0)
        return str(currentProjectName)

    def setActive(self, id):                           
        """ Set the active project by id"""        
        query = QSqlQuery("UPDATE projects SET active = 0")
        queryUpdate = QSqlQuery()
        queryUpdate.prepare("UPDATE projects SET active = 1 WHERE id = :id ")
        queryUpdate.bindValue(":id", id)
        queryUpdate.exec_()

    def setSrid(self, id):
        """ Set SRID project by id"""
        srid = QgsProject.instance().crs().postgisSrid()
        queryUpdate = QSqlQuery()
        queryUpdate.prepare("UPDATE projects SET srid = :srid WHERE id = :id ")
        queryUpdate.bindValue(":srid", srid)
        queryUpdate.bindValue(":id", id)
        queryUpdate.exec_()
         
    def handleMissingActive(self):
        """ prevents from not having active project """
        query = QSqlQuery()          
        query.exec("UPDATE projects SET active = 1 limit 1;")

    def updateServerId(self, serverId):
        sql = "UPDATE projects SET server_id = {} \
               WHERE active == true".format(serverId)
        query = QSqlQuery(sql)
        if query.lastError().isValid():
            return query.lastError()
        return True

    def updateDefaultView(self, bool):
        sql = "UPDATE projects SET default_view = {} \
               WHERE active == true".format(bool)
        query = QSqlQuery(sql)
        if query.lastError().isValid():
            return query.lastError()
        return True

    def getDefaultView(self):
        sql = "SELECT default_view FROM projects \
               WHERE active == true"
        query = QSqlQuery(sql)
        if query.first():
            return bool(query.value(0))
        return True

    def updateDepthMinView(self, bool):
        sql = "UPDATE projects SET depth_min_view = {} \
               WHERE active == true".format(bool)
        query = QSqlQuery(sql)
        if query.lastError().isValid():
            return query.lastError()
        return True

    def getDepthMinView(self):
        sql = "SELECT depth_min_view FROM projects \
               WHERE active == true"
        query = QSqlQuery(sql)
        if query.first():
            print(query.value(0))
            if (query.value(0) == None):
                return None
            return bool(query.value(0))
        return None