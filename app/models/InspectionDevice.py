from PyQt5.QtSql import QSqlTableModel, QSqlQuery, QSqlRelationalTableModel
from PyQt5.QtCore import Qt, QLocale

class InspectionDevice(QSqlTableModel):
    
    def __init__(self, *args, **kwargs):        
        super(InspectionDevice, self).__init__(*args, **kwargs)        
        self.setTable("inspection_devices")
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.setSort(self.fieldIndex('id'), Qt.AscendingOrder)                        
        #headers
        self.locale = QLocale().name()
        self.language = self.locale[0:2] if self.locale[0:2] in ('en','es','pt') else 'en'
        if self.language == "es":
            self.setHeaderData(self.fieldIndex("type_es"), Qt.Horizontal, "Tipo")
            self.setHeaderData(self.fieldIndex("max_depth"), Qt.Horizontal, "Prof. máxima (m)")        
            self.setHeaderData(self.fieldIndex("max_diameter_suggested"), Qt.Horizontal, "DN Máximo (mm)")
        elif self.language == "pt":
            self.setHeaderData(self.fieldIndex("type_pt"), Qt.Horizontal, "Tipo")
            self.setHeaderData(self.fieldIndex("max_depth"), Qt.Horizontal, "Prof. máxima (m)")        
            self.setHeaderData(self.fieldIndex("max_diameter_suggested"), Qt.Horizontal, "DN Máximo (mm)")
        else:            
            self.setHeaderData(self.fieldIndex("type_en"), Qt.Horizontal, "Type")
            self.setHeaderData(self.fieldIndex("max_depth"), Qt.Horizontal, "Max Depth (m)")        
            self.setHeaderData(self.fieldIndex("max_diameter_suggested"), Qt.Horizontal, "Max DN Suggested(mm)")
        
        self.select()
    
    def getInspectionTypeUp(self, depthUp, adoptedDiameter):
        sql = "SELECT type_es, min(max_depth)\
                FROM inspection_devices\
                WHERE criteria_id in\
                    (SELECT project_criteria_id\
                    FROM parameters pa\
                    LEFT JOIN projects p on pa.id = p.parameter_id\
                    WHERE p.active)\
                AND {}<= max_depth\
                AND {}<= max_diameter_suggested".format(depthUp, adoptedDiameter)

        query = QSqlQuery(sql)
        if query.first():
            return query.value(0)
        else:
            return 0
