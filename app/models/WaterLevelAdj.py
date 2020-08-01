from PyQt5.QtCore import pyqtSignal, QModelIndex
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlQuery
from PyQt5.QtCore import Qt

class WaterLevelAdj(QSqlRelationalTableModel):
    
    def __init__(self, *args, **kwargs):
        super(WaterLevelAdj, self).__init__(*args, **kwargs)
        self.setTable("wl_adj")
        self.select()
    
    def getValueBy(self, column, where=None):
        sql = "SELECT w.{}\
                FROM wl_adj w\
                LEFT JOIN calculations c ON c.id = w.calculation_id\
                WHERE c.project_id IN (SELECT id FROM projects WHERE active)".format(column)
        if where != None:
            sql = sql + " AND {}".format(where)
        query = QSqlQuery(sql)
        if query.first():
            return query.value(0)