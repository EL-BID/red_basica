import sys
import os
import json
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from .app.models.test import Test
from .app.controllers.MainController import MainController
from .app.views.MainView import MainView


class App(QMainWindow):

    def __init__(self):
        #,sys_argv
        super(App, self).__init__()
        # sys_argv        
        self.model = Test()
        self.main_controller = MainController(self.model)
        self.MainView = MainView(self.model, self.main_controller)

    if __name__ == '__main__':
        app = App()
        # sys.argv
        # app = App()
        sys.exit(app.exec_())
        

    def show(self):          
        # test = Test()
        self.MainView.show()
        # self.webview.show()
        # test.addMany([{'nombre':'uno', 'valor': 1},{'nombre':'dos', 'valor': 2}])
        #test.add({'nombre': 'tres', 'valor': 3})        
        #rec = test.get(3)
        #test.delete(3)
        # tests = test.getAll()
        #test.update({'nombre': 'uno editado'}, {'valor': 1})
        #all = test.getAll()  
        # self.webview.show()
    