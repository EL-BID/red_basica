from PyQt5.QtWidgets import (QDialog)
from PyQt5.QtCore import QLocale
from .ui.EditValuesDialogUi import Ui_editDialog

class EditValuesView(QDialog, Ui_editDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))