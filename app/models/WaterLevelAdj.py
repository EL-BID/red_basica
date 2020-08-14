from PyQt5.QtCore import Qt, pyqtSignal, QModelIndex, QAbstractTableModel
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlQuery 

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
        else:
            return 0
    
    # A2.AB13
    def getMaxNaDiffNeeded(self):
        sql = "SELECT MAX(w.na_diff_needed)\
                FROM wl_adj w\
                LEFT JOIN calculations c ON c.id = w.calculation_id\
                WHERE c.project_id IN (SELECT id FROM projects WHERE active)"
        query = QSqlQuery(sql)
        if query.first():
            return query.value(0)
        else:
            return 0