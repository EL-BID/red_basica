from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic
from .MainViewUi import Ui_MainWindow

class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.todoView.setModel(self._model)
        self._ui.addButton.pressed.connect(self.onAddRow)
        # # connect widgets to controller
        # self._ui.spinBox_amount.valueChanged.connect(self._main_controller.change_amount)
        # self._ui.pushButton_reset.clicked.connect(lambda: self._main_controller.change_amount(0))

        # # listen for model event signals
        # self._model.amount_changed.connect(self.on_amount_changed)
        # self._model.even_odd_changed.connect(self.on_even_odd_changed)
        # self._model.enable_reset_changed.connect(self.on_enable_reset_changed)

        # # set a default value
        # self._main_controller.change_amount(89)

    def onAddRow(self):
        self._model.insertRows(self._model.rowCount(), 1)
        self._model.submit()