from PyQt5.QtWidgets import QMainWindow, QDialog, QAbstractItemView
from PyQt5.QtCore import pyqtSlot, Qt, QModelIndex
from PyQt5.QtSql import QSqlRelationalDelegate
from PyQt5 import uic
from .ui.MainWindowUi import Ui_MainWindow
from ..controllers.CalculationController import CalculationController
from ..models.Calculation import Calculation
from ..models.Contribution import Contribution
from ..models.WaterLevelAdj import WaterLevelAdj
from ..models.delegates.CalculationDelegate import CalculationDelegate

class MainView(QMainWindow, Ui_MainWindow):
    def __init__(self, dialogs):

        QMainWindow.__init__(self)
        self.setupUi(self)

        #Main window
        self._dialogs = dialogs
        self.calculationController = CalculationController()

        #Models
        self.calcModel = Calculation()
        self.contribModel = Contribution()
        self.wlaModel = WaterLevelAdj()
        
        #Red Basica Table
        self.calcTable.setModel(self.calcModel)        
        self.calcTable.setItemDelegate(CalculationDelegate(self.calcTable))
        self.calcTable.setColumnHidden(self.calcModel.fieldIndex("id"), True)
        self.calcTable.setColumnHidden(self.calcModel.fieldIndex("project_id"), True)
        self.calcTable.setColumnHidden(self.calcModel.fieldIndex("layer_name"), True)
        self.calcTable.setColumnHidden(self.calcModel.fieldIndex("created_at"), True)
        self.calcTable.setColumnHidden(self.calcModel.fieldIndex("updated_at"), True)
        
        #Contributions Table
        self.contribTable.setModel(self.contribModel)
        self.contribTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.contribTable.setColumnHidden(self.contribModel.fieldIndex("id"), True)
        self.contribTable.setColumnHidden(self.contribModel.fieldIndex("calculation_id"), True)        
        self.contribTable.setColumnHidden(self.contribModel.fieldIndex("created_at"), True)
        self.contribTable.setColumnHidden(self.contribModel.fieldIndex("updated_at"), True)       
        self.contribTable.horizontalHeader().setSectionResizeMode(True)

        #WaterLevelAdj Table
        self.wlaTable.setModel(self.wlaModel)
        self.wlaTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.wlaTable.setColumnHidden(self.wlaModel.fieldIndex("id"), True)
        self.wlaTable.setColumnHidden(self.wlaModel.fieldIndex("calculation_id"), True)
        self.wlaTable.setColumnHidden(self.wlaModel.fieldIndex("created_at"), True)
        self.wlaTable.setColumnHidden(self.wlaModel.fieldIndex("updated_at"), True)        

        
        #menu actions
        self.actionProject.triggered.connect(self.checkProjectAction)
        self.actionParameters.triggered.connect(self.openParametersDialog)
        self.actionCalculara_DN.triggered.connect(self.calculateDN)
        self.actionCalcular_DN_Creciente.triggered.connect(self.calculateGrowingDN)

        #triggered actions
        self._dialogs['newProject'].buttonBox.accepted.connect(self.changeMainTitle)
        self._dialogs['newProject'].buttonBox.accepted.connect(self.closeProjectDialog)
        self._dialogs['newProject'].buttonBox.accepted.connect(self.openParametersDialog)
        self._dialogs['project'].newProjectButton.clicked.connect(self.openNewProjectDialog)
        self._dialogs['project'].dialogButtonBox.accepted.connect(self.updateProject)
        self._dialogs['parameters'].buttonBox.accepted.connect(self.closeParametersDialog)
        self._dialogs['parameters'].buttonBox.accepted.connect(self.callImport)
    
    def updateProject(self):
        self._dialogs['project'].saveRecord()
        self.changeMainTitle()

    def checkProjectAction(self):
        if self._dialogs['project'].model.getActiveProject():           
            self.openProjectDialog()
        else:            
            self.openNewProjectDialog()

    def openProjectDialog(self):
        self._dialogs['project'].show()

    def closeProjectDialog(self):
        self._dialogs['project'].hide()       

    def openNewProjectDialog(self):
        self.closeProjectDialog()
        self._dialogs['newProject'].addRecord()
        self._dialogs['newProject'].show()        

    def changeMainTitle(self):
        name = self._dialogs['newProject'].model.getNameActiveProject()
        self.setWindowTitle('SANIBIDapp [' + name + ']')

    def closeNewProjectDialog(self):
        self._dialogs['newProject'].hide() 

    def openParametersDialog(self):
        self._dialogs['parameters'].show()         

    def closeParametersDialog(self):
        self._dialogs['parameters'].hide()

    def callImport(self):
        projectId = self._dialogs['newProject'].model.getActiveId()
        self.calculationController.importData(projectId)
        self.calcModel.select()
        self.contribModel.select()
        self.wlaModel.select()
        #TODO order by col_seg

    def calculateDN(self):
        projectId = self._dialogs['newProject'].model.getActiveId()
        self.calculationController.calculateDN(projectId)
        self.calcModel.select()
        self.contribModel.select()
        self.wlaModel.select()
    
    def calculateGrowingDN(self):
        projectId = self._dialogs['newProject'].model.getActiveId()
        self.calculationController.calculateDN(projectId, True)
        self.calcModel.select()
        self.contribModel.select()
        self.wlaModel.select()

    def newProject(self):
        self.closeProjectDialog()
        self.openNewProjectDialog()