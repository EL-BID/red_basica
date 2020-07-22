from qgis.utils import iface
from qgis.core import QgsProject
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlQuery
from ...helper_functions import HelperFunctions
import json
from datetime import datetime


class DataController(QObject):
    def __init__(self):
        super().__init__()
        self.h = HelperFunctions(iface)

    def campo_ordem(self, f):
        return f[self.h.readValueFromProject("SEG_NAME_C")]

    def getJsonData(self):
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
                        
        now = datetime.now()
        current_export = {
            'timestamp' : now.strftime("%d/%m/%Y %H:%M:%S"),
            'headers': fieldnames,
            'data': rows
        }
        
        # with open(os.path.join(data_dir, 'export_tramos_nodos.json'), "w") as write_file:
        #     json.dump(current_export, write_file)
        
        # self.h.ShowMessage("Generated")
        listRows = []
        for row in rows:
            zipRow = zip(fieldnames,row)
            listRows.append(dict(zipRow))

        return listRows