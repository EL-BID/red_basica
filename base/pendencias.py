from glob import glob
from os import path
from qgis.core import *
from qgis.gui import *
from collections import defaultdict
from PyQt5.QtGui import QColor
from qgis.core import QgsProject

from qgis.PyQt.QtXml import QDomDocument
# Initialize Qt resources from file resources.py
import locale
# Import the code for the dialog
import os.path
from osgeo import ogr
import os
from qgis.core import *
from qgis.gui import *
from string import ascii_letters, digits

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

    def checkInvalidNames(self, features):
        """ find invalid names """
        selected_fid = []
        allowed_chars = ascii_letters + digits + '-' + '_' + '.'
        for f in features:
            n = f[self.h.readValueFromProject("SEG_NAME_C")]
            if ( n.find('--') != -1 or set(n).difference(allowed_chars)): 
                selected_fid.append(f.id())                    

        if len(selected_fid)> 0 :
            return selected_fid
        else:
            return None

    def checkDiscontinuousSegments(self, features):
        """ check when segment is not initial nor final and has no prev col 
            returns discontinuous segments or none
        """
        
        #project info
        beg_line_coord_e = self.h.readValueFromProject("BEG_LINE_COORD_E")
        beg_line_coord_n = self.h.readValueFromProject("BEG_LINE_COORD_N")
        fin_line_coord_e = self.h.readValueFromProject("FIN_LINE_COORD_E")
        fin_line_coord_n = self.h.readValueFromProject("FIN_LINE_COORD_N")
        seg_name = self.h.readValueFromProject("SEG_NAME")
        seg_name_c = self.h.readValueFromProject("SEG_NAME_C")

        lstMinFeatures = []        
        for ft in features:                           
            minFeatureObj = {}
            minFeatureObj["BEG_LINE_COORD_E"] = ft[beg_line_coord_e]
            minFeatureObj["BEG_LINE_COORD_N"] = ft[beg_line_coord_n]
            minFeatureObj["FIN_LINE_COORD_E"] = ft[fin_line_coord_e]
            minFeatureObj["FIN_LINE_COORD_N"] = ft[fin_line_coord_n]
            minFeatureObj["SEG_NAME"] = ft[seg_name]
            minFeatureObj["SEG_NAME_C"] = ft[seg_name_c]            
            lstMinFeatures.append(minFeatureObj)

        fids = []
        for f in features:
            #AUX_TRM_I and AUX_TRM_F
            isBegin,isEnd,totalEnd = self.h.Get_Aux_Trm(f.id(),features)
            #TRM_(N-1)_A           
            hasPrevCol = True if self.h.Get_Feature_On_Index(lstMinFeatures,f,-1) != None else False      
            #TRM_(N-1)_B
            hasColM = True if self.h.Get_Feature_On_Index(lstMinFeatures,f,-1,False) != None else False  #this may be redundant
            if not isBegin and not isEnd and not hasPrevCol and hasColM:
                fids.append(f.id())        

        return fids if len(fids)>0 else None

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

            testInvalidNames = self.checkInvalidNames(dicionario)
            if testInvalidNames is not None:
                camada.removeSelection()
                camada.select(testInvalidNames)
                self.iface.mapCanvas().setSelectionColor( QColor("red") )
                self.iface.messageBar().pushMessage(self.h.tr("Error"), str(len(testInvalidNames)) + " " + self.h.tr("selected patch(es) have invalid name(s)"), level=Qgis.Critical, duration=5)
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

            test6 = self.checkDiscontinuousSegments(dicionario)
            if test6 is not None:
                camada.removeSelection()
                camada.select(test6)                
                self.iface.mapCanvas().setSelectionColor( QColor("red") )
                self.iface.messageBar().pushMessage(self.h.tr("Error"), str(len(test6)) + " " + self.h.tr("The selected segments are not connected to a previous segment and are neither beginning nor ending"), level=Qgis.Critical, duration=5)
                return False


            #Chegou até aqui é porque houve sucesso em todos os testes.
            self.iface.messageBar().pushMessage(self.h.tr("Sucess"), self.h.tr("No nonconformities were found"), level=Qgis.Success, duration=5)
            return True
        else:
            self.iface.messageBar().pushMessage(self.h.tr("Error"), self.h.tr("Node layer not found"), level=Qgis.Critical, duration=5)


