from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtCore import pyqtSlot, Qt, QModelIndex
from PyQt5 import uic
from .MainWindowUi import Ui_MainWindow



class MainView(QMainWindow):
    def __init__(self, dialogs, controller):
        super().__init__()

        #Main window
        self._dialogs = dialogs
        self._main_controller = controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        
        #menu actions 
        self._ui.actionProject.triggered.connect(self.openProjectDialog)
        self._ui.actionParameters.triggered.connect(self.openParametersDialog)

    def openProjectDialog(self):
        self._dialogs['project'].show()

    def closeProjectDialog(self):
        self._dialogs['project'].hide()       

    def openNewProjectDialog(self):
        self._dialogs['newProject'].show()

    def closeNewProjectDialog(self):
        self._dialogs['newProject'].hide() 

    def openParametersDialog(self):
        self._dialogs['parameters'].show() 

    def closeParametersDialog(self):
        self._dialogs['parameters'].hide()                            
                   
    def newProject(self):
        self.closeProjectDialog()
        self.openNewProjectDialog()

    def insertNewProject(self):
        dialog = self._dialogs['newProject']
        dialog._main_controller.insert_record()       
        #clear inputs
        # todo: find way to iterate over widgets
        dialog._ui.projectNameEdit.clear()
        dialog._ui.countryEdit.clear()
        dialog._ui.cityEdit.clear()
        dialog._ui.authorEdit.clear() 
        dialog._ui.dateEdit.clear()
        dialog._ui.microsystemEdit.clear()        
        #self._dialogs['project']._ui.selectProjectBox.model.dataChanged.emit(QModelIndex(), QModelIndex())
        #falta setear el currentIndex al combo
   