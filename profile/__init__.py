import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from .views.MainView import MainView


class Profile:

    def __init__(self, iface):
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.initialized = False
        self.profileWidget = None


    def run(self):
        if not self.initialized:
            self.profileWidget = MainView()
            self.iface.addDockWidget(self.profileWidget.location, self.profileWidget)
            self.initialized = True
        else:
            self.profileWidget.show()
            print("ya esta instanciado")

    