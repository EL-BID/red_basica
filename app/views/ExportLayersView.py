from PyQt5.QtWidgets import QDialog
from .ui.ExportLayersDialogUi import Ui_ExportLayersDialog

class ExportLayersView(QDialog, Ui_ExportLayersDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.overrideRadioButton.clicked.connect(self.onOverrideChecked)
        self.createRadioButton.clicked.connect(self.onCreateChecked)

    def onOverrideChecked(self):
        self.segmentsEdit.setDisabled(True)
        self.nodesEdit.setDisabled(True)
    

    def onCreateChecked(self):
        self.segmentsEdit.setDisabled(False)
        self.nodesEdit.setDisabled(False)