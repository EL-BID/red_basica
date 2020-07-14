from PyQt5.QtWidgets import QDataWidgetMapper

class CriteriaDataMapper(QDataWidgetMapper):

    def map(self, ui):
        model = self.model()
        self.addMapping(ui.profileName, model.fieldIndex('name'))
        self.addMapping(ui.waterConsumptionPcSpinBox, model.fieldIndex('water_consumption_pc'))
        self.addMapping(ui.k1DailySpinBox, model.fieldIndex('k1_daily'))
        self.addMapping(ui.k2HourlySpinBox, model.fieldIndex('k2_hourly'))
        self.addMapping(ui.coefficientReturnCSpinBox, model.fieldIndex('coefficient_return_c'))
        self.addMapping(ui.intakeRateSpinBox, model.fieldIndex('intake_rate'))
        self.addMapping(ui.avgTractiveForceSpinBox, model.fieldIndex('avg_tractive_force_min'))
        self.addMapping(ui.flowMinQminSpinBox, model.fieldIndex('flow_min_qmin'))
        self.addMapping(ui.waterSurfaceMaxSpinBox, model.fieldIndex('water_surface_max'))
        self.addMapping(ui.maxWaterLevelSpinBox, model.fieldIndex('max_water_level'))
        self.addMapping(ui.minDiameterLineEdit, model.fieldIndex('min_diameter'))
        # self.addMapping(ui., model.fieldIndex('diameter_up_150'))
        # self.addMapping(ui., model.fieldIndex('diameter_up_200'))
        # self.addMapping(ui., model.fieldIndex('from_diameter_250'))
        # self.addMapping(ui., model.fieldIndex('cover_min_street'))
        # self.addMapping(ui., model.fieldIndex('cover_min_sidewalks_gs'))
        # self.addMapping(ui., model.fieldIndex('type_preferred_head_col'))
        # self.addMapping(ui., model.fieldIndex('max_drop double'))
        # self.addMapping(ui., model.fieldIndex('bottom_ib_mh'))