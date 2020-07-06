from PyQt5.QtCore import QObject, pyqtSlot


class MainController(QObject):
    def __init__(self, model=None):
        super().__init__()

        self._model = model

    def set_active_project(self, text):
        print("set")
        pass

    @pyqtSlot(int)
    def change_amount(self, value):
        self._model.amount = value

        # calculate even or odd
        self._model.even_odd = 'odd' if value % 2 else 'evesn'

        # calculate button enabled state
        self._model.enable_reset = True if value else False