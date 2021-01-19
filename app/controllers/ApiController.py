from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QCoreApplication
from ..models.Project import Project
from ..controllers.DataController import DataController
import requests, json, traceback

translate = QCoreApplication.translate

class ApiController(QObject):
    finished = pyqtSignal(object)
    error = pyqtSignal(Exception, basestring)
    progress = pyqtSignal(float)
    info = pyqtSignal(str)
    message = pyqtSignal(str)

    def __init__(self, model=None):
        super().__init__()
        self.projectModel = Project()

    def publishProject(self, projectId, user, password):
        """ publish project to sanibid dashboard """
        success = False
        msg = translate("Api", "Processing project")
        self.info.emit(msg)
        self.progress.emit(25)

        controller = DataController()
        project = controller.getFullProject(user, password, wgs84=True)
        if project:
            url = "http://localhost:3000/api/projects"
            payload=json.dumps(project)
            headers = {
            'Content-Type': 'application/json'
            }
            self.progress.emit(50)
            self.info.emit(translate("Api", "Sending project to server"))
            serverId = self.projectModel.getValueBy('server_id',projectId)

            if (serverId == None):
                response = requests.request("POST", url, headers=headers, data=payload)
            else:
                response = requests.request("PUT", url+'/{}'.format(projectId), headers=headers, data=payload)

            res = response.json()

            if (res['status'] != 200):
                success = False
                self.info.emit('Error: '+res['message'])
                
            else:
                self.projectModel.updateServerId(res['server_id'])
                self.progress.emit(100)
                success = True
                self.info.emit(translate("Api", "Project submitted"))
        else:
            success = False
            self.info.emit('Error: Not able to generate Project JSON')

        self.finished.emit(success)
        return True