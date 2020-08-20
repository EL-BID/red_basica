from qgis.utils import iface
from qgis.core import QgsProject, QgsFeatureRequest, QgsExpression
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlQuery
from PyQt5.QtGui import QColor
from ...helper_functions import HelperFunctions
from ...pendencias import AnalisaPendencias
import json
from datetime import datetime
import time
import traceback


class DataController(QObject):
    
    finished = pyqtSignal(object)
    error = pyqtSignal(Exception, basestring)
    progress = pyqtSignal(float)
    info = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.iface = iface
        self.h = HelperFunctions(iface)

    def campo_ordem(self, f):
        return f[self.h.readValueFromProject("SEG_NAME_C")]

    def runVerifications(self):
        """ run each test in pendencias.py before importing data """
        success = True
        fixSegments = False
        info = None
        self.info.emit('running verifications before import')
        try:
            pendencias = AnalisaPendencias(self.iface, self.h)
            cmd = QgsProject.instance().readEntry("AutGeoAtt", "NODE_LAYER")[0]
            lst = QgsProject.instance().mapLayersByName(cmd)
            if lst:
                nodes = lst[0]
                layer = self.h.GetLayer()
                features = [f for f in layer.getFeatures()]

                if success:                    
                    self.progress.emit(2)
                    testVertices = pendencias.AnalisaDoisVertices(features)
                    if testVertices is not None:
                        layer.removeSelection()
                        layer.select(testVertices)
                        info = 'selected patch(es) does not have both vertices'
                        success = False    

                if success:                   
                    self.progress.emit(4)
                    testNames = pendencias.AnalisaFaltaDeNomes(features)
                    if testNames is not None:
                        layer.removeSelection()
                        layer.select(testNames)
                        info = 'selected patch(es) does not have name(s)'
                        success = False
                
                if success:                    
                    self.progress.emit(6)
                    testRepeatedNames = pendencias.AnalisaNomeRepetido(features)
                    if testRepeatedNames is not None:
                        layer.removeSelection()
                        layer.select(testRepeatedNames)
                        info = "selected patch(es)  have repeated names"
                        success = False
                
                if success:
                    self.progress.emit(8)                    
                    testExtension = pendencias.AnalisaExtensaoZero(features)
                    if testExtension is not None:
                        layer.removeSelection()
                        layer.select(testExtension)
                        success = False
                        info = "selected patch(es)  have 0 (zero) extension"
                
                if success:
                    self.progress.emit(10)                    
                    testTwoNodes = pendencias.AnalisaDoisNos(features, nodes)
                    if testTwoNodes is not None:
                        layer.removeSelection()
                        layer.select(testTwoNodes)
                        info = "selected patch(es) does not have nodes in one or two vertices"
                        success = False 
                
                if success:
                    self.progress.emit(15)
                    self.info.emit('checking segments continuity')
                    testContinuity = pendencias.checkDiscontinuousSegments(features)
                    if testContinuity is not None:                        
                        layer.removeSelection()
                        layer.select(testContinuity)                                           
                        info = "Continuity error detected"
                        success = False                                                
                        fixSegments = True
                    else:
                        info = 'ready to import data'
                
                if not success:
                    self.iface.mapCanvas().setSelectionColor( QColor("red") )
                
            else:
                info = self.h.tr("Node layer not found")
                success = False                

        except Exception as e:
            success = False
            info = 'unespected error'
            self.error.emit(e, traceback.format_exc())
            
        self.info.emit(info)
        self.finished.emit({'success':success, 'fix': fixSegments, 'info': info})

    def getJsonData(self):
        start_time = time.time()
        # data_dir = os.path.join(os.path.dirname(__file__), 'data')

        beg_line_coord_e = self.h.readValueFromProject("BEG_LINE_COORD_E")
        beg_line_coord_n = self.h.readValueFromProject("BEG_LINE_COORD_N")
        fin_line_coord_e = self.h.readValueFromProject("FIN_LINE_COORD_E")
        fin_line_coord_n = self.h.readValueFromProject("FIN_LINE_COORD_N")

        qe = self.h.readValueFromProject("QE")
        qei = self.h.readValueFromProject("QEI")
        qef = self.h.readValueFromProject("QEF")
        cota_i = "COTA_I"
        cota_f = "COTA_F"
        cota = self.h.readValueFromProject("COTA")
        mylayer = self.h.GetLayer()

        #to do: handle loading
        # we are not going to have selected features checkbox  
        vetores = mylayer.getFeatures()
        dicionario = [f for f in vetores]

        dicionario.sort(key=self.campo_ordem)
        
        #export data

        lst = QgsProject.instance().mapLayersByName( self.h.readValueFromProject('NODE_LAYER') )
        if lst:
            nodeLayer = lst[0]

        if nodeLayer:
            qe_idx = nodeLayer.fields().lookupField(qe)
            qei_idx = nodeLayer.fields().lookupField(qei)
            qef_idx = nodeLayer.fields().lookupField(qef)
            cota_idx = nodeLayer.fields().lookupField(cota)
        
        fieldnames = []
        fieldnames.append("AUX_TRM_I")
        fieldnames.append("AUX_TRM_F")
        fieldnames.append(self.h.readValueFromProject("SEG_NAME"))
        fieldnames.append(self.h.readValueFromProject("SEG_NAME_C"))
        fieldnames.append(self.h.readValueFromProject("EXT_FIELD_NAME"))
        fieldnames.append("TRM_(N-1)_A")
        fieldnames.append("TRM_(N-1)_B")
        fieldnames.append("TRM_(N-1)_C")
        if isinstance(qe, basestring):
            fieldnames.append(qe)
        else:
            fieldnames.append("QE")

        if isinstance(qef, basestring):
            fieldnames.append(qef)
        else:
            fieldnames.append("QEF")
            
        if isinstance(qei, basestring):
            fieldnames.append(qei)
        else:
            fieldnames.append("QEI")


        fieldnames.append(self.h.readValueFromProject("AUX_PROF_I"))
        fieldnames.append(self.h.readValueFromProject("AUX_POS"))
        fieldnames.append(self.h.readValueFromProject("AUX_PROF_F"))
        fieldnames.append(cota_i)
        fieldnames.append(cota_f)
        fieldnames.append("TRM_(N+1)")
        fieldnames.append("ID_TRM")
        fieldnames.append(beg_line_coord_e)
        fieldnames.append(beg_line_coord_n)
        fieldnames.append(fin_line_coord_e)
        fieldnames.append(fin_line_coord_n)
        fieldnames.append(self.h.readValueFromProject("AUX_PAV_1"))
        fieldnames.append(self.h.readValueFromProject("AUX_PAV_2"))
        fieldnames.append(self.h.readValueFromProject("AUX01"))
        fieldnames.append(self.h.readValueFromProject("AUX02"))
        fieldnames.append(self.h.readValueFromProject("AUX03"))
        fieldnames.append(self.h.names()["NODO_I"][0])
        fieldnames.append(self.h.names()["NODO_F"][0])


        #line = ';'.join(x for x in fieldnames) + '\n'
        #unicode_line = line.encode('utf-8')
        #output_file.write(unicode_line)

        lstMinFeatures = []
        lstFeatures = []
        for ft in dicionario:
            try:
                pol = ft.geometry().isEmpty()
            except:
                self.h.ShowError("O trecho " + ft[self.h.readValueFromProject("SEG_NAME_C")] + " esta corrompido. nao possui geometria" )
                break
                
            minFeatureObj = {}
            minFeatureObj["BEG_LINE_COORD_E"] = ft[beg_line_coord_e]
            minFeatureObj["BEG_LINE_COORD_N"] = ft[beg_line_coord_n]
            minFeatureObj["FIN_LINE_COORD_E"] = ft[fin_line_coord_e]
            minFeatureObj["FIN_LINE_COORD_N"] = ft[fin_line_coord_n]
            minFeatureObj["SEG_NAME"] = ft[self.h.readValueFromProject("SEG_NAME")]
            minFeatureObj["SEG_NAME_C"] = ft[self.h.readValueFromProject("SEG_NAME_C")]
            lstMinFeatures.append(minFeatureObj)
            lstFeatures.append(ft)
        
        rows = []
        for f in dicionario:
            #self.dlgExport.progressBar.setValue(self.dlgExport.progressBar.value() + 1)
            values = []
            geom = f.geometry()
            isBegin,isEnd,totalEnd = self.h.Get_Aux_Trm(f.id(),lstFeatures)

            #SEG_NAME_C
            name = f.attributes()[mylayer.fields().lookupField( self.h.readValueFromProject('SEG_NAME_C') )]
            o_name = name
            geom.convertToSingleType()
            vl_id = '{0:.6f}, {1:.6f}'.format(geom.asPolyline()[0].x(), geom.asPolyline()[0].y())
            values.append(str(vl_id))
            values.append(str(str(f[self.h.readValueFromProject("EXT_FIELD_NAME")])))
            values.append(str(str(f[beg_line_coord_e])))
            values.append(str(str(f[beg_line_coord_n])))
            values.append(str(str(f[fin_line_coord_e])))
            values.append(str(str(f[fin_line_coord_n])))
            values.append(str(f[self.h.readValueFromProject("SEG_NAME")]))
            values.append(str(name))
            values.append(str(f[self.h.readValueFromProject("AUX_POS")]))
            values.append(str(f[self.h.readValueFromProject("AUX_PAV_1")]))
            values.append(str(f[self.h.readValueFromProject("AUX_PAV_2")]))
            values.append(str(f[self.h.readValueFromProject("AUX_PROF_I")]))
            values.append(str(f[self.h.readValueFromProject("AUX_PROF_F")]))
            values.append(str(f[self.h.readValueFromProject("AUX01")]))
            values.append(str(f[self.h.readValueFromProject("AUX02")]))
            values.append(str(f[self.h.readValueFromProject("AUX03")]))
            #AUX_TRM_I
            _isBegin = 0
            if isBegin == True:
                _isBegin = 1
            values.append(str(_isBegin))
            #AUX_TRM_F
            _isEnd = 0
            if isEnd == True:
                _isEnd = 1
            values.append(str(_isEnd))
            #TRM_(N-1)_A
            fnd = self.h.Get_Feature_On_Index(lstMinFeatures,f,-1)
            if fnd != None:
                nameOf = fnd["SEG_NAME_C"]
                values.append(str(nameOf))
            else:
                values.append("")
            #TRM_(N-1)_B                
            fnd = self.h.Get_Feature_On_Index(lstMinFeatures,f,-1,False)
            if fnd != None:
                nameOf = fnd["SEG_NAME_C"]
                values.append(str(nameOf))
                toExclud = fnd["SEG_NAME"]
                #TRM_(N-1)_C                
                fnd = self.h.Get_Feature_On_Index(lstMinFeatures,f,-1,False,[toExclud])
                if fnd != None:
                    nameOf = fnd["SEG_NAME_C"]
                    values.append(str(nameOf))
                else:
                    values.append("")
            else:
                values.append("")
                values.append("")
            #TRM_(N+1)
            fnd = self.h.Get_Feature_On_Index(lstMinFeatures,f,1,False,[],True)
            if fnd != None:
                nameOf = fnd["SEG_NAME_C"]
                values.append(str(nameOf))
            else:
                values.append("")               
            if nodeLayer:
                point1 = self.h.GetPointFromCoordinates(nodeLayer.getFeatures(),geom.asPolyline()[0])
                point2 = self.h.GetPointFromCoordinates(nodeLayer.getFeatures(),geom.asPolyline()[-1])
                if point1:
                    _qeList = point1.attributes()[nodeLayer.fields().lookupField( self.h.readValueFromProject('QE') )]
                    #QE
                    values.append(str(_qeList))
                    if _qeList:
                        qei,qef = self.h.GetQEFromBlockLayer(_qeList.split(","))
                        #QEI
                        values.append(str(qei))
                        #QEF
                        values.append(str(qef))
                    else:
                        #QEI
                        values.append("")
                        #QEF
                        values.append("")
                    #COTA_I
                    values.append(str(point1.attributes()[cota_idx]))
                    #NODO_I
                    values.append(str(o_name))
                else:
                    values.append("")
                    values.append("")
                    values.append("")
                    values.append("")
                if point2:                  
                    #COTA_F
                    values.append(str(point2.attributes()[cota_idx]))
                    #NODO_F
                    if totalEnd:
                        nodo_name = name + "-FINAL"
                    else:
                        fnd = self.h.Get_Feature_On_Index(lstMinFeatures,f,+1,True,[],True)
                        if fnd:
                            nodo_name = fnd['SEG_NAME_C'] 
                    values.append(str(nodo_name))
                else:
                    values.append("")
            v2 = []
            v2.append(values[16])
            v2.append(values[17])
            v2.append(values[6])
            v2.append(values[7])
            v2.append(values[1])
            v2.append(values[18])
            v2.append(values[19])
            v2.append(values[20])
            v2.append(values[22])
            v2.append(values[24])
            v2.append(values[23])
            v2.append(values[11])
            v2.append(values[8])
            v2.append(values[12])
            v2.append(values[25])
            v2.append(values[27])
            v2.append(values[21])
            v2.append(values[0])
            v2.append(values[2])
            v2.append(values[3])
            v2.append(values[4])
            v2.append(values[5])
            v2.append(values[9])
            v2.append(values[10])
            v2.append(values[13])
            v2.append(values[14])
            v2.append(values[15])
            v2.append(values[26])
            v2.append(values[28])

            v2.append("")

            rows.append(v2)

        listRows = {}
        toCheck = []
        for row in rows:
            zipRow = zip(fieldnames,row)
            colSeg = row[3]
            initialSeg = row[0]
            finalSeg = row[1]
            previousCol = row [5]
            col1 = row [6]
            col2 = row [7]
            if initialSeg == '0' and finalSeg == '0' and not previousCol and (col1 or col2):
                toCheck.append(colSeg)         
            listRows[colSeg] = dict(zipRow)
        listRows = self.checkingData(toCheck, listRows)
        print("Total time execution to process: --- %s seconds ---" % (time.time() - start_time))
        return listRows

    
    def updateSegmentsLayer(self, colseg, data):
        layer = self.h.GetLayer()
        layer.removeSelection()
        fields = layer.fields()
        col = self.h.readValueFromProject("SEG_NAME_C")
        features = layer.getFeatures(QgsFeatureRequest(QgsExpression("\"{}\" = '{}'".format(col, colseg))))
        layer.startEditing()
        for feature in features:            
            for key in data:
                idx = fields.indexFromName(key)
                if idx != -1:
                    msg = "field {} antes:{} despues:{}".format(key, feature.attributes()[idx], data[key])
                    layer.changeAttributeValue(feature.id(), idx, data[key])
                    print(msg)
        layer.commitChanges()
        return True
    
    
    def checkingData(self, toCheck, list):        
        for colSeg in toCheck:
            col1 = list[colSeg]['TRM_(N-1)_B']
            col2 = list[colSeg]['TRM_(N-1)_C']
            col1LastNumber = col2LastNumber = 0
            if col1:
                col1LastNumber = int(col1.split('-')[1]) if col1.count('-') == 1 else int(col1.split('--')[1])
            if col2:
                col2LastNumber = int(col2.split('-')[1]) if col2.count('-') == 1 else int(col2.split('--')[1])
            d = {col1: col1LastNumber, col2:col2LastNumber}
            parentCol = max(d, key=d.get)
            list[parentCol]['AUX_TRM_F'] = "0"
            prntColSegLen = len(parentCol.split('-')[1]) if parentCol.count('-') == 1 else len(parentCol.split('--')[1])
            prntColSegLastNr = int(parentCol.split('-')[1]) if parentCol.count('-') == 1 else int(parentCol.split('--')[1])
            colSegLen = len(colSeg.split('-')[1]) if colSeg.count('-') == 1 else len(colSeg.split('--')[1])
            colSegLastNr = int(colSeg.split('-')[1]) if colSeg.count('-') == 1 else int(colSeg.split('--')[1])
            colSegCol = list[colSeg]['ID_COL'] 
            final = 0
            i = 0
            while final == 0:
                prntColSegLastNr = prntColSegLastNr + 1
                colSegIndex = colSegCol + '-' + str(colSegLastNr).zfill(colSegLen)
                lpCol = list[parentCol]['ID_COL']
                lpColN = list[parentCol]['ID_COL'] + '-' + str(prntColSegLastNr).zfill(prntColSegLen)
                if i == 0:
                    replaceCol = list[min(d, key=d.get)]['ID_TRM_(N)'] if col2 else ""                    
                    list[colSegIndex].update({
                        'TRM_(N-1)_A': list[parentCol]['ID_TRM_(N)'],
                        'TRM_(N-1)_B': replaceCol,
                        'TRM_(N-1)_C': ""
                    })   
                else:
                    list[colSegIndex].update({
                        'TRM_(N-1)_A': list[list[colSegIndex]['TRM_(N-1)_A']]['ID_TRM_(N)']
                    })
                final = int(list[colSegIndex]['AUX_TRM_F'])

                data = {
                        'ID_COL': lpCol,
                        'ID_TRM_(N)': lpColN,
                        'NODO_I': lpColN
                    }
                list[colSegIndex].update(data)
                self.updateSegmentsLayer(colSegIndex, data)
                colSegLastNr += 1
                i += 1

        for colSeg in list:
            if (list[colSeg]['AUX_TRM_F'] == "0" and list[list[colSeg]['TRM_(N+1)']]['ID_TRM_(N)'] != list[colSeg]['TRM_(N+1)']):
                newColSeg = list[list[colSeg]['TRM_(N+1)']]['ID_TRM_(N)']
                list[colSeg].update({'TRM_(N+1)': newColSeg, 'NODO_F': newColSeg})
            if (list[colSeg]['AUX_TRM_F'] == "1" and list[colSeg]['TRM_(N+1)'] != "" and list[list[colSeg]['TRM_(N+1)']]['ID_TRM_(N)'] != list[colSeg]['TRM_(N+1)']):
                list[colSeg].update({'TRM_(N+1)': list[list[colSeg]['TRM_(N+1)']]['ID_TRM_(N)']})
            if (list[colSeg]['AUX_TRM_F'] == "1"):
                if ('-FINAL' in list[colSeg]['NODO_F']):
                    if (list[list[colSeg]['NODO_F'].replace('-FINAL','')]['ID_TRM_(N)'] != list[colSeg]['NODO_F'].replace('-FINAL','')):
                        list[colSeg].update({'NODO_F': list[list[colSeg]['NODO_F'].replace('-FINAL','')]['ID_TRM_(N)'] + '-FINAL'})
                if ('-FINAL' not in list[colSeg]['NODO_F']):
                    if (list[list[colSeg]['NODO_F']]['ID_TRM_(N)'] != list[colSeg]['NODO_F']):
                        list[colSeg].update({'NODO_F': list[list[colSeg]['NODO_F']]['ID_TRM_(N)']})

            if (list[colSeg]['TRM_(N-1)_B'] != ""):
                if (list[list[colSeg]['TRM_(N-1)_B']]['ID_TRM_(N)'] != list[colSeg]['TRM_(N-1)_B']):
                    list[colSeg].update({'TRM_(N-1)_B': list[list[colSeg]['TRM_(N-1)_B']]['ID_TRM_(N)']})
            
            if (list[colSeg]['TRM_(N-1)_C'] != ""):
                if (list[list[colSeg]['TRM_(N-1)_C']]['ID_TRM_(N)'] != list[colSeg]['TRM_(N-1)_C']):
                    list[colSeg].update({'TRM_(N-1)_C': list[list[colSeg]['TRM_(N-1)_C']]['ID_TRM_(N)']})
                        
        if toCheck:
            layer = self.h.GetLayer()
            features = [f for f in layer.getFeatures()]
            checks = AnalisaPendencias(self.iface, self.h)
            testRepeatedNames = checks.AnalisaNomeRepetido(features)
            if testRepeatedNames is not None:
                layer.removeSelection()
                layer.select(testRepeatedNames)
                self.info.emit("selected patch(es)  have repeated names")
                return False
        
        sort_column = self.h.readValueFromProject("SEG_NAME_C")
        sorted_list =  {k: v for k, v in sorted(list.items(), key=lambda item: item[1][sort_column])} #sort by key
        
        return sorted_list.values()

   