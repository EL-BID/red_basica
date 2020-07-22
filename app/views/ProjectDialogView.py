from PyQt5.QtWidgets import (QAbstractItemView, QDataWidgetMapper, QCompleter, QComboBox,
    QHeaderView, QDialog, QMessageBox)
from PyQt5.QtGui import QKeySequence
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlRelationalDelegate
from PyQt5.QtCore import Qt, pyqtSlot, QModelIndex, QDateTime
from ..models.Project import Project
from .ui.ProjectDialogUi import Ui_ProjectDialog

class ProjectView(QDialog, Ui_ProjectDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.selectedProject = None
        self.model = Project()
        self.model.setSort(self.model.fieldIndex('active'),Qt.DescendingOrder)
        selectProjectCompleter = QCompleter(self.model)
        selectProjectCompleter.setCaseSensitivity(Qt.CaseInsensitive)
        self.selectProjectBox.setCompleter(selectProjectCompleter)
        self.selectProjectBox.setModel(self.model)
        self.selectProjectBox.setModelColumn(self.model.fieldIndex('name'))

        #actions
        self.selectProjectBox.currentIndexChanged.connect(self.on_change)
                
        #active project should be 0 if sorted
        self.selectProjectBox.setCurrentIndex(0)

    def on_change(self, i):
        id = self.model.data(self.model.index(i, self.model.fieldIndex("id")))
        self.selectedProject = id

    def showEvent(self, event): 
        self.model.select()
        self.selectProjectBox.setCurrentIndex(0)    

    def saveRecord(self):        
        self.model.setActive(self.selectedProject)