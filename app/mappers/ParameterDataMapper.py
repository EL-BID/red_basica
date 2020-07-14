from PyQt5.QtWidgets import QDataWidgetMapper

class ParameterDataMapper(QDataWidgetMapper):

    def map(self, ui):
            # project_criteria_id integer,\
            # layer_name text,\
            # contribution_sewage boolean,\
        model = self.model()
        self.addMapping(ui.beginningPopulationEdit, model.fieldIndex('beginning_population'))
        self.addMapping(ui.finalPopulationEdit, model.fieldIndex('final_population'))
        self.addMapping(ui.occupancyRateStartEdit, model.fieldIndex('occupancy_rate_start'))
        self.addMapping(ui.occupancyRateEndEdit, model.fieldIndex('occupancy_rate_end'))
        self.addMapping(ui.residencesStartEdit, model.fieldIndex('residences_start'))
        self.addMapping(ui.residencesEndEdit, model.fieldIndex('residences_end'))        
        self.addMapping(ui.connectionsStartEdit, model.fieldIndex('connections_start'))
        self.addMapping(ui.connectionsEndEdit, model.fieldIndex('connections_end'))
        self.addMapping(ui.pointFlowsStartEdit, model.fieldIndex('point_flows_start'))
        self.addMapping(ui.pointFlowsEndEdit, model.fieldIndex('point_flows_end'))
        self.addMapping(ui.qeReferenceMedEdit, model.fieldIndex('qe_reference_med'))
        self.addMapping(ui.qeReferenceMaxEdit, model.fieldIndex('qe_reference_max'))        
        #self.addMapping(ui., model.fieldIndex(''))  ver lo del radiobutton de contribution_sewage
        self.addMapping(ui.sewerContributionRateStartEdit, model.fieldIndex('sewer_contribution_rate_start'))
        self.addMapping(ui.sewerContributionRateEndEdit, model.fieldIndex('sewer_contribution_rate_end'))
        #Criteria Tab
        self.addMapping(ui.profileComboBox, model.fieldIndex('project_criteria_id'))
        