from PyQt5.QtWidgets import (QAbstractItemView, QDataWidgetMapper, QCompleter, QComboBox,
    QHeaderView, QDialog, QMessageBox)
from PyQt5.QtGui import QKeySequence
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlRelationalDelegate
from PyQt5.QtCore import Qt, pyqtSlot, QModelIndex, QDateTime
from ..models.Project import Project
from .ui.ProjectDialogUi import Ui_ProjectDialog

class ProjectView(QDialog, Ui_ProjectDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.selectedProject = None        
        self.model = Project()
        self.model.setSort(self.model.fieldIndex('active'),Qt.DescendingOrder)        
        self.selectProjectBox.setModel(self.model)
        self.selectProjectBox.setModelColumn(self.model.fieldIndex('name'))

        #Remember the index of country
        country_idx = self.model.fieldIndex("country_id")

        #set the relations to the other ddbb tables
        self.model.setRelation(country_idx, QSqlRelation("countries", "id", "name_en"))

        #Initialize the Country combobox
        self.countryBox.setModel(self.model.relationModel(country_idx))
        self.countryBox.setModelColumn(self.model.relationModel(country_idx).fieldIndex("name_en"))
        #Initialize the QCompleter
        selectCountryCompleter = QCompleter(self.model.relationModel(country_idx))
        selectCountryCompleter.setCompletionMode(QCompleter.InlineCompletion)
        selectCountryCompleter.setCaseSensitivity(Qt.CaseInsensitive)
        self.countryBox.setCompleter(selectCountryCompleter)
        self.countryBox.setEditable(True)
        self.countryBox.setInsertPolicy(QComboBox.NoInsert)

        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel(self.model)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.AutoSubmit)
        self.mapper.setItemDelegate(QSqlRelationalDelegate(self))
        self.mapper.addMapping(self.projectNameEdit, self.model.fieldIndex("name"))
        self.mapper.addMapping(self.cityEdit, self.model.fieldIndex("city"))
        self.mapper.addMapping(self.microsystemEdit, self.model.fieldIndex("microsystem"))
        self.mapper.addMapping(self.authorEdit, self.model.fieldIndex("author"))
        self.mapper.addMapping(self.dateEdit, self.model.fieldIndex("date"))
        self.mapper.addMapping(self.countryBox, country_idx)
        #mapper index is set on showEvent
                
        #actions
        self.selectProjectBox.currentIndexChanged.connect(self.on_change)
                

    def on_change(self, i):
        id = self.model.data(self.model.index(i, self.model.fieldIndex("id")))
        name = self.model.data(self.model.index(i, self.model.fieldIndex("name")))
        self.selectedProject = id
        idx = self.selectProjectBox.findText(name)
        self.mapper.setCurrentIndex(idx)

    def showEvent(self, event): 
        self.model.select()
        #model is sorted by active so is the first record
        self.selectProjectBox.setCurrentIndex(0)    
        self.mapper.setCurrentIndex(0)

    def saveRecord(self):
        self.model.submit()   
        self.model.setActive(self.selectedProject)