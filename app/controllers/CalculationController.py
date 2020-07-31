from PyQt5.QtCore import QObject, pyqtSlot, Qt
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlQuery
from ..models.Calculation import Calculation
from ..models.Parameter import Parameter
from ..models.Project import Project
from ..models.Criteria import Criteria
from ..models.Contribution import Contribution
from ..models.WaterLevelAdj import WaterLevelAdj
from .DataController import DataController
import time

class CalculationController(QObject):
    def __init__(self):
        super().__init__()
        self.model = Calculation()
        self.parameterModel = Parameter()
        self.critModel = Criteria()
        self.contModel = Contribution()
        self.projModel = Project()
        self.wlAdj = WaterLevelAdj()

    def importData(self, projectId):
        #TODO each time the parameter is changed, we have to import again? 
        if not self.checkFirstImport(projectId):
            start_time = time.time()
            self.uploadCalculations()
            self.updateParameters()
            self.updateContributions()
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
            rec.setValue('project_id',1) #TODO set active project.
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
            slopesTerr = 0 if (float(row['L']) == 0 or row['ID_COL'] == None) else round((float(row['COTA_I']) - float(row['COTA_F'])) / float(row['L']), 4)
            rec.setValue('slopes_terr',slopesTerr)
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

                wlRec = self.wlAdj.record()
                wlRec.setValue('calculation_id', self.model.query().lastInsertId())
                wlRec.setValue('col_seg',row['ID_TRM_(N)'])
                wlRec.setValue('previous_col_seg_id',row['TRM_(N-1)_A'])
                wlRec.setValue('m1_col_id',row['TRM_(N-1)_B'])
                wlRec.setValue('m2_col_id',row['TRM_(N-1)_C'])
                wlRow = self.wlAdj.rowCount()
                self.wlAdj.insertRecord(wlRow, wlRec)


    # When the calculations have been loaded, the missing parameters are generated
    def updateParameters(self):
        print('Updating Parameters')
        self.parameterModel.select()
        #TODO check if save on current project
        row = self.projModel.getActiveProjectParameter() - 1
        contributionSewage = self.parameterModel.getValueBy('contribution_sewage')
        sewerContEnd = self.avgLinearContributionRate(0) if contributionSewage > 0 else 0
        sewerContStart = self.avgLinearContributionRate(1) if contributionSewage > 0 else 0
        self.parameterModel.setData(self.parameterModel.index(row, self.parameterModel.fieldIndex("point_flows_end")), self.model.getQtyFinalQeSum(), Qt.EditRole)
        self.parameterModel.setData(self.parameterModel.index(row, self.parameterModel.fieldIndex("point_flows_start")), self.model.getQtyInitialQeSum(), Qt.EditRole)
        self.parameterModel.setData(self.parameterModel.index(row, self.parameterModel.fieldIndex("sewer_contribution_rate_end")), sewerContEnd, Qt.EditRole)
        self.parameterModel.setData(self.parameterModel.index(row, self.parameterModel.fieldIndex("sewer_contribution_rate_start")), sewerContStart, Qt.EditRole)
        self.parameterModel.updateRowInTable(row, self.parameterModel.record(row))

    def updateContributions(self, colSeg=None):
        print('Updating Contributions')
        project_id = self.projModel.getActiveId()
        calIdx = self.contModel.fieldIndex("calculation_id")
        self.contModel.setRelation(calIdx, QSqlRelation("calculations", "id", "col_seg"))
        self.contModel.relationModel(calIdx).setFilter('calculations.project_id = {}'.format(project_id))
        self.model.setFilter('project_id = {}'.format(project_id))
        self.model.setFilter('initial_segment = 1')
        for i in range(self.model.rowCount()):
            self.model.select()
            if self.model.record(i).value('total_flow_rate_end') == None:
                colSeg = self.model.record(i).value('col_seg')
                self.recursiveContributions(colSeg)
    
    def recursiveContributions(self, colSeg):
        calMod = Calculation()
        conMod = Contribution()
        splitCol = colSeg.split('-')
        conMod.setFilter('col_seg like "{}-%"'.format(splitCol[0]))
        calMod.setFilter('col_seg like "{}-%"'.format(splitCol[0]))
        calMod.select()
        conMod.select()
        for i in range(conMod.rowCount()):
            calMod.select()
            conMod.select()
            calc = calMod.record(i)
            con = conMod.record(i)
            prevEnd = calMod.getTotalFlowEndByColSeg(calc.value('previous_col_seg_id'))
            conMod.setData(conMod.index(i, conMod.fieldIndex('previous_col_seg_end')), prevEnd)
            prevStart = calMod.getTotalFlowStartByColSeg(calc.value('previous_col_seg_id'))
            conMod.setData(conMod.index(i, conMod.fieldIndex('previous_col_seg_start')), prevStart)
            m1End = 0
            m1Start = 0
            if calc.value('m1_col_id'):
                self.recursiveContributions(calc.value('m1_col_id'))
                calMod.select()
                m1End = calMod.getTotalFlowEndByColSeg(calc.value('m1_col_id'))
                conMod.setData(conMod.index(i, conMod.fieldIndex('col_pipe_m1_end')), m1End)
                m1Start = calMod.getTotalFlowStartByColSeg(calc.value('m1_col_id'))
                conMod.setData(conMod.index(i, conMod.fieldIndex('col_pipe_m1_start')), m1Start)
            m2End = 0
            m2Start = 0
            if calc.value('m2_col_id'):
                self.recursiveContributions(calc.value('m2_col_id'))
                calMod.select()
                m2End = calMod.getTotalFlowEndByColSeg(calc.value('m2_col_id'))
                conMod.setData(conMod.index(i, conMod.fieldIndex('col_pipe_m2_end')), m2End)
                m2Start = calMod.getTotalFlowStartByColSeg(calc.value('m2_col_id'))
                conMod.setData(conMod.index(i, conMod.fieldIndex('col_pipe_m2_start')), m2Start)
            conMod.setData(conMod.index(i, conMod.fieldIndex('subtotal_up_seg_end')), (prevEnd + m1End + m2End))
            conMod.setData(conMod.index(i, conMod.fieldIndex('subtotal_up_seg_start')), (prevStart + m1Start + m2Start))
            if conMod.updateRowInTable(i, conMod.record(i)):
                linearContEnd = con.value('linear_contr_seg_end') if con.value('linear_contr_seg_end') != None else 0
                totalFlowEnd = round(calc.value('intake_in_seg') + (prevEnd + m1End + m2End) + con.value('condominial_lines_end') + linearContEnd, 2)
                calMod.setData(calMod.index(i, calMod.fieldIndex('total_flow_rate_end')), totalFlowEnd)
                linearContStart = con.value('linear_contr_seg_start') if con.value('linear_contr_seg_start') != None else 0
                totalFlowStart = round(calc.value('intake_in_seg') + (prevStart + m1Start + m2Start) + con.value('condominial_lines_start') + linearContStart, 2)
                calMod.setData(calMod.index(i, calMod.fieldIndex('total_flow_rate_start')), totalFlowStart)
                calMod.updateRowInTable(i, calMod.record(i))

    # $Parametros.$L$24 || Getting Maximum Flow l/s
    def getMaximumFlow(self):
        return round(self.parameterModel.getValueBy('qe_reference_max'), 4)

    # $Parametros.$L$38 or$ Parametros.$L$40 || Average Linear Contribution Rate (l/s.km) start boolean
    def avgLinearContributionRate(self, start):
        extensionSum = self.model.getExtensionSum()
        if extensionSum == 0:
            return 0
        population = self.parameterModel.getValueBy('beginning_population') if start else self.parameterModel.getValueBy('final_population')
        x = self.critModel.getValueBy('water_consumption_pc * pc.coefficient_return_c')
        return round((population * x / 86400)/extensionSum*1000, 3)

    # $A1.$B$1
    def getContributionAux(self, extension):
        contributionSewage = self.parameterModel.getValueBy('contribution_sewage')
        return 0 if (contributionSewage == 0 or extension == 0 ) else 1

    # $A1.$M$1 || Condominial Lines and Others START (l/s)
    def getCondominialLinesStart(self, qeIp):
        qeIp = self.strToFloat(qeIp)
        return round(qeIp * self.getMaximumFlow() / self.critModel.getValueBy('k1_daily'), 2)

    # $A1.$H$1 END-Linear Contribution in Segment (l/s)
    def getEndLinearContInSeg(self, ext):
        if ext == 0:
            return 0
        else:
            return ((self.getContributionAux(ext) * self.critModel.getValueBy('k1_daily') * self.critModel.getValueBy('k2_hourly') * self.parameterModel.getValueBy('sewer_contribution_rate_end') * ext) / 1000)

    # $A1.$N$1 START-Linear Contribution in Segment (l/s)
    def getStartLinearContInSeg(self, ext):
        if ext == 0:
            return 0
        else:
            return ((self.getContributionAux(ext) * self.critModel.getValueBy('k2_hourly') * self.parameterModel.getValueBy('sewer_contribution_rate_start') * ext) / 1000)

    @staticmethod
    def strToFloat(str):
        return float(str) if len(str) > 0 else 0