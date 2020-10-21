from PyQt5.QtWidgets import QDialog
from .ui.IterationsDialogUi import Ui_iterationsDialog

class IterationsView(QDialog, Ui_iterationsDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)