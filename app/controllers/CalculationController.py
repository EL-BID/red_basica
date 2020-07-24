from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlQuery
from ..models.Calculation import Calculation
from ..models.Parameter import Parameter
from ..models.Criteria import Criteria
from ..models.Contribution import Contribution
from .DataController import DataController
import time

class CalculationController(QObject):
    def __init__(self):
        super().__init__()
        self.model = Calculation()
        self.parameterModel = Parameter()
        self.critModel = Criteria()
        self.contModel = Contribution()

    def importData(self, projectId):
        #TODO each time the parameter is changed, we have to import again? 
        if not self.checkFirstImport(projectId):
            start_time = time.time()
            self.uploadCalculations()
            self.generateContributions()
            print("Total time execution to upload: --- %s seconds ---" % (time.time() - start_time))
        else:
            print('Its imported')

    def checkFirstImport(self, projectId):
        print('Checking if is imported')
        imported = 0
        #TODO bind value is not working
        query = QSqlQuery("SELECT count(*)>0 FROM calculations WHERE project_id = "+str(projectId))
        while query.next():
            imported = query.value(0)
        return bool(imported)
    
    def uploadCalculations(self):
        print('uploading..')
        #TODO put the progress dialog into the Data Controller
        data = DataController().getJsonData()
        for row in data:
            self.model.select()
            rec = self.model.record()
            rec.setValue('project_id',1)
            rec.setValue('initial_segment',row['AUX_TRM_I'])
            rec.setValue('initial segment',row['AUX_TRM_I'])
            rec.setValue('final_segment',row['AUX_TRM_F'])
            rec.setValue('collector_number',row['ID_COL'])
            rec.setValue('col_seg',row['ID_TRM_(N)'])
            rec.setValue('extension',row['L'])
            rec.setValue('previous_col_seg_id',row['TRM_(N-1)_A'])
            rec.setValue('m1_col_id',row['TRM_(N-1)_B'])
            rec.setValue('m2_col_id',row['TRM_(N-1)_C'])
            if not row['ID_UC'] == 'NULL':
                rec.setValue('block_others_id',row['ID_UC'])
            rec.setValue('qty_final_qe',row['QE_FP']) if 'QE_FP' in row else rec.setValue('qty_final_qe',row['QEF'])
            rec.setValue('qty_initial_qe',row['QE_IP']) if 'QE_IP' in row else rec.setValue('qty_final_qe',row['QEI'])
            intake_in_seg = round(self.critModel.getValueBy('intake_rate') * self.strToFloat(row['L'])/1000, 4)
            rec.setValue('intake_in_seg', intake_in_seg)
            if not row['AUX_POS'] == 'NULL':
                rec.setValue('col_pipe_position',row['AUX_POS'])
            if not row['AUX_PROF_I'] == 'NULL':
                rec.setValue('aux_prof_i',row['AUX_PROF_I'])
            rec.setValue('el_terr_up',row['COTA_I'])
            rec.setValue('el_terr_down',row['COTA_F'])
            rec.setValue('inspection_id_up',row['NODO_I'])
            rec.setValue('inspection_id_down',row['NODO_F'])
            rec.setValue('downstream_seg_id',row['TRM_(N+1)'])
            rowCount = self.model.rowCount()
            if (self.model.insertRecord(rowCount,rec)):
                cRec = self.contModel.record()
                cRec.setValue('calculation_id', self.model.query().lastInsertId())
                condominial_lines_end = self.getMaximumFlow() * self.strToFloat(row['QE_FP'])
                cRec.setValue('condominial_lines_end', condominial_lines_end)
                cRec.setValue('col_seg',row['ID_TRM_(N)'])
                cRec.setValue('condominial_lines_start',self.getCondominialLinesStart(row['QE_IP']))
                cRow = self.contModel.rowCount()
                self.contModel.insertRecord(cRow, cRec)

    #TODO
    def generateContributions(self):
        print('generataeContributions')

    # $Parametros.$L$24 || Getting Maximum Flow l/s
    def getMaximumFlow(self):
        occupancy_rate_start = self.parameterModel.getValueBy('occupancy_rate_start')
        x = self.critModel.getValueBy('water_consumption_pc * pc.coefficient_return_c * pc.k1_daily * pc.k2_hourly')
        return round((x * occupancy_rate_start) / 86400, 4)

    # $A1.$B$1
    def getContributionAux(self, extension):
        contribution_sewage = self.parameterModel.getValueBy('contribution_sewage')
        return 0 if (contribution_sewage == 0 or extension == 0 ) else 1

    # $A1.$M$1 || Condominial Lines and Others (l/s)
    def getCondominialLinesStart(self, qeIp):
        qeIp = self.strToFloat(qeIp)
        return round(qeIp * self.getMaximumFlow() / self.critModel.getValueBy('k1_daily'), 2)

    # $A1.$N$1 START-Linear Contribution in Segment (l/s)
    def getLinearContributionInSegment(self, ext):
        #if($RedBasica.$F15=0;0;$B15*$Parametros.$F$42*$Parametros.$F$37*$RedBasica.$F15/1000)
        #if $F15 = extension = L => 0
        #else $B15 = getContributionAux(extension) * crit.getValueBy('k2_hourly') * param.getValueBy('sewer_contribution_rate_start') * calculation.extension / 10000
        print(' ')

    @staticmethod
    def strToFloat(str):
        return float(str) if len(str) > 0 else 0