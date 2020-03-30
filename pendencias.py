from glob import glob
from os import path
from qgis.core import *
from qgis.gui import *
from collections import defaultdict
import qgis.utils
from qgis.gui import QgsMessageBar
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt, QVariant
from PyQt5.QtCore import QSettings, QTranslator, QVersionNumber, QCoreApplication, Qt, QObject, pyqtSignal 
from PyQt5.QtGui import QIcon, QFont, QColor, QIntValidator
from PyQt5.QtWidgets import QAction, QDialog, QFormLayout, QTableWidgetItem, QFileDialog, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit
from qgis.core import (QgsUnitTypes,
                       QgsLayout,
                       QgsLayoutItemPage,
                       QgsLayoutGuide,
                       QgsLayoutObject,
                       QgsProject,
                       QgsPrintLayout,
                       QgsLayoutItemGroup,
                       QgsLayoutItem,
                       QgsLayoutItemHtml,
                       QgsProperty,
                       QgsLayoutPageCollection,
                       QgsLayoutMeasurement,
                       QgsLayoutFrame,
                       QgsFillSymbol,
                       QgsReadWriteContext,
                       QgsLayoutItemMap,
                       QgsLayoutItemLabel,
                       QgsLayoutSize,
                       QgsLayoutPoint)

from qgis.PyQt.QtXml import QDomDocument
# Initialize Qt resources from file resources.py
import locale
# Import the code for the dialog
import os.path
from osgeo import ogr
import os
from qgis.core import *
from qgis.gui import *
from .helper_functions import HelperFunctions

class AnalisaPendencias:
    iface = None
    h = None

    def __init__ (self, iface, helper):
        self.iface = iface
        self.h = helper

    def AnalisaFaltaDeNomes(self, trechos):
        selected_fid = []
        for tr in trechos:
            #self.iface.messageBar().pushMessage("Erro", str(len(tr[self.h.readValueFromProject("SEG_NAME_C")])) , level=Qgis.Critical, duration=20)
            if (tr[self.h.readValueFromProject("SEG_NAME_C")] == NULL):
                selected_fid.append(tr.id())
        
        if len(selected_fid)> 0 :
            return selected_fid
        else:
            return None
    
    def AnalisaNomeRepetido(self, trechos):
        d = defaultdict(list)
        selected_fid = []

        for tr in trechos:
            d[tr[self.h.readValueFromProject("SEG_NAME_C")]].append(tr.id())
        
        for nome,ids in d.items():
            if len(ids) > 1:
                selected_fid.extend(ids)

        if len(selected_fid)> 0 :
            return selected_fid
        else:
            return None

    def AnalisaDoisVertices(self, trechos):
        selected_fid = []

        for tr in trechos:
            vertices =  tr.geometry()
            vertices.convertToSingleType()
            vertices = vertices.asPolyline()
            if len(vertices) <2:
                selected_fid.append(tr.id())
        
        if len(selected_fid)> 0 :
            return selected_fid
        else:
            return None

    def AnalisaExtensaoZero(self, trechos):
        selected_fid = []
        for tr in trechos:
            geom = tr.geometry()
            if geom.length() == 0.00:
                selected_fid.append(tr.id())

        if len(selected_fid)> 0 :
            return selected_fid
        else:
            return None

    def AnalisaDoisNos(self, trechos, nos):
        selected_fid = []

        nos_dict = {f.id(): f for f in nos.getFeatures()}
        indice_espacial = QgsSpatialIndex(nos.getFeatures())

        for tr in trechos:
            geom = tr.geometry()
            geom.convertToSingleType()
            if not nos_dict:
                selected_fid.append(tr.id())
            else:
                pt1 = nos_dict[indice_espacial.nearestNeighbor(geom.asPolyline()[-1],1)[0]]
                pt1 = pt1.geometry().asPoint()
                pt2 = nos_dict[indice_espacial.nearestNeighbor(geom.asPolyline()[0],1)[0]]
                pt2 = pt2.geometry().asPoint()
                if not ((pt1.x() == geom.asPolyline()[-1].x())and(pt1.y() == geom.asPolyline()[-1].y())):
                    selected_fid.append(tr.id())
                elif not ((pt2.x() == geom.asPolyline()[0].x())and(pt2.y() == geom.asPolyline()[0].y())):
                    selected_fid.append(tr.id())


        if len(selected_fid)> 0 :
            return selected_fid
        else:
            return None        

    def AnalisarPendencias(self, apenas_selecionados=False):
        cmd = QgsProject.instance().readEntry("AutGeoAtt", "NODE_LAYER")[0]
        lst = QgsProject.instance().mapLayersByName(cmd)
        if lst:
            nos = lst[0]
            camada = self.h.GetLayer()
            if apenas_selecionados:
                vetores = camada.selectedFeatures()
            else:
                vetores = camada.getFeatures()

            dicionario = [f for f in vetores]
            #self.iface.messageBar().pushMessage("Dicionario", str(len(dicionario)) , level=Qgis.Critical, duration=5)

            teste3 = self.AnalisaDoisVertices(dicionario)
            if teste3 is not None:
                camada.removeSelection()
                camada.select(teste3)
                #self.iface.messageBar().pushMessage("Erro", str(teste3), level=Qgis.Critical, duration=5)
                self.iface.mapCanvas().setSelectionColor( QColor("red") )
                self.iface.messageBar().pushMessage(h.tr("Error"), str(len(teste3)) + " " + self.h.tr("selected patch(es) does not have both vertices"), level=Qgis.Critical, duration=5)
                return False

            teste1 = self.AnalisaFaltaDeNomes(dicionario)
            if teste1 is not None:
                camada.removeSelection()
                camada.select(teste1)
                self.iface.mapCanvas().setSelectionColor( QColor("red") )
                self.iface.messageBar().pushMessage(self.h.tr("Error"), str(len(teste1)) + " " + self.h.tr("selected patch(es) does not have name(s)"), level=Qgis.Critical, duration=5)
                return False
            
            teste2 = self.AnalisaNomeRepetido(dicionario)
            if teste2 is not None:
                camada.removeSelection()
                camada.select(teste2)
                self.iface.mapCanvas().setSelectionColor( QColor("red") )
                self.iface.messageBar().pushMessage(self. h.tr("Error"), str(len(teste2)) + " " + self.h.tr("selected patch(es)  have repeated names"), level=Qgis.Critical, duration=5)
                return False

            teste5 = self.AnalisaExtensaoZero(dicionario)
            if teste5 is not None:
                camada.removeSelection()
                camada.select(teste5)
                #self.iface.messageBar().pushMessage("Erro", str(teste4), level=Qgis.Critical, duration=5)
                self.iface.mapCanvas().setSelectionColor( QColor("red") )
                self.iface.messageBar().pushMessage(self.h.tr("Error"), str(len(teste5)) + " " + self.h.tr("selected patch(es)  have 0 (zero) extension"), level=Qgis.Critical, duration=5)
                return False

            teste4 = self.AnalisaDoisNos(dicionario, nos)
            if teste4 is not None:
                camada.removeSelection()
                camada.select(teste4)
                #self.iface.messageBar().pushMessage("Erro", str(teste4), level=Qgis.Critical, duration=5)
                self.iface.mapCanvas().setSelectionColor( QColor("red") )
                self.iface.messageBar().pushMessage(self.h.tr("Error"), str(len(teste4)) + " " + self.h.tr("selected patch(es) does not have nodes in one or two vertices"), level=Qgis.Critical, duration=5)
                return False


            


            #Chegou até aqui é porque houve sucesso em todos os testes.
            self.iface.messageBar().pushMessage(self.h.tr("Sucess"), self.h.tr("No nonconformities were found"), level=Qgis.Success, duration=5)
            return True
        else:
            self.iface.messageBar().pushMessage(self.h.tr("Error"), self.h.tr("Node layer not found"), level=Qgis.Critical, duration=5)


