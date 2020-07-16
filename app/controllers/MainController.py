from PyQt5.QtCore import QObject, pyqtSlot


class MainController(QObject):
    def __init__(self, model=None):
        super().__init__()

        self._model = model

    def set_active_project(self, text):
        print("set")
        pass
    