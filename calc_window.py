import sys
import os
import json
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from .models.model import Model
from .controllers.main_ctrl import MainController
from .views.main_view import MainView

class CalcWindow(QMainWindow):

    def __init__(self):
        #,sys_argv
        super(CalcWindow, self).__init__()
        # sys_argv
        self.model = Model()
        self.main_controller = MainController(self.model)
        self.main_view = MainView(self.model, self.main_controller)

    if __name__ == '__main__':
        app = CalcWindow()
        # sys.argv
        # app = App()
        sys.exit(app.exec_())
        
    
    def show(self):          
        # test = Test()
        self.main_view.show()
        # self.webview.show()
        # test.addMany([{'nombre':'uno', 'valor': 1},{'nombre':'dos', 'valor': 2}])
        #test.add({'nombre': 'tres', 'valor': 3})        
        #rec = test.get(3)
        #test.delete(3)
        # tests = test.getAll()
        #test.update({'nombre': 'uno editado'}, {'valor': 1})
        #all = test.getAll()  
        # self.webview.show()
    