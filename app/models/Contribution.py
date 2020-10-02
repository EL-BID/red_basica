from PyQt5.QtCore import Qt, pyqtSignal, QModelIndex,QAbstractTableModel
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlQuery

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
        return super(Contribution, self).headerData(section, orientation, role)