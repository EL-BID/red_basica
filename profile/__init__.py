import sys
import os
from . import pyqtgraph as pg
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import QMainWindow


class Profile(QMainWindow):
    def __init__(self):
        super(Profile, self).__init__()             

    if __name__ == "__main__":
        win = Profile()
        plot = pg.plot()
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        y1 = [1, 0.5, 0.7, 0.1, 0.4, 1, 0.8, 1, 0.3, 1 ]
        bg1 = pg.BarGraphItem(x=x, height=y1, width=0.3, brush='r')
        plot.addItem(bg1)  
        win.addItem(plot)
        sys.exit(win.exec_())
