from PyQt5.QtCore import QObject, QDateTime
from ..models.Parameter import Parameter

class ProjectController(QObject):
    def __init__(self, dialog=None):
        super().__init__()
        if dialog:    
            self.model = dialog._model
            self.ui = dialog._ui
        else:
            raise Exception("Dialog is needed to create ProjectController")            

    def set_active_project(self):
        combo = self.ui.selectProjectBox
        comboModel = combo.model()
        index = combo.currentIndex()
        currentId = comboModel.index(index, comboModel.fieldIndex('id')).data()
        self.model.setActive(currentId)