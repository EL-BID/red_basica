from math import floor
from .ui.ProfileWidgetUi import Ui_ProfileWidget
from qgis.PyQt.QtWidgets import QDockWidget
from qgis.PyQt.QtCore import *
from qgis.core import QgsProject, QgsWkbTypes, QgsPointXY, QgsRasterLayer, QgsRaster, QgsDistanceArea
from ...base.helper_functions import HelperFunctions
from .. import pyqtgraph as pg
from ...app.models.Calculation import Calculation
from ..utils.vLayer import vLayer

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')


class MainView(QDockWidget, Ui_ProfileWidget):
    def __init__(self, iface):
        QDockWidget.__init__(self)
        self.setupUi(self)
        self.location = Qt.BottomDockWidgetArea
        self.h = HelperFunctions(iface)
        #layout
        self.layout = self.frame_for_plot.layout()
        self.layers = {}
        self.area_fill = None
        self.area_fill_margin = 1
        self.devices = None
        self.plotWdg = self.set_plot_widget()
        self.layout.addWidget(self.plotWdg)

        #update button
        self.updateButton.clicked.connect(self.updatePlot)

        #layers combo
        layers = [layer for layer in QgsProject.instance().mapLayers().values()]
        layer_list = []
        for layer in layers:
            if (layer.type() == layer.RasterLayer) or \
                (layer.type() == layer.MeshLayer) or \
                (layer.type() == layer.PluginLayer and layer.LAYER_TYPE == 'selafin_viewer') or \
                (layer.type() == layer.VectorLayer and layer.geometryType() ==  QgsWkbTypes.PointGeometry):
                layer_list.append(layer.name())
        self.layerComboBox.addItems(layer_list)


    def clearLayers(self):
        if self.area_fill:
            self.plotWdg.removeItem(self.area_fill)
        if self.devices:
            self.plotWdg.removeItem(self.devices)
        for k in self.layers.keys():
            self.layers[k].clear()

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
        self.clearLayers()
        profileLayerName = self.layerComboBox.currentText()
        interval = int(self.distanceDoubleSpinBox.value())
        col_seg_att_name = self.h.readValueFromProject("SEG_NAME_C")
        features = sorted(self.h.GetLayer().selectedFeatures(), key=lambda x: x.attribute(col_seg_att_name))
        virtualLayer  = vLayer("nameVirtual", "Point")
        rasterLayer = QgsProject.instance().mapLayersByName(profileLayerName)[0]
        xRaster = []
        yRaster = []
        y = []
        x = []
        devices = {'x':[], 'y':[], 'h':[] }
        xVal = None
        for f in features:
            col_seg = f.attribute(col_seg_att_name)
            line = f.geometry()

            #overlays
            data = Calculation.getActiveProfileData(col_seg)
            for n in data.keys():
                for col in data[n]:
                    #pipes layer
                    x1 = 0 if col['x_initial'] == None else col['x_initial']
                    if xVal is None:
                        xVal = x1
                    x2 = col['x_final']
                    x.extend([x1, x2]) 
                    
                    initialPointY = QgsPointXY(col['geom_x_initial'], col['geom_y_initial'])
                    iPy = rasterLayer.dataProvider().identify(initialPointY, QgsRaster.IdentifyFormatValue)
                    finalPointY = QgsPointXY(col['geom_x_final'], col['geom_y_final'])
                    fPy = rasterLayer.dataProvider().identify(finalPointY, QgsRaster.IdentifyFormatValue)
                    y1 = list(iPy.results().values())[0] - col['y_initial'] 
                    y2 = list(fPy.results().values())[0] - col['y_final']
                    y.extend([y1, y2])
                    
                    #devices
                    devices['x'].extend([x1, x2])
                    h1 = col['y_initial']
                    h2 = col['y_final']
                    devices['h'].extend([h1, h2])                                       
                    devices['y'].extend([y1 + h1/2, y2 + h2/2])

            #ground layer            
            for part in line.get():
                line_start = part[0]
                line_end = part[-1]                
                pointm = virtualLayer.diff(line_end, line_start)
                cosa,cosb = virtualLayer.dirCos(pointm)
                lg = virtualLayer.length(line_end, line_start)                
                distance = 0
                i = 0                
                while distance < (lg + self.area_fill_margin):
                    i += interval
                    point = QgsPointXY(line_start.x()  + (i * cosa), line_start.y() + (i * cosb))
                    ident = rasterLayer.dataProvider().identify(point, QgsRaster.IdentifyFormatValue)
                    virtualLayer.createPoint(point)
                    yVal = list(ident.results().values())[0]
                    xVal = xVal if not xRaster else (xVal + interval)                    
                    yRaster.append(yVal)
                    xRaster.append(xVal)                   
                    distance += interval 

        #TODO; another button to activate the new point layer
        #virtualLayer.displayLayer

        #draw ground area
        self.layers['ground'] = self.plotWdg.plot(xRaster, yRaster, pen=pg.mkPen('CCCCCC',  width=1))
        yGroundBase = [ (min(yRaster) - self.area_fill_margin) for i in yRaster]
        self.layers['ground_base'] = self.plotWdg.plot(xRaster, yGroundBase, pen=pg.mkPen('CCCCCC',  width=1))
        self.area_fill = pg.FillBetweenItem(self.layers['ground'], self.layers['ground_base'], brush=pg.mkBrush(242, 176, 109, 100))
        self.plotWdg.addItem(self.area_fill)
        
        #draw inspection devices
        self.devices = pg.BarGraphItem(x = devices['x'], y = devices['y'], height = devices['h'], width = 0.6, brush ='w')
        self.plotWdg.addItem(self.devices) 

        #draw pipes
        self.layers['pipes'] = self.plotWdg.plot(x, y, pen=pg.mkPen('CACACA',  width=5), symbol='o', symbolPen ='b', symbolBrush = 0.2)        
        self.plotWdg.getViewBox().autoRange(items=self.plotWdg.getPlotItem().listDataItems())        
