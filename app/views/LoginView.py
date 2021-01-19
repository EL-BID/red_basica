from PyQt5.QtWidgets import QDialog
from .ui.LoginView import Ui_loginQDialog

class LoginView(QDialog, Ui_loginQDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)