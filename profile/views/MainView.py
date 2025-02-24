from .ui.ProfileWidgetUi import Ui_ProfileWidget
from qgis.PyQt.QtWidgets import QDockWidget
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.core import QgsProject, QgsPointXY, QgsVectorLayer
from qgis.gui import *
from ...base.helper_functions import HelperFunctions
from ...base.rasterinterpolator import RasterInterpolator
from .. import pyqtgraph as pg
from ..utils.vLayer import vLayer
from ..utils.helpers import get_rounded_attr

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

VIRTUAL_LAYER_DEFAULT_NAME = "Profile nodes"

class MainView(QDockWidget, Ui_ProfileWidget):
    def __init__(self, iface):
        QDockWidget.__init__(self)
        self.setupUi(self)
        self.location = Qt.BottomDockWidgetArea
        self.h = HelperFunctions(iface)
        self.opts = {
            'area_fill_margin':1.5,
            'pipe_width': 0.05,
            'device_width': 0.8
        } 
        
        self.layout = self.frame_for_plot.layout()
        self.plotWdg = self.set_plot_widget()
        self.layout.addWidget(self.plotWdg)

        #cursor
        self.show_cursor = self.showCursorCheckBox.isChecked()
        self.current_cursor_position = QgsVertexMarker(iface.mapCanvas())
        self.current_cursor_position.setColor(QColor(Qt.red))
        self.current_cursor_position.setIconSize(5)
        self.current_cursor_position.setIconType(QgsVertexMarker.ICON_BOX)  # or ICON_CROSS, ICON_X
        self.current_cursor_position.setPenWidth(3)
       
        #initialize layers
        self.layers = {}
        self.rasterLayer = None
        self.virtualLayer = vLayer(VIRTUAL_LAYER_DEFAULT_NAME, "Point")
        self.area_fill_layer = None
        self.devices_layer = None
        self.pipesBackgroung = None
        self.waterBackground = None
        self.devices = None
        self.pipes = None
        self.labels = None
        self.projectNodesLayer = None
        self.projectSegmentsLayer = None
        
        # signals
        self.plotWdg.scene().sigMouseMoved.connect(self.mouseMoved)
        self.plotWdg.sigRangeChanged.connect(self.onRangeChanged)
        self.showCursorCheckBox.clicked.connect(self.setCursorVisibility)
        self.showLayerCheckBox.clicked.connect(self.setVirtualLayerVisibility)
        self.updateButton.clicked.connect(self.updatePlot)
        #self.virtualLayer.on

        self.nodeTypeFieldComboBox.currentIndexChanged.connect(lambda index: self.on_index_changed(index, self.nodeTypeFieldComboBox))
        self.nodeCFFieldComboBox.currentIndexChanged.connect(lambda index: self.on_index_changed(index, self.nodeCFFieldComboBox))
        self.depthUpFieldComboBox.currentIndexChanged.connect(lambda index: self.on_index_changed(index, self.depthUpFieldComboBox))
        self.depthDownFieldComboBox.currentIndexChanged.connect(lambda index: self.on_index_changed(index, self.depthDownFieldComboBox))
        self.adoptedDiameterFieldComboBox.currentIndexChanged.connect(lambda index: self.on_index_changed(index, self.adoptedDiameterFieldComboBox))
        self.slopeFieldComboBox.currentIndexChanged.connect(lambda index: self.on_index_changed(index, self.slopeFieldComboBox))
        self.waterLevelEndFieldComboBox.currentIndexChanged.connect(lambda index: self.on_index_changed(index, self.waterLevelEndFieldComboBox))

        self.loadLayersCombobox()

    def on_index_changed(self, index, combo):
        if index == -1:
            combo.setStyleSheet("QComboBox { border: 1px solid red; }")
        else:
            combo.setStyleSheet("")

    def loadLayersCombobox(self):
    
        # elevation layers combo
        layer_list = []
        for layer in QgsProject.instance().mapLayers().values():
            if (layer.type() == layer.RasterLayer) or \
                (layer.type() == layer.MeshLayer) or \
                (layer.type() == layer.PluginLayer and layer.LAYER_TYPE == 'selafin_viewer'):
                layer_list.append(layer.name())
        self.layerComboBox.addItems(layer_list)
        
        # Attr mapping
        segments_layer = self.h.GetLayer()
        nodes_layer = self.h.GetNodeLayer()

        self.nodeTypeFieldComboBox.setLayer(nodes_layer)
        self.nodeCFFieldComboBox.setLayer(nodes_layer)
        self.depthUpFieldComboBox.setLayer(segments_layer)
        self.depthDownFieldComboBox.setLayer(segments_layer)
        self.adoptedDiameterFieldComboBox.setLayer(segments_layer)
        self.slopeFieldComboBox.setLayer(segments_layer)
        self.waterLevelEndFieldComboBox.setLayer(segments_layer)
        
        self.nodeTypeFieldComboBox.setField('Nodo_tipo')
        self.nodeCFFieldComboBox.setField('CF_nodo_2')
        self.depthUpFieldComboBox.setField('h_col_p1')
        self.depthDownFieldComboBox.setField('h_col_p2')
        self.adoptedDiameterFieldComboBox.setField('DN')
        self.slopeFieldComboBox.setField('S')
        self.waterLevelEndFieldComboBox.setField('yrel_f')


    def setCursorVisibility(self):
        """ show/hide cursor from map and profile"""
        checked = self.showCursorCheckBox.isChecked()
        self.show_cursor = checked
        if not self.show_cursor:
            #clean widget
            self.current_cursor_position.hide()
            for item in self.plotWdg.allChildItems():
                    if str(type(item)) == "<class 'red_basica.profile.pyqtgraph.graphicsItems.InfiniteLine.InfiniteLine'>":
                        if item.name() == 'cross_vertical':
                            item.hide()
                        elif item.name() == 'cross_horizontal':
                            item.hide()
                    elif str(type(item)) == "<class 'red_basica.profile.pyqtgraph.graphicsItems.TextItem.TextItem'>":
                        if item.textItem.toPlainText()[0] == 'X':
                            item.hide()
                        elif item.textItem.toPlainText()[0] == 'Y':
                            item.hide()

    def setVirtualLayerVisibility(self):
        """ show/hide layer from layer tree """        
        checked = self.showLayerCheckBox.isChecked()        
        if not self.virtualLayer.isValid():
            self.virtualLayer = vLayer(VIRTUAL_LAYER_DEFAULT_NAME, "Point")        
        self.virtualLayer.setVisibility(checked)
                

    def clearLayers(self):
        """ remove layers and items from widget """        
        if self.area_fill_layer:
            self.plotWdg.removeItem(self.area_fill_layer)
        if self.devices_layer:
            self.plotWdg.removeItem(self.devices_layer)
        if self.waterBackground:
            self.plotWdg.removeItem(self.waterBackground)
        if self.pipesBackgroung:
            self.plotWdg.removeItem(self.pipesBackgroung)
        if self.labels:
            for item in self.labels:
                self.plotWdg.removeItem(item['label'])
        
        for k in self.layers.keys():
            self.layers[k].clear()


    def set_plot_widget(self):
        """ creates instance of pg.PlotWidget and sets initial config """
        plotWdg = pg.PlotWidget()
        plotWdg.showGrid(True,True,int(1))
        datavline = pg.InfiniteLine(0, angle=90 ,pen=pg.mkPen('b',  width=1) , name = 'cross_vertical' )
        datahline = pg.InfiniteLine(0, angle=0 , pen=pg.mkPen('b',  width=1) , name = 'cross_horizontal')
        plotWdg.addItem(datavline)
        plotWdg.addItem(datahline)
        #cursor
        xtextitem = pg.TextItem('X : /', color = (0,0,0), border = pg.mkPen(color=(0, 0, 0),  width=1), fill=pg.mkBrush('w'), anchor=(0,1))
        ytextitem = pg.TextItem('Y : / ', color = (0,0,0) , border = pg.mkPen(color=(0, 0, 0),  width=1), fill=pg.mkBrush('w'), anchor=(0,0))
        plotWdg.addItem(xtextitem)
        plotWdg.addItem(ytextitem)

        plotWdg.getViewBox().autoRange(items=[])
        plotWdg.getViewBox().disableAutoRange()
        plotWdg.getViewBox().border = pg.mkPen(color=(0, 0, 0),  width=1)
        return plotWdg
    
    
    def onRangeChanged(self, r):
        axX = self.plotWdg.getAxis('bottom').range
        range = axX[1] - axX[0]
        for item in self.labels:
            if range < 15:
                item['label'].show()
            else:
                if item['extension'] > 25 and range <= 95:
                    item['label'].show()
                if item['extension'] <= 25 and range <= 30:
                    item['label'].show()
                if item['extension'] <= 25 and range > 30:
                    item['label'].hide()
                if  range > 95:
                    item['label'].hide()
        return r


    def mouseMoved(self, pos):
        if self.show_cursor and self.plotWdg.sceneBoundingRect().contains(pos):
            range = self.plotWdg.getViewBox().viewRange()
            mousePoint = self.plotWdg.getViewBox().mapSceneToView(pos)
            x_cursor = mousePoint.x()
            y_cursor = mousePoint.y()
            if x_cursor is not None and y_cursor is not None:
                    for item in self.plotWdg.allChildItems():
                        if str(type(item)) == "<class 'red_basica.profile.pyqtgraph.graphicsItems.InfiniteLine.InfiniteLine'>":
                            if item.name() == "cross_vertical":
                                item.show()
                                item.setPos(x_cursor)
                            elif item.name() == "cross_horizontal":
                                item.show()
                                item.setPos(y_cursor)
                        elif str(type(item)) == "<class 'red_basica.profile.pyqtgraph.graphicsItems.TextItem.TextItem'>":
                            if item.textItem.toPlainText()[0] == "X":
                                item.show()
                                item.setText("X : " + str(round(x_cursor, 3)))
                                item.setPos(x_cursor, range[1][0])
                            elif item.textItem.toPlainText()[0] == "Y":
                                item.show()
                                item.setText("Y : " + str(round(y_cursor, 3)))
                                item.setPos(range[0][0], y_cursor)
            self.updateCursorOnMap(x_cursor)
        
    
    def updateCursorOnMap(self, x_cursor):
        """ Draw cursor position on map """
        features = self.virtualLayer.getFeatures()
        d = (self.distanceDoubleSpinBox.value() / 2)
        points = [ f.geometry().asPoint() for f in features if abs(float(x_cursor) - float(f['x_axis'])) < d]
        if len(points)>0:
            point = points[0]
            self.current_cursor_position.setCenter(point)
            self.current_cursor_position.show()
        else:
            self.current_cursor_position.hide()
        

    def resetDevices(self):
        """ set default inspection devices structure """
        self.devices = {'x':[], 'y':[], 'h':[] }
        return self.devices

    def resetPipes(self):
        """ set default pipes structure """
        self.pipes =  {
            'top': {'x':[], 'y':[]},
            'bottom': {'x':[], 'y':[]},
            'water': {'x':[], 'y':[]}
        }
        return self.pipes
    
    def resetLabels(self):
        self.labels = []
        return self.labels
    
    def addPipe(self, pipe, x_axis_position):
        """ adds a single pipe to pipes -> returns coords """
        try:
            pipe_extension = pipe.get('extension')
            x1 = x_axis_position
            x2 = x_axis_position + pipe_extension
            rasterInterpolator = RasterInterpolator(self.rasterLayer, 1, 1)
            initialPointY = QgsPointXY(pipe.get('x_i'), pipe.get('y_i'))
            iPy = rasterInterpolator.interpolate(initialPointY)
            finalPointY = QgsPointXY(pipe.get('x_f'), pipe.get('y_f'))
            fPy = rasterInterpolator.interpolate(finalPointY)
            y1 = iPy - float(pipe.get('h_i'))
            y2 = fPy - float(pipe.get('h_f'))

            displacement = self.opts['device_width'] / 2
            self.pipes['bottom']['x'].extend([x1 + displacement, x2 - displacement])
            self.pipes['bottom']['y'].extend([y1, y2])

            self.pipes['top']['x'].extend([x1 + displacement, x2 - displacement])
            self.pipes['top']['y'].extend([y1 + self.opts['pipe_width'], y2 + self.opts['pipe_width']])

            flow_porc = pipe.get('flow_porc', 0)
            flow_width = (flow_porc * self.opts['pipe_width'])/100
            self.pipes['water']['x'].extend([x1 + displacement, x2 - displacement])
            self.pipes['water']['y'].extend([y1 + flow_width, y2 + flow_width])

            self.addLabel(
                (x1 + (x2-x1)/2) -0.5, 
                y1 + (self.opts['device_width']/2), 
                "<div align='center'><b>{}</b><br>{}m<br>Ø{}<br>{}</div>".format(
                    pipe.get('col_seg'),
                    pipe_extension,
                    pipe.get('diameter'),
                    pipe.get('slope')
                ),
                center=True,
                extension=pipe_extension
            )
            return dict(x1=x1, y1=y1, x2=x2, y2=y2)
        except:
            return False        

    def drawPipes(self):
        for p in self.pipes.keys():
            layerName = 'pipe-{}'.format(p)
            self.layers[layerName] = self.plotWdg.plot(self.pipes[p]['x'], self.pipes[p]['y'], pen=pg.mkPen('000000',  width=0.8))
        self.pipesBackgroung = pg.FillBetweenItem(self.layers['pipe-bottom'], self.layers['pipe-top'], brush=pg.mkBrush(255, 255, 255, 100))
        self.waterBackground = pg.FillBetweenItem(self.layers['pipe-water'], self.layers['pipe-bottom'], brush=pg.mkBrush(0, 0, 255, 50))
        self.plotWdg.addItem(self.pipesBackgroung)
        self.plotWdg.addItem(self.waterBackground)


    def isValidSelection(self, features):
        last_feature = None
        is_valid = True
        for f in features:
            if is_valid:
                if last_feature is None:
                    last_feature = f
                else:
                    current_line = f.geometry()
                    last_line = last_feature.geometry()
                    current_start_point = current_line.vertexAt(0)
                    last_end_point = last_line.vertexAt(1)
                    last_feature = f
                    if current_start_point != last_end_point:
                        is_valid = False
                        break
        return is_valid


    def updatePlot(self):
        """ draw plot with current features selection"""
        if not self.virtualLayer.isValid():
            self.virtualLayer = vLayer(VIRTUAL_LAYER_DEFAULT_NAME, "Point") 

        self.clearLayers()
        self.virtualLayer.clear()
        profileLayerName = self.layerComboBox.currentText()
        interval = self.distanceDoubleSpinBox.value()
        
        # segments layer attributes
        COLSEG_FIELD = self.h.readValueFromProject("SEG_NAME_C")
        EXTENSION_FIELD = self.h.readValueFromProject("EXT_FIELD_NAME")
        X_I_FIELD = self.h.readValueFromProject("BEG_LINE_COORD_E")
        Y_I_FIELD = self.h.readValueFromProject("BEG_LINE_COORD_N")
        X_F_FIELD = self.h.readValueFromProject("FIN_LINE_COORD_E")
        Y_F_FIELD = self.h.readValueFromProject("FIN_LINE_COORD_N")
        H_I_FIELD = self.depthUpFieldComboBox.currentField()
        H_F_FIELD = self.depthDownFieldComboBox.currentField()
        DN_FIELD = self.adoptedDiameterFieldComboBox.currentField()
        SLOPE_FIELD = self.slopeFieldComboBox.currentField()
        FLOW_PORC_FIELD = self.waterLevelEndFieldComboBox.currentField()
        
        if '' in [H_I_FIELD, H_F_FIELD, DN_FIELD, SLOPE_FIELD, FLOW_PORC_FIELD]:
            self.h.ShowWarning('Missing required attributes from Path layer.')
            return False

        # nodes layer attributes
        NODE_ID_FIELD = "Id_NODO_(n"
        COTA_FIELD = self.h.readValueFromProject("COTA")
        CF_FIELD = self.nodeCFFieldComboBox.currentField()
        NODE_TYPE_FIELD = self.nodeTypeFieldComboBox.currentField()

        if '' in [COTA_FIELD, CF_FIELD, NODE_TYPE_FIELD]:
            self.h.ShowWarning('Missing required attributes from Nodes layer.')
            return False

        selected_features = self.h.GetLayer().selectedFeatures()
        features = sorted(selected_features, key=lambda x: x[COLSEG_FIELD])

        if len(features) == 0:
            return False

        if not self.isValidSelection(features):
            self.h.ShowWarning('You have selected one or more sections that do not belong to another.')
            return False

        self.rasterLayer = QgsProject.instance().mapLayersByName(profileLayerName)[0]
        rasterInterpolator = RasterInterpolator(self.rasterLayer, 1, 1)
        xRaster = []
        yRaster = []
        self.resetDevices()
        self.resetPipes()
        self.resetLabels()
        xVal = None

        for f in features:
            col_seg = f.attribute(COLSEG_FIELD)
            line = f.geometry()
            current_extension = 0 if xVal is None else xExt2
            xExt2 = f[EXTENSION_FIELD] if xVal is None else xExt2 + f[EXTENSION_FIELD]

            #add pipe
            pipe_dict = dict(
                col_seg = col_seg,
                x_i = f[X_I_FIELD],
                x_f = f[X_F_FIELD],
                y_i = f[Y_I_FIELD],
                y_f = f[Y_F_FIELD],
                h_i = f[H_I_FIELD],
                h_f = f[H_F_FIELD],
                diameter = f[DN_FIELD],
                slope = get_rounded_attr(f, SLOPE_FIELD, 5),
                flow_porc= get_rounded_attr(f, FLOW_PORC_FIELD, 0),
                extension = f[EXTENSION_FIELD]
            )
            pipe = self.addPipe(pipe_dict, current_extension)
            if pipe == False:
                self.h.ShowError(f"Unable to create profile for: {col_seg}")
                return False

            x1 = pipe['x1']
            y1 = pipe['y1']
            x2 = pipe['x2']
            y2 = pipe['y2']

            #set xVal if dosnt exist
            if xVal is None:
                xVal = x1

            #add inspection device
            for node in self.h.GetNodeLayer().getFeatures():
                if node[NODE_ID_FIELD] == col_seg:
                    inspection_type_up = node[NODE_TYPE_FIELD]
                    el_terr_up = get_rounded_attr(node, COTA_FIELD) 
                    el_col_up = get_rounded_attr(node, CF_FIELD)

            self.devices['x'].extend([x1, x2])
            h1 = float(f[H_I_FIELD])
            h2 = float(f[H_F_FIELD])
            self.devices['h'].extend([h1, h2])
            self.devices['y'].extend([y1 + h1/2, y2 + h2/2])

            self.addLabel(
                (x1 - 0.5), y1, 
                "{}<br>CT = {}<br>CF = {}<br>h = {}".format(
                    inspection_type_up, 
                    el_terr_up if el_terr_up is not None else '', 
                    el_col_up if el_col_up is not None else '', 
                    f[H_I_FIELD]
                ),
                color="red", 
                extension=f[EXTENSION_FIELD]
            )

            #ground layer
            for part in line.get():
                line_start = part[0]
                line_end = part[-1]
                pointm = self.virtualLayer.diff(line_end, line_start)
                cosa,cosb = self.virtualLayer.dirCos(pointm)
                lg = self.virtualLayer.length(line_end, line_start)
                i = 0
                rest = lg % interval
                last = False
                while i <= lg:
                    point_x = line_start.x() + (i * cosa)
                    point_y = line_start.y() + (i * cosb)
                    point = QgsPointXY(point_x, point_y)

                    yVal = rasterInterpolator.interpolate(point)
                    yRaster.append(yVal)
                    xRaster.append(xVal)
                    attributes = {
                        'col_seg': col_seg,
                        'x_axis': xVal,
                        'y_axis': yVal,
                        'x': point_x,
                        'y': point_y,
                        'h': '??'
                    }
                    self.virtualLayer.createPoint(point, attributes)
                    if ((i + rest) == lg):
                        i = lg
                        xVal += rest
                        last = True
                    else:
                        i += interval
                        if not last:
                            xVal += interval

        #draw ground area
        self.layers['ground'] = self.plotWdg.plot(xRaster, yRaster, pen=pg.mkPen('CCCCCC',  width=1))
        lower_y_axis = min(self.devices['y'])
        yGroundBase = [ (lower_y_axis - self.opts['area_fill_margin']) for i in yRaster]
        self.layers['ground_base'] = self.plotWdg.plot(xRaster, yGroundBase, pen=pg.mkPen('CCCCCC',  width=1))
        self.area_fill_layer = pg.FillBetweenItem(self.layers['ground'], self.layers['ground_base'], brush=pg.mkBrush(242, 176, 109, 100))
        self.plotWdg.addItem(self.area_fill_layer)
        self.plotWdg.getViewBox().autoRange(items=self.plotWdg.getPlotItem().listDataItems())

        # layers
        self.virtualLayer.reload()
        self.drawPipes()
        self.drawInspectionDevices()
        self.drawLabels()
        self.setVirtualLayerVisibility()

    def drawInspectionDevices(self):
        self.devices_layer = pg.BarGraphItem(x = self.devices['x'], y = self.devices['y'], height = self.devices['h'], width = self.opts['device_width'], brush ='w') 
        self.plotWdg.addItem(self.devices_layer)

    def drawLabels(self):
        for item in self.labels:
            self.plotWdg.addItem(item['label'],  ignoreBounds = True)

    def addLabel(self, x, y, text, center=False, color='', extension=None):
        label = pg.TextItem('', color=(0,0,0),rotateAxis=(1, 0), anchor=(0,0), angle=0)
        label.setHtml(text)
        label.setPos(x,y)
        label.forgetViewBox()
        if (center):
            it = label.textItem
            option = it.document().defaultTextOption()
            option.setAlignment(QtCore.Qt.AlignCenter)
            it.document().setDefaultTextOption(option)
            it.setTextWidth(it.boundingRect().width())
        if (color == 'red'):
            label.setColor(QColor(255,0,0))
        labelDict = {
            'label': label,
            'extension': extension
        }
        self.labels.append(labelDict)