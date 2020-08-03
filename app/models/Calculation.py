import math
from PyQt5.QtCore import Qt,pyqtSignal, QModelIndex, QVariant
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlQuery
from PyQt5.QtGui import QColor

class Calculation(QSqlRelationalTableModel):
    
    def __init__(self, *args, **kwargs):
        super(Calculation, self).__init__(*args, **kwargs)
        self.setTable("calculations")
        self.select()

    def data(self, index, role):
        editables = [self.fieldIndex('col_pipe_position'), self.fieldIndex('aux_prof_i'),
                    self.fieldIndex('force_depth_up'),self.fieldIndex('force_depth_down'), 
                    self.fieldIndex('slopes_min_accepted_col'), self.fieldIndex('adopted_diameter')]
        if role == Qt.BackgroundRole:
            row = index.row()
            if index.column() in [self.fieldIndex('col_seg'), self.fieldIndex('depth_up')]:                  
                prevCol = self.record(row -1).value('collector_number')
                col = self.record(row).value('collector_number')                
                if col != prevCol:
                    return QColor(255, 128, 0)
            if  index.column() in [self.fieldIndex('depth_up'), self.fieldIndex('depth_down')]:
                val = self.record(row).value(index.column())
                if 2 <= val <3:
                    return QColor(229,204,255)
                if val >= 3:
                    return QColor(183,163,204)
            if  index.column() in editables:
                if index.column() in [self.fieldIndex('force_depth_up'), self.fieldIndex('force_depth_down')]:
                    val = self.record(row).value(index.column())
                    if val > 0:
                        return QColor(255,192,147)
                return QColor(255,255,178)

        return super(Calculation, self).data(index, role)    

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
    
    def eh(self, qls, dmm, imm, nman):
        if qls == 0:
            return 0
        else:
            return ((nman * qls / 1000)/ ((lmm ** 0.5) * ((dmm / 1000) ** (8/3))))
    
    def ehlin(self, qls, dmm, imm, nman):
        if qls == 0:
            return 0
        else:
            return 8 * ((((((float(nman.replace(',','.')) * qls / 1000) / ((imm**0.5) * ((dmm / 1000) ** (8 / 3))))) ** 3) / 4) ** 0.2)

    def angteta(self, qls, dmm, imm, nman):
        if qls == 0:
            return 0
        tta = 3
        ttb = math.sin(tta) + (self.ehlin(qls,dmm,imm,nman)) * (tta ** 0.4)
        while (abs(tta-ttb) > 0.00001):
            tta = ttb
            ttb = math.sin(tta) + (self.ehlin(qls,dmm,imm,nman)) * (tta ** 0.4)
        return ttb

    def raiohidr(self, qls, dmm, imm, nman):
        if qls == 0:
            return 0
        else:
            angteta = self.angteta(qls, dmm, imm, nman)
            if angteta < (2 * 3.15159265358979):
                return dmm / (1000 * 4) * ((1 - (math.sin(angteta) / angteta)))
            else:
                return -9999999999  #"Diâmetro Insuficiente"
    
    def laminaabs(self, qls, dmm, imm, nman):
        if qls == 0:
            return 0
        else:
            angteta = self.angteta(qls, dmm, imm, nman)
            if angteta < (2 * 3.15159265358979):
                return dmm / (1000 * 2) * ((1 - (math.cos(angteta / 2))))
            else:
                return -8888888888 #DN!!
    
    def laminarel(self, qls, dmm, imm, nman):
        if qls == 0:
            return 0
        else:
            angteta = self.angteta(qls, dmm, imm, nman)
            if angteta < (2 * 3.15159265358979):
                return 0.5 * ((1 - (math.cos(angteta / 2))))
            else:
                return -8888888888 #DN!!
    
    def areamolh(self, qls, dmm, imm, nman):
        if qls == 0:
            return 0
        else:
            angteta = self.angteta(qls, dmm, imm, nman)
            if angteta < (2 * 3.15159265358979):
                return ((dmm / 1000) ** 2) / 8 * ((angteta - (math.sin(angteta))))
            else:
                return -8888888888 #DN!!
    
    def perimolh(self, qls, dmm, imm, nman):
        if qls == 0:
            return 0
        else:
            angteta = self.angteta(qls, dmm, imm, nman)
            if angteta < (2 * 3.15159265358979):
                return dmm / 1000 * (angteta / 2)
            else:
                return -8888888888 #DN!!
    
    def tenstrat(self, qls, dmm, imm, nman):
        if self.angteta(qls, dmm, imm, nman) < (2 * 3.15159265358979):
            return (self.raiohidr(qls, dmm, imm, nman) * imm * 1000 * 9.81)
        else:
            return -8888888888 #DN!!
    
    def velocid(self, qls, dmm, imm, nman):
        if nman == 0:
            return 0
        else:
            if self.angteta(qls, dmm, imm, nman) < (2 * 3.15159265358979):
                return (self.raiohidr(qls, dmm, imm, nman) ** 0.6667) * (imm ** 0.5) / float(nman.replace(',','.'))
            else:
                return -8888888888 #DN!!

    def velocrit(self, qls, dmm, imm, nman):
        if nman == 0:
            return 0
        else:
            if self.angteta(qls, dmm, imm, nman) < (2 * 3.15159265358979):
                return (((self.raiohidr(qls, dmm, imm, nman) * 9.8) ** 0.5) * 6)
            else:
                return -8888888888 #DN!!
    
    def dn1mm(self, qls, imm, nman, tirmx):
        if qls == 0:
            return 0
        else:
            return 1000 * ((nman * qls / 1000) / (self.e2(tirmx) * (imm ** (1 / 2)))) ** (3 / 8)
    

    #Function to estimate the flow section factor E for blades 60 to 90
    def e1(self, tirmax):
        if tirmax == 0:
            return 0
        else:
            return (-0.8224 * (tirmax ** 3)) + (1.3033 * (tirmax ** 2)) - (0.1362 * tirmax)
    

    def e2(self, tirmx):
        if tirmx == 0:
            return 0
        else:
            return (-0.7867 * (tirmx ** 3)) + (1.2133 * (tirmx ** 2)) - (0.0912 * tirmx)