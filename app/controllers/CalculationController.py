from PyQt5.QtCore import QObject, pyqtSlot, Qt
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlQuery
from ..models.Calculation import Calculation
from ..models.Parameter import Parameter
from ..models.Project import Project
from ..models.Criteria import Criteria
from ..models.Contribution import Contribution
from ..models.WaterLevelAdj import WaterLevelAdj
from ..models.Pipe import Pipe
from ..models.InspectionDevice import InspectionDevice
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
        self.pipe = Pipe()
        self.inspectionoDevice = InspectionDevice()

    def importData(self, projectId):
        #TODO each time the parameter is changed, we have to import again? 
        if not self.checkFirstImport(projectId):
            start_time = time.time()
            self.uploadCalculations(projectId)
            print("Total time execution to calculations: --- %s seconds ---" % (time.time() - start_time))
            self.updateParameters()
            self.updateContributions(projectId)
            print("Total time execution to upload: --- %s seconds ---" % (time.time() - start_time))
        else:
            print('Its imported')

    def checkFirstImport(self, projectId):
        print('Checking if is imported')
        if projectId:
            imported = 0
            #TODO bind value is not working
            query = QSqlQuery("SELECT count(*)>0 FROM calculations WHERE project_id = "+str(projectId))
            while query.next():
                imported = query.value(0)
            return bool(imported)
        else:
            raise Exception("projectId is required to checkFirstImport")            
    
    def uploadCalculations(self, projectId):
        print('uploading..')
        #TODO put the progress dialog into the Data Controller
        data = DataController().getJsonData()
        for row in data:
            self.model.select()
            rec = self.model.record()
            rec.setValue('project_id',projectId)
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
                wlRec.setValue('previous_col_seg_end',row['TRM_(N-1)_A'])
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

    def updateContributions(self, projectId):        
        print('Updating Contributions')
        if projectId:      
            calIdx = self.contModel.fieldIndex("calculation_id")
            self.contModel.setRelation(calIdx, QSqlRelation("calculations", "id", "col_seg"))
            self.contModel.relationModel(calIdx).setFilter('calculations.project_id = {}'.format(projectId))
            self.model.setFilter('project_id = {}'.format(projectId))
            self.model.setFilter('initial_segment = 1')
            for i in range(self.model.rowCount()):
                self.model.select()
                colSeg = self.model.record(i).value('col_seg')
                if self.model.record(i).value('total_flow_rate_end') == None:
                    self.recursiveContributions(colSeg)
                if self.model.record(i).value('aux_depth_adjustment') == None: #TODO check if is the only way to know if is calculated
                    self.waterLevelAdjustments(colSeg)
        else:                    
            raise Exception("projectId is required to update contributions")                 
    
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
                flowQMin = self.critModel.getValueBy('flow_min_qmin')
                prjFlowRateQmax = 0 if (calc.value('collector_number')==None or totalFlowEnd == 0) else flowQMin if totalFlowEnd < flowQMin else totalFlowEnd
                calMod.setData(calMod.index(i, calMod.fieldIndex('prj_flow_rate_qgmax')), prjFlowRateQmax)
                initialFlowRateQi = 0 if (calc.value('collector_number')==None or totalFlowStart == 0) else flowQMin if totalFlowStart < flowQMin else totalFlowStart
                calMod.setData(calMod.index(i, calMod.fieldIndex('initial_flow_rate_qi')), initialFlowRateQi)
                adoptedDiameter = self.critModel.getValueBy('min_diameter') if calc.value('initial_segment') == 1 else calMod.getValueBy('adopted_diameter', 'col_seg = "{}"'.format(calc.value('previous_col_seg_id')))
                calMod.setData(calMod.index(i, calMod.fieldIndex('adopted_diameter')), adoptedDiameter)
                slopesMinAccepted = 0 if calc.value('extension') == 0 else self.slopesMinAcceptedCalc(adoptedDiameter)
                calMod.setData(calMod.index(i, calMod.fieldIndex('slopes_min_accepted_col')), slopesMinAccepted)
                cManning = 0 if (calc.value('extension') == 0 or calc.value('collector_number') == 0) else self.pipe.getValueBy('manning_adopted',"diameter ='{}'".format(adoptedDiameter))
                calMod.setData(calMod.index(i, calMod.fieldIndex('c_manning')), cManning)
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

    #TODO check if is universal and ask what happen btw 200 and 250s
    def slopesMinAcceptedCalc(self, adoptedDiameter):
        if (adoptedDiameter <= 150): 
            return self.critModel.getValueBy('diameter_up_150')
        if (adoptedDiameter <= 200):
            return  self.critModel.getValueBy('diameter_up_200')
        if (adoptedDiameter >= 250):
            return  self.critModel.getValueBy('from_diameter_250')


    @staticmethod
    def strToFloat(str):
        return float(str) if len(str) > 0 else 0

    def waterLevelAdjustments(self, colSeg):
        calMod = Calculation()
        wlMod = WaterLevelAdj()
        splitCol = colSeg.split('-')
        wlMod.setFilter('col_seg like "{}-%"'.format(splitCol[0]))
        calMod.setFilter('col_seg like "{}-%"'.format(splitCol[0]))
        wlMod.select()
        calMod.select()
        for i in range(wlMod.rowCount()):
            wlMod.select()
            calMod.select()
            calc = calMod.record(i)
            wl = wlMod.record(i)

            m1ColDepth = m2ColDepth = m1ColCov = m2ColCov = m1ColUp = m2ColUp = m1ColNa = m2ColNa = 0
            if len(wl.value('m1_col_id'))>0:
                self.waterLevelAdjustments(wl.value('m1_col_id'))
                wlMod.select()
                m1ColDepth = wlMod.getValueBy('down_end_h',"w.col_seg ='{}'".format(wl.value('m1_col_id')))
                wlMod.setData(wlMod.index(i, wlMod.fieldIndex('m1_col_depth')), m1ColDepth)
                m1ColCov = wlMod.getValueBy('down_end_cov',"w.col_seg ='{}'".format(wl.value('m1_col_id')))
                wlMod.setData(wlMod.index(i, wlMod.fieldIndex('m1_col_cov')), m1ColCov)
                m1ColUp = calMod.getValueBy('el_col_down',"col_seg = '{}'".format(calc.value('m1_col_id')))
                wlMod.setData(wlMod.index(i, wlMod.fieldIndex('m1_col_up')), m1ColUp)
                m1ColNa = wlMod.getValueBy('down_side_seg',"w.col_seg = '{}'".format(calc.value('m1_col_id')))
                wlMod.setData(wlMod.index(i, wlMod.fieldIndex('m1_col_na')), m1ColNa)

            if len(wl.value('m2_col_id'))>0:
                self.waterLevelAdjustments(wl.value('m2_col_id'))
                wlMod.select()
                m2ColDepth = wlMod.getValueBy('down_end_h',"w.col_seg ='{}'".format(wl.value('m2_col_id')))
                wlMod.setData(wlMod.index(i, wlMod.fieldIndex('m2_col_depth')), m2ColDepth)
                m2ColCov = wlMod.getValueBy('down_end_cov',"w.col_seg ='{}'".format(wl.value('m2_col_id')))
                wlMod.setData(wlMod.index(i, wlMod.fieldIndex('m2_col_cov')), m2ColCov)
                m2ColUp = calMod.getValueBy('el_col_down',"col_seg = '{}'".format(calc.value('m2_col_id')))
                wlMod.setData(wlMod.index(i, wlMod.fieldIndex('m2_col_up')), m2ColUp)
                m2ColNa = wlMod.getValueBy('down_side_seg',"col_seg = '{}'".format(calc.value('m2_col_id')))
                wlMod.setData(wlMod.index(i, wlMod.fieldIndex('m2_col_na')), m2ColNa)

            extension = calc.value('extension')
            prevDepthDown = calMod.getValueBy('depth_down',"col_seg = '{}'".format(calc.value('previous_col_seg_id')))
            amtSegDepth = prevDepthDown if (calc.value('initial_segment') != 1 and extension > 0) else 0
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('amt_seg_depth')), amtSegDepth)
            greaterDepth = max(m1ColDepth, m2ColDepth, amtSegDepth)
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('greater_depth')), greaterDepth)
            depthUp = self.calcDepthUp(calc, wl, greaterDepth)
            calMod.setData(calMod.index(i, calMod.fieldIndex('depth_up')), depthUp)
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('insp_dev_h_out')), depthUp)
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('calc_depth_up')), depthUp) 
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('imp_depth_up')), depthUp) #TODO AE.A15
            calMod.setData(calMod.index(i, calMod.fieldIndex('aux_depth_adjustment')), depthUp)
            adoptedDiameter = calc.value('adopted_diameter')
            coveringUp = depthUp - adoptedDiameter / 1000
            calMod.setData(calMod.index(i, calMod.fieldIndex('covering_up')), coveringUp)
            elColUp = (calc.value('el_terr_up') - depthUp) if (extension != 0 or calc.value('collector_number') != 0) else 0
            calMod.setData(calMod.index(i, calMod.fieldIndex('el_col_up')), elColUp)

            depthDown = self.calcDepthDown(calc, wl, elColUp)
            coveringDown = round(depthDown,2) - adoptedDiameter/1000
            calMod.setData(calMod.index(i, calMod.fieldIndex('covering_down')), coveringDown)
            calMod.setData(calMod.index(i, calMod.fieldIndex('depth_down')), round(depthDown,2))
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('down_end_h')), round(depthDown,2))
            elColDown = (calc.value('el_terr_down') - depthDown) if (extension != 0 or calc.value('collector_number') != 0) else 0
            calMod.setData(calMod.index(i, calMod.fieldIndex('el_col_down')), round(elColDown,2))
            elTopGenUp =  (calc.value('el_terr_up') - coveringUp) if (extension != 0 or calc.value('collector_number') != 0) else 0
            calMod.setData(calMod.index(i, calMod.fieldIndex('el_top_gen_up')), elTopGenUp)
            elTopGenDown =  (calc.value('el_terr_down') - coveringDown) if (extension != 0 or calc.value('collector_number') != 0) else 0
            calMod.setData(calMod.index(i, calMod.fieldIndex('el_top_gen_down')), elTopGenDown)
            slopesAdoptedCol =  (elTopGenUp-elTopGenDown)/extension if (extension != 0 or calc.value('collector_number') != 0) else 0
            calMod.setData(calMod.index(i, calMod.fieldIndex('slopes_adopted_col')), round(slopesAdoptedCol, 5))

            dn1mm = calMod.dn1mm(calc.value('prj_flow_rate_qgmax'), round(slopesAdoptedCol, 5), calc.value('c_manning'), self.critModel.getValueBy('max_water_level'))
            diam1 = self.critModel.getValueBy('min_diameter') if dn1mm < self.critModel.getValueBy('min_diameter') else self.pipe.getMinDiameter(dn1mm)
            calMod.setData(calMod.index(i, calMod.fieldIndex('suggested_diameter')), diam1)

            waterLevelY = 0 if calc.value('collector_number') == 0 or calc.value('extension') == 0 else calMod.laminaabs(calc.value('prj_flow_rate_qgmax'), adoptedDiameter, slopesAdoptedCol, calc.value('c_manning'))
            calMod.setData(calMod.index(i, calMod.fieldIndex('water_level_y')), round(waterLevelY, 2))
            waterLevelPipeEnd = 0 if calc.value('collector_number') == 0 or calc.value('extension') == 0 else calMod.laminarel(calc.value('prj_flow_rate_qgmax'), adoptedDiameter, slopesAdoptedCol, calc.value('c_manning'))
            calMod.setData(calMod.index(i, calMod.fieldIndex('water_level_pipe_end')), round(waterLevelPipeEnd, 2)*100)
            flowQMin= self.critModel.getValueBy('flow_min_qmin')
            totalFlowRateEnd = calc.value('total_flow_rate_end')
            trForceQls = flowQMin if totalFlowRateEnd / self.critModel.getValueBy('k2_hourly') < flowQMin else totalFlowRateEnd
            tractiveForce = 0 if calc.value('collector_number') == 0 or calc.value('extension') == 0 else calMod.tenstrat(trForceQls, adoptedDiameter, slopesAdoptedCol, calc.value('c_manning'))
            calMod.setData(calMod.index(i, calMod.fieldIndex('tractive_force')), round(tractiveForce, 2))
            criticalVelocity = 0 if calc.value('collector_number') == 0 or calc.value('extension') == 0 else calMod.velocrit(calc.value('prj_flow_rate_qgmax'), adoptedDiameter, slopesAdoptedCol, calc.value('c_manning'))
            calMod.setData(calMod.index(i, calMod.fieldIndex('critical_velocity')), round(criticalVelocity, 2))
            velocity = 0 if calc.value('collector_number') == 0 or calc.value('extension') == 0 else calMod.velocid(calc.value('prj_flow_rate_qgmax'), adoptedDiameter, slopesAdoptedCol, calc.value('c_manning'))
            calMod.setData(calMod.index(i, calMod.fieldIndex('velocity')), round(velocity, 2))
            waterLevelYStart = 0 if calc.value('collector_number') == 0 or calc.value('extension') == 0 else calMod.laminaabs(calc.value('initial_flow_rate_qi'), adoptedDiameter, slopesAdoptedCol, calc.value('c_manning'))
            calMod.setData(calMod.index(i, calMod.fieldIndex('water_level_y_start')), round(waterLevelYStart, 2))
            waterLevelPipeStart = 0 if calc.value('collector_number') == 0 or calc.value('extension') == 0 else calMod.laminarel(calc.value('initial_flow_rate_qi'), adoptedDiameter, slopesAdoptedCol, calc.value('c_manning'))
            calMod.setData(calMod.index(i, calMod.fieldIndex('water_level_pipe_start')), round(waterLevelPipeStart, 2)*100)
            totalFlowRateStart = calc.value('total_flow_rate_start')
            trForceStartQls = flowQMin if totalFlowRateStart / self.critModel.getValueBy('k2_hourly') < flowQMin else totalFlowRateStart
            tractiveForceStart = 0 if calc.value('collector_number') == 0 or calc.value('extension') == 0 else calMod.tenstrat(trForceStartQls, adoptedDiameter, slopesAdoptedCol, calc.value('c_manning'))
            calMod.setData(calMod.index(i, calMod.fieldIndex('tractive_force_start')), round(tractiveForceStart, 2))

            prevCoveringDown = calMod.getValueBy('covering_down',"col_seg = '{}'".format(calc.value('previous_col_seg_id')))
            amtSegCov = prevCoveringDown if (calc.value('initial_segment') != 1 and extension > 0) else 0
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('amt_seg_cov')), amtSegCov)
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('insp_dev_cov_out')), round(coveringUp,2))
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('down_end_cov')), round(coveringDown,2))
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('greater_cov')), max(m1ColCov, m2ColCov, amtSegCov))
            forceDepthUp = 0 if calc.value('force_depth_up')==None else calc.value('force_depth_up')
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('force_depth')), forceDepthUp)
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('aux_ini')), calc.value('initial_segment'))

            elColDownPrevious = calMod.getValueBy('el_col_down',"col_seg = '{}'".format(calc.value('previous_col_seg_id')))
            amtSegUp = 0 if elColDownPrevious == None else elColDownPrevious
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('amt_seg_up')), amtSegUp)
            lowestUp = 0 if amtSegUp == 0 and m1ColUp == 0 and m2ColUp == 0 else min(i for i in [amtSegUp, m1ColUp, m2ColUp] if i > 0)
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('lowest_up')), lowestUp)
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('insp_dev_cov_up')), elColUp)
            upDiffNeeded = 0 if amtSegUp == 0 else round(elColUp - lowestUp + self.critModel.getValueBy('bottom_ib_mh'), 2) if elColUp - lowestUp > (self.critModel.getValueBy('bottom_ib_mh') * -1) else 0
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('up_diff_needed')), upDiffNeeded)
            #$A3.H15
            upstreamSideSeg = 0 if calc.value('extension') == 0 or (elColUp + waterLevelY) < 0 else elColUp + waterLevelY
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('up_side_seg')), round(upstreamSideSeg,2))
            #$A3.I15
            downstreamSideSeg = 0 if calc.value('extension') == 0 or (elColDown + waterLevelY) < 0 else elColDown + waterLevelY
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('down_side_seg')), round(downstreamSideSeg, 2))
            downSidePrev = wlMod.getValueBy('down_side_seg',"w.col_seg = '{}'".format(calc.value('previous_col_seg_id')))
            amtSegNa = 0 if downSidePrev == None or downSidePrev < 0 else downSidePrev
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('amt_seg_na')), amtSegNa)
            naDeeper = 0 if amtSegNa == 0 and m1ColNa == 0 and m2ColNa == 0 else min(i for i in [amtSegNa, m1ColNa, m2ColNa] if i > 0)
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('na_deeper')), naDeeper)
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('insp_dev_cov_na')), upstreamSideSeg)
            naDiffNeeded = 0 if amtSegNa == 0 else round(upstreamSideSeg - naDeeper, 2) if (upstreamSideSeg - naDeeper) > 0 else 0
            wlMod.setData(wlMod.index(i, wlMod.fieldIndex('na_diff_needed')), naDiffNeeded)
            calMod.setData(calMod.index(i, calMod.fieldIndex('inspection_type_up')), self.inspectionoDevice.getInspectionTypeUp(depthUp, adoptedDiameter))
            calMod.updateRowInTable(i, calMod.record(i))
            wlMod.updateRowInTable(i, wlMod.record(i))

        for i in range(calMod.rowCount()):
            calMod.select()
            calc = calMod.record(i)
            inspectionTypeUp = calMod.getValueBy('inspection_type_up',"col_seg ='{}'".format(calc.value('downstream_seg_id')))
            insTypeDown = inspectionTypeUp if inspectionTypeUp != None else calc.value('inspection_type_up')
            calMod.setData(calMod.index(i, calMod.fieldIndex('inspection_type_down')), insTypeDown)
            calMod.updateRowInTable(i, calMod.record(i))

    # $RedBasica.$V$15
    def calcDepthUp(self, calc, wl, greaterDepth):
        if (calc.value('initial_segment') == 1):
            if (calc.value('force_depth_up') == None):
                if (calc.value('col_pipe_position') == 1):
                    return self.critModel.getValueBy('cover_min_sidewalks_gs') + calc.value('adopted_diameter') / 1000
                else:
                    return self.critModel.getValueBy('cover_min_street') + calc.value('adopted_diameter') / 1000
            else:
                return calc.value('force_depth_up')
        else:
            bottomIbMh = self.critModel.getValueBy('bottom_ib_mh')
            if (calc.value('force_depth_up') == None):
                x = (self.critModel.getValueBy('cover_min_sidewalks_gs') + bottomIbMh + (calc.value('adopted_diameter')/1000)) if calc.value('col_pipe_position') == 1 else (self.critModel.getValueBy('cover_min_street') + bottomIbMh + (calc.value('adopted_diameter')/1000))
                return max((greaterDepth + bottomIbMh), calc.value('aux_depth_adjustment'), x)
            else:
                return max((greaterDepth + bottomIbMh), calc.value('force_depth_up'))
    
    # $RedBasica.$W$15 depth_down
    def calcDepthDown(self, calc, wl, elColUp):
        extension = calc.value('extension')
        if extension == 0:
            return 0
        else:
            forceDepthDown = calc.value('force_depth_down')
            y = 0 if forceDepthDown == None else forceDepthDown
            elTerrDown = calc.value('el_terr_down')
            slopesMinAccepted = calc.value('slopes_min_accepted_col')
            a = elTerrDown - (elColUp - slopesMinAccepted * extension)
            #TODO ask to Leonardo 'cause this conditions everything is true
            if  y >= 0:
                if (forceDepthDown == None):
                    coverMinSidewalks = self.critModel.getValueBy('cover_min_sidewalks_gs')
                    coverMinStreet = self.critModel.getValueBy('cover_min_street')
                    adoptedDiameter = calc.value('adopted_diameter')
                    b = coverMinSidewalks + adoptedDiameter / 1000 if calc.value('col_pipe_position') == 1 else coverMinStreet + adoptedDiameter / 1000
                    return max(a,b)
                else:
                    return max(a, forceDepthDown)
            else: 
                if (forceDepthDown == None):
                    return a
                else:
                    max(a, forceDepthDown)
