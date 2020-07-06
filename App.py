import sys
import os
import json
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from .app.controllers.MainController import MainController
from .app.views.MainView import MainView
from .app.views.ProjectDialogUi import Ui_ProjectDialog
from .app.views.NewProjectDialogUi import Ui_NewProjectDialog
from .app.controllers.MainController import MainController
from .app.controllers.ProjectController import ProjectController
from .app.models.Project import Project

class App(QMainWindow):

    def __init__(self):
        #,sys_argv
        super(App, self).__init__()
        self.projectModel = Project()

        #Projects 
        projectDialog = QDialog()        
        projectDialog._model = self.projectModel        
        projectDialog._ui = Ui_ProjectDialog()
        projectDialog._ui.setupUi(projectDialog)
        projectDialog._ui.selectProjectBox.setModel(projectDialog._model)    
        projectDialog._ui.selectProjectBox.setEditable(True)    
        projectDialog._ui.selectProjectBox.setModelColumn(projectDialog._model.getDisplayColumn())   
        projectDialog._main_controller = ProjectController(projectDialog._model, projectDialog._ui)    
        projectDialog._ui.dialogButtonBox.accepted.connect(projectDialog._main_controller.set_active_project)
        projectDialog._ui.newProjectButton.clicked.connect(self.show_new_project)

        #New Project Dialog
        newProjectDialog = QDialog()    
        newProjectDialog._model = self.projectModel          
        newProjectDialog._ui = Ui_NewProjectDialog()
        newProjectDialog._ui.setupUi(newProjectDialog)   
        newProjectDialog._main_controller = ProjectController(newProjectDialog._model, newProjectDialog._ui)    
        newProjectDialog._ui.dialogButtonBox.accepted.connect(self.insert_new_project)

        self.dialogs = {
            'project': projectDialog,
            'newProject': newProjectDialog
        }

        self.main_controller = MainController(None)
        self.MainView = MainView(self.dialogs, self.main_controller)

    if __name__ == '__main__':
        app = App()
        # sys.argv
        # app = App()
        sys.exit(app.exec_())
        

    def show(self):          
        self.MainView.show()
        if not self.projectModel.getActiveProject():
            self.show_new_project()

    def show_new_project(self):
        self.MainView.newProject()

    def insert_new_project(self):
        self.MainView.insertNewProject()
        
    