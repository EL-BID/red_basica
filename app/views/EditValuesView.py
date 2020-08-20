from PyQt5.QtWidgets import (QAbstractItemView, QDataWidgetMapper, QCompleter, QComboBox,
    QHeaderView, QDialog, QMessageBox)
from PyQt5.QtGui import QKeySequence
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlRelationalDelegate
from PyQt5.QtCore import Qt, pyqtSlot, QModelIndex, QDateTime
from ..models.Project import Project
from .ui.EditValuesDialogUi import Ui_editDialog

class EditValuesView(QDialog, Ui_editDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)