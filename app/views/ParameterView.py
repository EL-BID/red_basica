from PyQt5.QtWidgets import (QAbstractItemView, QDataWidgetMapper, QCompleter, QComboBox,
    QHeaderView, QDialog, QMessageBox)
from PyQt5.QtGui import QKeySequence
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlRelationalDelegate
from PyQt5.QtCore import Qt, pyqtSlot, QModelIndex

from ..models.Parameter import Parameter
from ..models.Criteria import Criteria
from .ui.ParameterDialogUi import Ui_NewParameterDialog

class ParameterView(QDialog, Ui_NewParameterDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.model = Parameter()
        model = QSqlRelationalTableModel(self.profileComboBox)        
        model.setTable("parameters")
        
        criteria_idx = model.fieldIndex("project_criteria_id")                
        model.setRelation(criteria_idx, QSqlRelation("project_criterias", "id", "name"))
        if not model.select():
            print(model.lastError())

        #Tab1
        self.profileComboBox.setModel(model.relationModel(criteria_idx))
        self.profileComboBox.setModelColumn(model.relationModel(criteria_idx).fieldIndex("name"))
                        
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel(model)  
        self.mapper.addMapping(self.beginningPopulationEdit, model.fieldIndex('beginning_population'))
        self.mapper.addMapping(self.finalPopulationEdit, model.fieldIndex('final_population'))
        self.mapper.addMapping(self.occupancyRateStartEdit, model.fieldIndex('occupancy_rate_start'))
        self.mapper.addMapping(self.occupancyRateEndEdit, model.fieldIndex('occupancy_rate_end'))
        self.mapper.addMapping(self.residencesStartEdit, model.fieldIndex('residences_start'))
        self.mapper.addMapping(self.residencesEndEdit, model.fieldIndex('residences_end'))        
        self.mapper.addMapping(self.connectionsStartEdit, model.fieldIndex('connections_start'))
        self.mapper.addMapping(self.connectionsEndEdit, model.fieldIndex('connections_end'))
        self.mapper.addMapping(self.pointFlowsStartEdit, model.fieldIndex('point_flows_start'))
        self.mapper.addMapping(self.pointFlowsEndEdit, model.fieldIndex('point_flows_end'))
        self.mapper.addMapping(self.qeReferenceMedEdit, model.fieldIndex('qe_reference_med'))
        self.mapper.addMapping(self.qeReferenceMaxEdit, model.fieldIndex('qe_reference_max'))               
        self.mapper.addMapping(self.sewerContributionRateStartEdit, model.fieldIndex('sewer_contribution_rate_start'))
        self.mapper.addMapping(self.sewerContributionRateEndEdit, model.fieldIndex('sewer_contribution_rate_end'))        
        self.mapper.addMapping(self.profileComboBox, criteria_idx)
        self.mapper.setItemDelegate(QSqlRelationalDelegate(self.profileComboBox))  
        self.mapper.toFirst()

        #Tab2
        self.mapper_criteria_profile = QDataWidgetMapper(self)
        criteriaModel = Criteria()
        self.mapper_criteria_profile.setModel(criteriaModel)
        
        self.mapper_criteria_profile.addMapping(self.profileName, criteriaModel.fieldIndex('name'))
        self.mapper_criteria_profile.addMapping(self.waterConsumptionPcSpinBox, criteriaModel.fieldIndex('water_consumption_pc'))
        self.mapper_criteria_profile.addMapping(self.k1DailySpinBox, criteriaModel.fieldIndex('k1_daily'))
        self.mapper_criteria_profile.addMapping(self.k2HourlySpinBox, criteriaModel.fieldIndex('k2_hourly'))
        self.mapper_criteria_profile.addMapping(self.coefficientReturnCSpinBox, criteriaModel.fieldIndex('coefficient_return_c'))
        self.mapper_criteria_profile.addMapping(self.intakeRateSpinBox, criteriaModel.fieldIndex('intake_rate'))
        self.mapper_criteria_profile.addMapping(self.avgTractiveForceSpinBox, criteriaModel.fieldIndex('avg_tractive_force_min'))
        self.mapper_criteria_profile.addMapping(self.flowMinQminSpinBox, criteriaModel.fieldIndex('flow_min_qmin'))
        self.mapper_criteria_profile.addMapping(self.waterSurfaceMaxSpinBox, criteriaModel.fieldIndex('water_surface_max'))
        self.mapper_criteria_profile.addMapping(self.maxWaterLevelSpinBox, criteriaModel.fieldIndex('max_water_level'))
        self.mapper_criteria_profile.addMapping(self.minDiameterLineEdit, criteriaModel.fieldIndex('min_diameter'))
        self.mapper_criteria_profile.addMapping(self.diameterUp150SpinBox, criteriaModel.fieldIndex('diameter_up_150'))
        self.mapper_criteria_profile.addMapping(self.diameterUp200SpinBox, criteriaModel.fieldIndex('diameter_up_200'))
        self.mapper_criteria_profile.addMapping(self.diameterUp250SpinBox, criteriaModel.fieldIndex('from_diameter_250'))
        self.mapper_criteria_profile.addMapping(self.coverMinStreetSpinBox, criteriaModel.fieldIndex('cover_min_street'))
        self.mapper_criteria_profile.addMapping(self.coverMinSidewalksGsSpinBox, criteriaModel.fieldIndex('cover_min_sidewalks_gs'))
        self.mapper_criteria_profile.addMapping(self.typePreferredHeadColSpinBox, criteriaModel.fieldIndex('type_preferred_head_col'))
        self.mapper_criteria_profile.addMapping(self.maxDropSpinBox, criteriaModel.fieldIndex('max_drop'))
        self.mapper_criteria_profile.addMapping(self.bottomIbMhSpinBox, criteriaModel.fieldIndex('bottom_ib_mh'))
        self.mapper_criteria_profile.toFirst()

        #Buttons
        self.buttonBox.accepted.connect(self.saveParameters)

    def saveParameters(self):
        self.mapper.submit()
        self.mapper_criteria_profile.submit()        