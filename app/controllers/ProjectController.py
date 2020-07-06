from PyQt5.QtCore import QObject, QDateTime


class ProjectController(QObject):
    def __init__(self, model=None, ui=None):
        super().__init__()

        self.model = model
        self.ui = ui

    def set_active_project(self):
        combo = self.ui.selectProjectBox
        comboModel = combo.model()
        index = combo.currentIndex()
        currentId = comboModel.index(index, comboModel.fieldIndex('id')).data()
        self.model.setActive(currentId)
       
        
    def insert_record(self):        
        record = self.model.record()
        record.setGenerated('id', False)
        record.setValue('parameter_id', None)
        record.setValue('name', self.ui.nameEdit.text())       
        record.setValue('city', self.ui.cityEdit.text())
        record.setValue('microsystem', self.ui.microsystemEdit.text())
        record.setValue('author', self.ui.authorEdit.text())
        record.setValue('active', 0)
        record.setValue('date', self.ui.dateEdit.date())
        record.setValue('created_at', QDateTime.currentDateTime())
        record.setValue('updated_at', QDateTime.currentDateTime())
        newRecord = self.model.insertRecord(-1, record) #con -1 lo inserta al final
        if newRecord:
            lastId = self.model.query().lastInsertId()
            self.model.setActive(lastId)
        


         