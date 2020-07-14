import sys
import os
import json
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QMainWindow, QDialog, QCompleter
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from .app.controllers.MainController import MainController
from .app.views.MainView import MainView
from .app.views.ProjectDialogUi import Ui_ProjectDialog
from .app.views.NewProjectDialogUi import Ui_NewProjectDialog
from .app.views.ParameterDialogUi import Ui_NewParameterDialog
from .app.controllers.MainController import MainController
from .app.controllers.ProjectController import ProjectController
from .app.controllers.ParameterController import ParameterController
from .app.models.Project import Project
from .app.models.Country import Country
from .app.models.Parameter import Parameter, ParameterDataMapper

class App(QMainWindow):

    def __init__(self):
        #,sys_argv
        super(App, self).__init__()
        self.projectModel = Project()
        self.countryModel = Country()
        self.parameterModel = Parameter()

        #Projects 
        projectDialog = QDialog()        
        projectDialog._model = self.projectModel        
        projectDialog._ui = Ui_ProjectDialog()
        projectDialog._ui.setupUi(projectDialog)
        projectDialog._ui.selectProjectBox.setModel(self.projectModel)    
        projectDialog._ui.selectProjectBox.setEditable(True)    
        projectDialog._ui.selectProjectBox.setModelColumn(projectDialog._model.getDisplayColumn())   
        projectDialog._main_controller = ProjectController(self.projectModel, projectDialog._ui)    
        projectDialog._ui.dialogButtonBox.accepted.connect(projectDialog._main_controller.set_active_project)
        projectDialog._ui.newProjectButton.clicked.connect(self.show_new_project)

        #New Project Dialog
        newProjectDialog = QDialog()    
        newProjectDialog._model = self.projectModel          
        newProjectDialog._ui = Ui_NewProjectDialog()
        newProjectDialog._ui.setupUi(newProjectDialog)

        completer = QCompleter(self.countryModel)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        newProjectDialog._ui.countryBox.setCompleter(completer)
        newProjectDialog._ui.countryBox.setEditable(True)
        for i, text in self.countryModel.getList():
            newProjectDialog._ui.countryBox.addItem(text, i)

        newProjectDialog._main_controller = ProjectController(newProjectDialog._model, newProjectDialog._ui)    
        newProjectDialog._ui.buttonBox.accepted.connect(self.insert_new_project)

        #Parameter Dialog
        parametersDialog = QDialog()    
        parametersDialog._model = self.parameterModel          
        parametersDialog._ui = Ui_NewParameterDialog()
        parametersDialog._ui.setupUi(parametersDialog)
        parametersDialog._mapper = ParameterDataMapper()
        parametersDialog._mapper.setModel(self.parameterModel)
        parametersDialog._mapper.map(parametersDialog._ui)
        parametersDialog._mapper.toFirst()
        parametersDialog._main_controller = ParameterController(newProjectDialog._model, newProjectDialog._ui)    
        #parameterDialog._ui.buttonBox.accepted.connect(self.insert_new_project)

        self.dialogs = {
            'project': projectDialog,
            'newProject': newProjectDialog,
            'parameters': parametersDialog
        }

        self.main_controller = MainController(None)
        self.MainView = MainView(self.dialogs, self.main_controller)

    if __name__ == '__main__':
        app = App()
        sys.exit(app.exec_())
        

    def show(self):          
        self.MainView.show()
        if not self.projectModel.getActiveProject():
            self.show_new_project()

    def show_new_project(self):
        self.MainView.newProject()

    def insert_new_project(self):
        self.MainView.insertNewProject()
        self.MainView.openParametersDialog()      
        
    