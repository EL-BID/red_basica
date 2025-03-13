import os
from datetime import datetime
from qgis.PyQt.QtCore import QObject, QLocale
from qgis.PyQt.QtWidgets import QDialog, QFileDialog
from qgis.utils import iface
from qgis.core import *
from .dialog_ui import Ui_SwmmExportDialog
from ..helper_functions import HelperFunctions

class ExportSwmmFile(QDialog, Ui_SwmmExportDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.iface = iface
        self.h = HelperFunctions(iface)
        locale = QLocale().name()
        self.lang = locale[0:2] if locale[0:2] in ('en', 'es', 'pt') else 'en'
        self.sections = ('TITLE', 'OPTIONS', 'JUNCTIONS', 'OUTFALLS', 'CONDUITS',
                            'XSECTIONS', 'REPORT', 'MAP', 'COORDINATES')
        self.line_tab = '\t'
        self.segments = []
        self.nodes = []
        self.flowType = "qi"

        self.buttonBox.rejected.connect(self.onCancel)
        self.buttonBox.accepted.connect(self.onSave)
        self.selectFileButton.clicked.connect(self.selectInputFile)
        self.initialFlowRadioButton.clicked.connect(self.onFlowTypeChange)
        self.finalFlowRadioButton.clicked.connect(self.onFlowTypeChange)

    def onCancel(self):
        self.hide()
    
    def onSave(self):
        if 0 < len(self.fileName.text()):            
            try:
                self.setCrs(QgsProject.instance().crs())
                self.writeFile()
                self.h.ShowMessage("SWMM file created successfully.")
                self.hide()
                return True
            except Exception as e:
                self.h.ShowError("Saving INP file failed: " + str(e))
                self.hide()
        return False

    def onFlowTypeChange(self):
        self.fileName.setText("")
        initialFlowChecked = self.initialFlowRadioButton.isChecked()
        self.flowType = "qi" if initialFlowChecked else "qf"
    
    def selectInputFile(self):
        
        f, __ = QFileDialog.getSaveFileName(
                    self,
                    "INP file",
                    "{}_MyProject_{}.inp".format("saniHUB", self.flowType.upper()),
                    "EPANET INP file (*.inp)",
                )
        self.fileName.setText(f)

    def getFinalNode(self, segment):
        """ """
        nodes_layer = self.h.GetNodeLayer()
        node_id_field = "Id_NODO_(n"
        final_node = ''

        geom = segment.geometry()
        geom.convertToSingleType()
        last_vertex = geom.asPolyline()[-1]
        end_point = QgsGeometry.fromPointXY(last_vertex)
        
        for feature in nodes_layer.getFeatures():
            if feature.geometry().intersects(end_point):
                final_node = feature[node_id_field]
                break

        return final_node
    
    def getNodes(self):
        """ Get list of nodes """

        nodes = []
        layer =  self.h.GetNodeLayer()        
        cf_field = 'CF_nodo'#self.h.readValueFromProject("COTA")
        idx =  layer.fields().lookupField(cf_field)
        if idx == -1:            
            raise ValueError("Unable to find CF_nodo attribute on nodes layer.")
        
        depth_field = 'h_nodo_NT'
        idx =  layer.fields().lookupField(depth_field)
        if idx == -1:            
            raise ValueError("Unable to find h_nodo_NT attribute on nodes layer.")

        id_field = 'Id_NODO_(n'
        idx =  layer.fields().lookupField(id_field)
        if idx == -1:
            raise ValueError("Unable to find Id_NODO_(n attribute on nodes layer.")            
                
        for f in layer.getFeatures():
            geom = f.geometry()
            item = dict(node=f[id_field], elev=f[cf_field], depth=f[depth_field], x=geom.asPoint().x(), y=geom.asPoint().y())
            nodes.append(item)
        
        sorted_nodes = sorted(nodes, key=lambda item: item["node"])
        return sorted_nodes

    def getSegments(self):
        """ Get list of each segment """

        segments = []
        layer =  self.h.GetLayer()
        colseg_id_field = self.h.readValueFromProject("SEG_NAME")
        colseg_field = self.h.readValueFromProject("SEG_NAME_C")
        extension_field = self.h.readValueFromProject('EXT_FIELD_NAME')
        n_field = 'n'  
        dn_field = 'DN'
        drop_field = 'caida_p2_h'
        qi_field = 'Qmed_i'
        qf_field = 'Qmax_f'

        for field in [n_field, dn_field, drop_field, qi_field, qf_field, colseg_id_field]:
            idx =  layer.fields().lookupField(field)
            if idx == -1:
                raise ValueError(f"""Unable to find {field} attribute on patch layer.""")
        
        features = layer.getFeatures()
        for f in features:
            item = dict(
                fid=f.id(),
                initial_node=f[colseg_field],
                final_node=self.getFinalNode(f),
                extension=f[extension_field], 
                c_manning=f[n_field],
                dn_meters= (float(f[dn_field]) / 1000),
                upstream_drop = f[drop_field],
                qi = f[qi_field],
                qf = f[qf_field]
            )
            segments.append(item)

        sorted_segments = sorted(segments, key=lambda item: item["initial_node"])
        return sorted_segments

    def getContent(self, section):
        """  """
        switcher = {
            'TITLE': self.getTitleSection,
            'OPTIONS': self.getOptionsSection,
            'JUNCTIONS': self.getJunctionsSection,
            'OUTFALLS': self.getOutfallsSection,
            'CONDUITS': self.getConduitsSection,
            'XSECTIONS': self.getXsectionsSection,
            'REPORT': self.getReportSection,
            'MAP': self.getMapSection,
            'COORDINATES': self.getCoordinatesSection,
        }
        func = switcher.get(section, lambda: "Invalid Section")
        return func()

    def writeFile(self):
        """ write file """

        filename = self.fileName.text()
        self.inpfile = open(filename, 'w')
        self.nodes = self.getNodes()
        self.segments = self.getSegments()
        for section in self.sections:            
            self.writeSection(section)
        self.inpfile.close()

    def writeSection(self, section):
        """ generate content to a specific section """

        self.writeSectionLabel(section)
        content = self.getContent(section)
        for line in content:
            self.inpfile.write(line + '\n')
        self.inpfile.write('\n')

    def writeSectionLabel(self, section):
        """ Write a section label to the INP file """

        self.inpfile.write('['+section+'] \n')

    def setCrs(self, crs):
        """ Set CRS """

        self.crstransform = False
        canvascrs = self.iface.mapCanvas().mapSettings().destinationCrs()
        if crs.isValid() and canvascrs.isValid():
            self.crstransform = QgsCoordinateTransform(
                crs, canvascrs, QgsProject.instance())
        if self.crstransform.isShortCircuited():
            self.crstransform = False

    def transformXY(self, x, y):
        """ Transform coordinates where necessary to canvas crs """

        if self.crstransform:
            pnt = self.crstransform.transform(QgsPoint(x, y))
            x = pnt.x()
            y = pnt.y()
        return [x, y]

    def clean(self, value):
        """ prevent NULL and round values in INP file """

        if type(value) == float:
            value = round(value, 2)

        v = str(value)
        if 'NULL' == v:
            return ''
        return v

    def getTitleSection(self):
        """ [TITLE] section """

        title = {
                 'pt': 'Sistema de Esgoto',
                 'es': 'Sistema de Alcantarillado',
                 'en': 'Sewerage System'
                }
        lines = ('SaniHUB', title[self.lang])
        return lines

    def getOptionsSection(self):
        """ [OPTIONS] section """

        date = datetime.now()
        lines = ('FLOW_UNITS' + '\t \t' + 'LPS',  # Padrão de unidades Litros por segundo
                 'START_DATE' + '\t \t' + \
                 date.strftime('%m/%d/%Y'),  # Data do projeto
                 'START_TIME' + '\t \t' + '00:00:00',
                 'REPORT_START_DATE' + '\t' + date.strftime('%m/%d/%Y'),
                 'REPORT_START_TIME' + '\t' + '00:00:00',
                 # Data do final do projeto
                 'END_DATE' + '\t \t' + \
                 date.replace(year=date.year+1).strftime('%m/%d/%Y'),
                 'END_TIME' + '\t \t' + '12:00:00',
                 'SWEEP_START' + '\t \t' + '01/01',
                 'SWEEP_END' + '\t \t' + '12/31',
                 # Padrão de entrada dos valores dos degraus (distância do tubo ao fundo do PV)
                 'LINK_OFFSETS' + '\t \t' + 'DEPTH'
                 )
        return lines

    def getJunctionsSection(self):
        """ [JUNCTIONS] section """

        h1 = self.line_tab.join(
            (';;',   'Invert', 'Max.', 'Init.', 'Surcharge', 'Ponded'))
        h2 = self.line_tab.join(
            (';;Name', 'Elev.', 'Depth', 'Depth', 'Depth   ',    'Area'))
        h3 = self.line_tab.join(
            (';;----', '------', '-----', '-----', '--------', '-------'))

        lines = [h1, h2, h3]
        for rec in self.nodes:
            if ('FINAL' not in rec['node']):
                data = [
                    self.clean(rec.get('node', '')),
                    self.clean(rec.get('elev', 0)),
                    self.clean(rec.get('depth', 0)),
                    '0', '0', '0'
                ]
                line = self.line_tab.join(data)
                lines.append(line)
        return lines

    def getOutfallsSection(self):
        """ [OUTFALLS] section """

        h1 = self.line_tab.join(
            (';;', 'Invert', 'Outfall', 'Stage/Table', 'Tide'))
        h2 = self.line_tab.join(
            (';;Name', 'Elev.', 'Type', 'Time Series', 'Gate'))
        h3 = self.line_tab.join(
            (';;----', '-----', '-----', '-----------', '-----'))
        lines = [h1, h2, h3]
        for rec in self.nodes:
            if ('FINAL' in rec['node']):
                data = [
                    self.clean(rec.get('node', '')),
                    self.clean(rec.get('elev', 0)),
                    'FREE',
                    '',
                    'NO'
                ]
                line = self.line_tab.join(data)
                lines.append(line)
        return lines

    def getConduitsSection(self):
        """ [CONDUITS] section """

        h1 = self.line_tab.join(
            (';;',    'Inlet', 'Outlet', '     ',   'Manning', 'Inlet',  'Outlet', 'Init.', 'Max.'))
        h2 = self.line_tab.join(
            (';;Name', 'Node ', 'Node ', 'Length',  'N      ', 'Offset', 'Offset', 'Flow',  'Flow'))
        h3 = self.line_tab.join((';;----', '-----', '------', '-------',
                                 '-------', '------', '------', '-----', '------'))

        lines = [h1, h2, h3]
        for rec in self.segments:
            data = [
                self.clean(rec.get('initial_node', '')),
                self.clean(rec.get('initial_node', '')),
                self.clean(rec.get('final_node', '')),
                self.clean(rec.get('extension',0)),
                self.clean(rec.get('c_manning', 0)),
                '0',
                self.clean(rec.get('upstream_drop',0)),
                self.clean(rec.get(self.flowType, 0)),
                '0'
            ]
            line = self.line_tab.join(data)
            lines.append(line)
        return lines

    def getXsectionsSection(self):
        """ [XSECTIONS] section """

        h1 = self.line_tab.join(
            (';;Link', 'Shape   ', 'Geom1', 'Geom2', 'Geom3', 'Geom4', 'Barrels'))
        h2 = self.line_tab.join(
            (';;----', '--------', '-----', '------', '------', '------', '-------'))

        lines = [h1, h2]
        for rec in self.segments:
            data = [
                self.clean(rec.get('initial_node', '')),
                'CIRCULAR',
                self.clean(rec.get('dn_meters', 0)),
                '0',
                '0',
                '0',
                '1'  # Barrels (should be 0 ?)
            ]
            line = self.line_tab.join(data)
            lines.append(line)
        return lines

    def getReportSection(self):
        """ [REPORT] section """

        return ('INPUT      NO',
                'CONTROLS   NO',
                'SUBCATCHMENTS ALL',
                'NODES ALL',
                'LINKS ALL'
                )

    def getMapSection(self):
        """ [MAP] section """

        canvas = self.iface.mapCanvas()
        # DIMENSIONS
        extent = canvas.extent()
        mins = str(extent.xMinimum()) + ' ' + str(extent.yMinimum())
        maxs = str(extent.xMaximum()) + ' ' + str(extent.yMaximum())
        dim_line = 'DIMENSIONS ' + mins + ' ' + maxs
        # UNITS
        mapunits = 'Meter'  # TODO: check this
        units_line = 'UNITS ' + mapunits

        lines = (dim_line, units_line)
        return lines

    def getCoordinatesSection(self):
        """ [COORDINATES] section """

        h1 = self.line_tab.join((';;Node', 'X-Coord    ', 'Y-Coord    '))
        h2 = self.line_tab.join((';;----', '-----------', '-----------'))

        lines = [h1, h2]
        for rec in self.nodes:
            (x, y) = self.transformXY(rec.get('x'), rec.get('y'))
            data = [
                rec.get('node', ''),
                self.clean(x),
                self.clean(y)
            ]
            line = self.line_tab.join(data)
            lines.append(line)
        return lines
