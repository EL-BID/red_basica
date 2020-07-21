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
        self.model = Project()
        # self.loadComboBox()
        selectProjectCompleter = QCompleter(self.model)
        selectProjectCompleter.setCaseSensitivity(Qt.CaseInsensitive)
        self.selectProjectBox.setCompleter(selectProjectCompleter)
        self.selectProjectBox.setModel(self.model)
        self.selectProjectBox.setModelColumn(self.model.fieldIndex('name'))
        # projectDialog._main_controller = ProjectController(self.projectModel, projectDialog._ui)
        # projectDialog._main_controller = ProjectController(projectDialog)
        # self.selectProjectBox.model.dataChanged.emit(QModelIndex(), QModelIndex())
        self.dialogButtonBox.accepted.connect(self.saveRecord)

    def loadComboBox(self):
        selectProjectCompleter = QCompleter(self.model)
        selectProjectCompleter.setCaseSensitivity(Qt.CaseInsensitive)
        self.selectProjectBox.setCompleter(selectProjectCompleter)
        self.selectProjectBox.setModel(self.model)
        self.selectProjectBox.setModelColumn(self.model.fieldIndex('name'))

    def addRecord(self):
        print('addrecord')
        # row = self.model.rowCount()
        # self.mapper.submit()
        # self.model.insertRow(row)
        # self.mapper.setCurrentIndex(row)
        # now = QDateTime.currentDateTime()
        # self.dateEdit.setDateTime(now)
        # self.projectNameEdit.setFocus()

    def saveRecord(self):
        # row = self.mapper.currentIndex()
        # self.mapper.submit()
        # self.mapper.setCurrentIndex(row)
        print('holis')