from PyQt5.QtWidgets import QDialog
from .ui.IterationsDialogUi import Ui_iterations

class IterationsView(QDialog, Ui_iterations):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)