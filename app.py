import sys
from PyQt5.QtWidgets import QApplication
from .models.model import Model
from .controllers.main_ctrl import MainController
from .views.main_view import MainView


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.main_controller = MainController(self.model)
        self.main_view = MainView(self.model, self.main_controller)
        self.main_view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    # app = App()
    sys.exit(app.exec_())