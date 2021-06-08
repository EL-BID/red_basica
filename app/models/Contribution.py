from PyQt5.QtCore import Qt, pyqtSignal, QModelIndex,QAbstractTableModel, QCoreApplication
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlQuery
from PyQt5.QtGui import QColor

translate = QCoreApplication.translate

class Contribution(QSqlRelationalTableModel):
    
    def __init__(self, *args, **kwargs):
        super(Contribution, self).__init__(*args, **kwargs)
        self.setTable("contributions")
        self.select()
    
    def headerData(self, section, orientation, role = Qt.DisplayRole):
        if (orientation == Qt.Vertical and role == Qt.BackgroundRole and self.record(section).value('initial_segment') == 1):
            return QColor(230, 104, 41)
        if (orientation == Qt.Vertical and role == Qt.DisplayRole):
            return self.record(section).value('col_seg')
        if role == Qt.ToolTipRole:
            if orientation == Qt.Horizontal:
                return translate("ContTbl", self.record().fieldName(section))
        return super(Contribution, self).headerData(section, orientation, role)