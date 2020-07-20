import sys
import os
import json
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QMainWindow, QDialog, QCompleter
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlRelationalDelegate
from .app.controllers.MainController import MainController
from .app.views.MainView import MainView
from .app.views.NewProjectView import NewProjectView
from .app.views.ParameterView import ParameterView

class App(QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        self.projectDialog = NewProjectView()
        self.parametersDialog = ParameterView()

        self.dialogs = {
            'project': self.projectDialog,
            'parameters': self.parametersDialog
        }

        self.main_controller = MainController(None)
        self.MainView = MainView(self.dialogs, self.main_controller)

    if __name__ == '__main__':
        app = App()
        sys.exit(app.exec_())
        
    def show(self):          
        self.MainView.show()
        # if not self.projectModel.getActiveProject():
        self.show_new_project()
        # if self.projectModel.getActiveProject():
        #     self.MainView.setWindowTitle('SANIBIDapp [' + self.projectModel.getNameActiveProject() + ']')

    def show_new_project(self):
        print('  ')
        # self.MainView.newProject()

    def insert_new_project(self):
        self.MainView.insertNewProject()
        self.MainView.openParametersDialog()
        self.MainView.setWindowTitle('SANIBIDapp [' + self.projectModel.getNameActiveProject() + ']')

    def save_parameters(self):
        self.MainView.saveParameters()
