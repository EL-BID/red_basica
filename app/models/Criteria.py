from PyQt5.QtCore import pyqtSignal, QModelIndex, QDateTime
from PyQt5.QtSql import QSqlTableModel, QSqlRelationalTableModel, QSqlQuery
from PyQt5.QtCore import Qt

class Criteria(QSqlTableModel):
    
    def __init__(self, *args, **kwargs):        
        super(Criteria, self).__init__(*args, **kwargs)
        self.setTable("project_criterias")
        self.setSort(self.fieldIndex('id'), Qt.AscendingOrder)
        self.select()

    # @staticmethod
    # def copyPipesFromTo(_from, _to):
    #     query = QSqlQuery()
    #     query.prepare("INSERT INTO pipes \
    #                     (criteria_id, diameter, material_id, manning_suggested, manning_adopted)\
    #                     select :to, diameter, material_id, manning_suggested, manning_adopted from pipes\
    #                     where criteria_id = :from")
    #     query.bindValue(":to", _to)
    #     query.bindValue(":from", _from)
    #     query.exec_()      


    def getValueBy(self, column):
        query = QSqlQuery("SELECT pc."+column+"\
            FROM project_criterias pc\
            LEFT JOIN parameters pa ON pa.project_criteria_id = pc.id\
            LEFT JOIN projects pr ON pr.parameter_id = pa.id\
            WHERE pr.active")
        if query.first():
            return query.value(0)
        else:
            return 0
