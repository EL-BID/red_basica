from PyQt5.QtCore import Qt, QCoreApplication, QT_TRANSLATE_NOOP
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlQuery
from PyQt5.QtGui import QColor

translate = QCoreApplication.translate
tr = QT_TRANSLATE_NOOP

class Contribution(QSqlRelationalTableModel):
    
    def __init__(self, *args, **kwargs):
        super(Contribution, self).__init__(*args, **kwargs)
        self.setTable("contributions")
        self.select()
        self.columns = [
            tr("ContTbl", "col_seg"),
            tr("ContTbl", "previous_col_seg_end"),
            tr("ContTbl", "col_pipe_m1_end"),
            tr("ContTbl", "col_pipe_m2_end"),
            tr("ContTbl", "subtotal_up_seg_end"),
            tr("ContTbl", "condominial_lines_end"),
            tr("ContTbl", "linear_contr_seg_end"),
            tr("ContTbl", "previous_col_seg_start"),
            tr("ContTbl", "col_pipe_m1_start"),
            tr("ContTbl", "col_pipe_m2_start"),
            tr("ContTbl", "subtotal_up_seg_start"),
            tr("ContTbl", "condominial_lines_start"),
            tr("ContTbl", "linear_contr_seg_start")
        ]
        self.hiddenColumns = ["id", "calculation_id", "created_at", "updated_at", "initial_segment"]

    
    def getColumns(self):
        return self.columns

    def getHiddenColumns(self):
        return self.hiddenColumns
    
    def headerData(self, section, orientation, role = Qt.DisplayRole):
        if (orientation == Qt.Vertical and role == Qt.BackgroundRole and self.record(section).value('initial_segment') == 1):
            return QColor(230, 104, 41)
        if (orientation == Qt.Vertical and role == Qt.DisplayRole):
            return self.record(section).value('col_seg')
        if role == Qt.ToolTipRole:
            if orientation == Qt.Horizontal:
                return translate("ContTbl", self.record().fieldName(section))
        return super(Contribution, self).headerData(section, orientation, role)