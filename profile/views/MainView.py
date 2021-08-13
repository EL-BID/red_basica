from .ui.ProfileWidgetUi import Ui_ProfileWidget
from qgis.PyQt.QtWidgets import QDockWidget
from qgis.PyQt.QtCore import *
from .. import pyqtgraph as pg
from ...app.models.Calculation import Calculation

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')


class MainView(QDockWidget, Ui_ProfileWidget):
    def __init__(self):
        QDockWidget.__init__(self)
        self.setupUi(self)
        self.location = Qt.BottomDockWidgetArea
        self.updateButton.clicked.connect(self.updatePlot)
        layout = self.frame_for_plot.layout()
        while layout.count():
            child = layout.takeAt(0)
            child.widget().deleteLater()
        self.plotWdg = self.set_plot_widget()
        layout.addWidget(self.plotWdg)
        

    def set_plot_widget(self):        
        plotWdg = pg.PlotWidget()
        plotWdg.showGrid(True,True,0.5)
        datavline = pg.InfiniteLine(0, angle=90 ,pen=pg.mkPen('b',  width=1) , name = 'cross_vertical' )
        datahline = pg.InfiniteLine(0, angle=0 , pen=pg.mkPen('b',  width=1) , name = 'cross_horizontal')
        plotWdg.addItem(datavline)
        plotWdg.addItem(datahline)
        #cursor
        xtextitem = pg.TextItem('X : /', color = (0,0,0), border = pg.mkPen(color=(0, 0, 0),  width=1), fill=pg.mkBrush('w'), anchor=(0,1))
        ytextitem = pg.TextItem('Y : / ', color = (0,0,0) , border = pg.mkPen(color=(0, 0, 0),  width=1), fill=pg.mkBrush('w'), anchor=(0,0))
        plotWdg.addItem(xtextitem)
        plotWdg.addItem(ytextitem)

        plotWdg.getViewBox().autoRange( items=[])
        plotWdg.getViewBox().disableAutoRange()
        plotWdg.getViewBox().border = pg.mkPen(color=(0, 0, 0),  width=1)

        return plotWdg
            
    def updatePlot(self):
        segments  = Calculation.getActiveProfileData()
        for n in segments.keys():
            # puntos
            x = [col['x'] for col in segments[n]]
            y = [col['y'] for col in segments[n]]
            self.plotWdg.plot(x, y, pen=pg.mkPen( 'r',  width=2) , name = n)
        # re scale
        self.plotWdg.getViewBox().autoRange( items=self.plotWdg.getPlotItem().listDataItems())    
