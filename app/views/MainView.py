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

    def openProjectDialog(self):
        self._dialogs['project'].show()

    def closeProjectDialog(self):
        self._dialogs['project'].hide()       

    def openNewProjectDialog(self):
        self._dialogs['newProject'].show()

    def closeNewProjectDialog(self):
        self._dialogs['newProject'].hide()             
                   
    def newProject(self):
        self.closeProjectDialog()
        self.openNewProjectDialog()

    def insertNewProject(self):
        self._dialogs['newProject']._main_controller.insert_record()        
        #self._dialogs['project']._ui.selectProjectBox.model.dataChanged.emit(QModelIndex(), QModelIndex())
        #falta setear el currentIndex al combo

    def onAddRow(self):
        self._model.insertRows(self._model.rowCount(), 1)
        self._model.submit()