import sys
import os
import json
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QMainWindow, QDialog, QCompleter, QWidget,QApplication
from PyQt5.QtSql import QSqlRelationalDelegate
#from .app.controllers.MainController import MainController
from .app.models.Project import Project
from .app.views.MainView import MainView
from .app.views.ProjectDialogView import ProjectView
from .app.views.NewProjectView import NewProjectView
from .app.views.ParameterView import ParameterView

class App(QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        self.projectModel = Project()
        self.newProjectDialog = NewProjectView()
        self.projectDialog = ProjectView()
        self.parametersDialog = ParameterView()

        self.dialogs = {
            'newProject': self.newProjectDialog,
            'project': self.projectDialog,
            'parameters': self.parametersDialog
        }
        
        self.MainView = MainView(self.dialogs)


    if __name__ == '__main__':
        app = App()
        sys.exit(app.exec_())
        
    def show(self):
        self.MainView.show()
        if not self.projectModel.getActiveProject():
            self.insert_new_project()
        if self.projectModel.getActiveProject():
            self.MainView.setWindowTitle('SANIBIDapp [' + self.projectModel.getNameActiveProject() + ']')


    def insert_new_project(self):
        self.MainView.openNewProjectDialog()

    # def save_parameters(self):
    #     self.MainView.saveParameters()
