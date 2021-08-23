from .ui.ProfileWidgetUi import Ui_ProfileWidget
from qgis.PyQt.QtWidgets import QDockWidget
from qgis.PyQt.QtCore import *
from qgis.core import QgsProject, QgsWkbTypes, QgsPointXY, QgsRasterLayer, QgsRaster
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
        layout = self.frame_for_plot.layout()
        while layout.count():
            child = layout.takeAt(0)
            child.widget().deleteLater()
        self.plotWdg = self.set_plot_widget()
        layout.addWidget(self.plotWdg)

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
        profileLayerName = self.layerComboBox.currentText()
        interval = int(self.distanceDoubleSpinBox.value())
        col_seg_att_name = self.h.readValueFromProject("SEG_NAME_C")
        layer = sorted(self.h.GetLayer().selectedFeatures(), key=lambda x: x.attribute(col_seg_att_name))
        virtualLayer  = vLayer("nameVirtual", "Point")
        rasterLayer = QgsProject.instance().mapLayersByName(profileLayerName)[0]
        xRaster = []
        yRaster = []
        y = []
        x = []
        xVal = 0
        for i in layer:
            col_seg = i.attribute(col_seg_att_name)
            line = i.geometry()
            for part in line.get():
                line_start = part[0]
                line_end = part[-1]
                pointm = virtualLayer.diff(line_end, line_start)
                cosa,cosb = virtualLayer.dirCos(pointm)
                lg = virtualLayer.length(line_end, line_start)
                for i in range(interval, int(lg) ,interval):
                    point = QgsPointXY(line_start.x()  + (i * cosa), line_start.y() + (i*cosb))
                    ident = rasterLayer.dataProvider().identify(point, QgsRaster.IdentifyFormatValue)
                    virtualLayer.createPoint(point)
                    yVal = list(ident.results().values())[0]
                    xVal = 0 if not xRaster else (xVal + interval)
                    yRaster.append(yVal)
                    xRaster.append(xVal)
                    self.plotWdg.plot(xRaster, yRaster, pen=pg.mkPen( 'r',  width=2) , name = col_seg)
            data = Calculation.getActiveProfileData(col_seg)
            for n in data.keys():
                for col in data[n]:
                    x.append(0 if col['x_initial'] == None else col['x_initial'])
                    x.append(col['x_final'])
                for col in data[n]:
                    initialPointY = QgsPointXY(col['geom_x_initial'], col['geom_y_initial'])
                    iPy = rasterLayer.dataProvider().identify(initialPointY, QgsRaster.IdentifyFormatValue)
                    finalPointY = QgsPointXY(col['geom_x_final'], col['geom_y_final'])
                    fPy = rasterLayer.dataProvider().identify(finalPointY, QgsRaster.IdentifyFormatValue)
                    y.append(list(iPy.results().values())[0] - col['y_initial'])
                    y.append(list(fPy.results().values())[0] - col['y_final'])

        #TODO; another button to activate the new point layer
        #virtualLayer.displayLayer

        self.plotWdg.plot(x, y, pen=pg.mkPen( 'g',  width=3), symbol='o')
        self.plotWdg.getViewBox().autoRange(items=self.plotWdg.getPlotItem().listDataItems())