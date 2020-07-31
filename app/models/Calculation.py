from PyQt5.QtCore import pyqtSignal, QModelIndex
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlQuery
from PyQt5.QtCore import Qt

class Calculation(QSqlRelationalTableModel):
    
    def __init__(self, *args, **kwargs):
        super(Calculation, self).__init__(*args, **kwargs)
        self.setTable("calculations")
        self.select()


    # $RedBasica.$F$11
    def getExtensionSum(self):
        query = QSqlQuery("SELECT sum(extension)\
                        FROM calculations c\
                        LEFT JOIN projects p ON c.project_id = p.id\
                        AND p.active")
        if query.first():
            return round(query.value(0),1)

    # $RedBasica.$K$11
    def getQtyFinalQeSum(self):
        query = QSqlQuery("SELECT sum(qty_final_qe)\
                        FROM calculations c\
                        LEFT JOIN projects p ON c.project_id = p.id\
                        AND p.active")
        if query.first():
            return round(query.value(0),1)

    # $RedBasica.$L$11
    def getQtyInitialQeSum(self):
        query = QSqlQuery("SELECT sum(qty_initial_qe)\
                        FROM calculations c\
                        LEFT JOIN projects p ON c.project_id = p.id\
                        AND p.active")
        if query.first():
            return round(query.value(0),1)

    # $A1.$C$14 Previous Segment - Current Collector Pipe (l/s)
    def getTotalFlowEndByColSeg(self, colSeg):
        query = QSqlQuery("SELECT total_flow_rate_end\
                        FROM calculations\
                        WHERE col_seg = '{}'".format(colSeg))
        if query.first():
            return 0 if query.value(0)==None else round(query.value(0),2)
        else: 
            return 0

    def getTotalFlowStartByColSeg(self, colSeg):
        query = QSqlQuery("SELECT total_flow_rate_start\
                        FROM calculations\
                        WHERE col_seg = '{}'".format(colSeg))
        if query.first():
            return 0 if query.value(0)==None else round(query.value(0),2)
        else: 
            return 0

    def getValueBy(self, column, where=None):
        sql = "SELECT c.{}\
                FROM calculations c\
                LEFT JOIN projects pr ON c.project_id = pr.id\
                WHERE pr.active".format(column)
        if where != None:
            sql = sql + " AND {}".format(where)
        query = QSqlQuery(sql)
        if query.first():
            return query.value(0)