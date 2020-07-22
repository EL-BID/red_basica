from PyQt5.QtWidgets import (QAbstractItemView, QDataWidgetMapper, QCompleter, QComboBox,
    QHeaderView, QDialog, QMessageBox)
from PyQt5.QtGui import QKeySequence
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlRelationalDelegate
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QModelIndex

from ..models.Parameter import Parameter
from ..models.Project import Project
from ..models.Criteria import Criteria
from .ui.ParameterDialogUi import Ui_NewParameterDialog

class ParameterView(QDialog, Ui_NewParameterDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.parameterId = None
        
        #ParameterModel               
        self.parameterModel = QSqlRelationalTableModel(self.profileComboBox)        
        self.parameterModel.setTable("parameters")
               
        criteria_idx = self.parameterModel.fieldIndex("project_criteria_id")                
        self.parameterModel.setRelation(criteria_idx, QSqlRelation("project_criterias", "id", "name"))         

        if not self.parameterModel.select():
            print(self.parameterModel.lastError().text())

        #Tab1
        self.profileComboBox.setModel(self.parameterModel.relationModel(criteria_idx))
        self.profileComboBox.setModelColumn(self.parameterModel.relationModel(criteria_idx).fieldIndex("name"))
                        
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel(self.parameterModel)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.AutoSubmit)
        self.mapper.addMapping(self.beginningPopulationEdit, self.parameterModel.fieldIndex('beginning_population'))
        self.mapper.addMapping(self.finalPopulationEdit, self.parameterModel.fieldIndex('final_population'))
        self.mapper.addMapping(self.occupancyRateStartEdit, self.parameterModel.fieldIndex('occupancy_rate_start'))
        self.mapper.addMapping(self.occupancyRateEndEdit, self.parameterModel.fieldIndex('occupancy_rate_end'))
        self.mapper.addMapping(self.residencesStartEdit, self.parameterModel.fieldIndex('residences_start'))
        self.mapper.addMapping(self.residencesEndEdit, self.parameterModel.fieldIndex('residences_end'))        
        self.mapper.addMapping(self.connectionsStartEdit, self.parameterModel.fieldIndex('connections_start'))
        self.mapper.addMapping(self.connectionsEndEdit, self.parameterModel.fieldIndex('connections_end'))
        self.mapper.addMapping(self.pointFlowsStartEdit, self.parameterModel.fieldIndex('point_flows_start'))
        self.mapper.addMapping(self.pointFlowsEndEdit, self.parameterModel.fieldIndex('point_flows_end'))
        self.mapper.addMapping(self.qeReferenceMedEdit, self.parameterModel.fieldIndex('qe_reference_med'))
        self.mapper.addMapping(self.qeReferenceMaxEdit, self.parameterModel.fieldIndex('qe_reference_max'))               
        self.mapper.addMapping(self.sewerContributionRateStartEdit, self.parameterModel.fieldIndex('sewer_contribution_rate_start'))
        self.mapper.addMapping(self.sewerContributionRateEndEdit, self.parameterModel.fieldIndex('sewer_contribution_rate_end'))        
        self.mapper.addMapping(self.profileComboBox, criteria_idx)
        self.mapper.setItemDelegate(QSqlRelationalDelegate(self.profileComboBox))                 
                
        #Tab2
        self.currentCriteriaIdx = None
        self.mapper_criteria_profile = QDataWidgetMapper(self)
        self.criteriaModel = Criteria()
        self.mapper_criteria_profile.setModel(self.criteriaModel)
        
        self.mapper_criteria_profile.addMapping(self.profileName, self.criteriaModel.fieldIndex('name'))
        self.mapper_criteria_profile.addMapping(self.waterConsumptionPcSpinBox, self.criteriaModel.fieldIndex('water_consumption_pc'))
        self.mapper_criteria_profile.addMapping(self.k1DailySpinBox, self.criteriaModel.fieldIndex('k1_daily'))
        self.mapper_criteria_profile.addMapping(self.k2HourlySpinBox, self.criteriaModel.fieldIndex('k2_hourly'))
        self.mapper_criteria_profile.addMapping(self.coefficientReturnCSpinBox, self.criteriaModel.fieldIndex('coefficient_return_c'))
        self.mapper_criteria_profile.addMapping(self.intakeRateSpinBox, self.criteriaModel.fieldIndex('intake_rate'))
        self.mapper_criteria_profile.addMapping(self.avgTractiveForceSpinBox, self.criteriaModel.fieldIndex('avg_tractive_force_min'))
        self.mapper_criteria_profile.addMapping(self.flowMinQminSpinBox, self.criteriaModel.fieldIndex('flow_min_qmin'))
        self.mapper_criteria_profile.addMapping(self.waterSurfaceMaxSpinBox, self.criteriaModel.fieldIndex('water_surface_max'))
        self.mapper_criteria_profile.addMapping(self.maxWaterLevelSpinBox, self.criteriaModel.fieldIndex('max_water_level'))
        self.mapper_criteria_profile.addMapping(self.minDiameterLineEdit, self.criteriaModel.fieldIndex('min_diameter'))
        self.mapper_criteria_profile.addMapping(self.diameterUp150SpinBox, self.criteriaModel.fieldIndex('diameter_up_150'))
        self.mapper_criteria_profile.addMapping(self.diameterUp200SpinBox, self.criteriaModel.fieldIndex('diameter_up_200'))
        self.mapper_criteria_profile.addMapping(self.diameterUp250SpinBox, self.criteriaModel.fieldIndex('from_diameter_250'))
        self.mapper_criteria_profile.addMapping(self.coverMinStreetSpinBox, self.criteriaModel.fieldIndex('cover_min_street'))
        self.mapper_criteria_profile.addMapping(self.coverMinSidewalksGsSpinBox, self.criteriaModel.fieldIndex('cover_min_sidewalks_gs'))
        self.mapper_criteria_profile.addMapping(self.typePreferredHeadColSpinBox, self.criteriaModel.fieldIndex('type_preferred_head_col'))
        self.mapper_criteria_profile.addMapping(self.maxDropSpinBox, self.criteriaModel.fieldIndex('max_drop'))
        self.mapper_criteria_profile.addMapping(self.bottomIbMhSpinBox, self.criteriaModel.fieldIndex('bottom_ib_mh'))
        

        #conections
        self.profileComboBox.currentIndexChanged.connect(self.onProfileChange)
        self.buttonBox.accepted.connect(self.saveParameters)
    

    def onProfileChange(self, i):        
        self.currentCriteriaIdx = i
        self.loadProfile()      

    def loadProfile(self):
        if self.currentCriteriaIdx:            
            self.mapper_criteria_profile.setCurrentIndex(self.currentCriteriaIdx)
        else:            
            self.mapper_criteria_profile.toFirst()

    def showEvent(self, event):        
        self.parameterId = Project.getActiveProjectParameter()
        if self.parameterId:
            self.parameterModel.setFilter("parameters.id = {}".format(self.parameterId))            
            self.mapper.toFirst() #onProfileChange is trigered by this
        else:
            self.addParameterRecord()
            self.loadProfile()

    def addParameterRecord(self):
        row = self.parameterModel.rowCount()
        self.mapper.submit()
        self.parameterModel.insertRow(row)
        self.mapper.setCurrentIndex(row)
        self.profileComboBox.setCurrentIndex(0)

    def saveParameters(self):
        self.mapper.submit()
        self.mapper_criteria_profile.submit()
        if not self.parameterId:
            self.parameterId = self.parameterModel.query().lastInsertId()
            Project.setParameterToActive(self.parameterId)