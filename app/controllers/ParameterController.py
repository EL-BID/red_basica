from PyQt5.QtCore import QObject, QDateTime


class ParameterController(QObject):

    def __init__(self, dialog=None):
        super().__init__()
        if dialog:
            self.model = dialog._model
            self.ui = dialog._ui
            self.mapper = dialog._mapper
            self.mapper_crit = dialog._mapper_crit
        else:
            raise Exception("Dialog is needed to create ParameterController")       
        
    def load_parameters(self):
        data = self.model.getCurrentData()        
        if data:
            filter_param = "id = {}".format(data['parameter_id'])
            self.mapper.model().setFilter(filter_param)
            self.mapper.toFirst()

            filter_crit = "id = {}".format(data['criteria_id'])
            self.mapper_crit.model().setFilter(filter_crit)
            self.mapper_crit.toFirst()

        else:
            raise Exception("Parameters data not found")

    def save(self):
        self.mapper.submit()
        self.mapper_crit.submit()
        #self.mapper.submit()            

         