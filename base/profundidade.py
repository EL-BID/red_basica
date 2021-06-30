from glob import glob
from os import path
from qgis.core import *
from qgis.gui import *


from qgis.PyQt.QtXml import QDomDocument
# Initialize Qt resources from file resources.py
import locale
# Import the code for the dialog
import os
from qgis.core import *
from qgis.gui import *

class CalculaProfundidade:
    iface = None
    h = None

    def __init__ (self, iface, helper):
        self.iface = iface
        self.h = helper

    def processNetwork(self, camada, nos, recobrimento_minimo, diametro, declividade, profundidade, apenasSelecionados):
        self.calcula_cota_rede(self.iface, camada, nos, recobrimento_minimo, diametro, declividade, profundidade, apenasSelecionados)

    def nos_montante(self, camada ,trecho, apenas_selecionados):
        #print("Nos Montante: {}".format(trecho["ID_TRM_(N)"]))
        if apenas_selecionados:
            vetores = camada.selectedFeatures()
        else:
            vetores = camada.getFeatures()

        dicionario = [f for f in vetores]
        for vet in dicionario:
            if (vet[self.h.readValueFromProject("FIN_LINE_COORD_E")] == trecho[self.h.readValueFromProject("BEG_LINE_COORD_E")]) and (vet[self.h.readValueFromProject("FIN_LINE_COORD_N")] == trecho[self.h.readValueFromProject("BEG_LINE_COORD_N")]):
                yield vet
        
    def no_jusante(self, camada, trecho, apenas_selecionados):
        if apenas_selecionados:
            vetores = camada.selectedFeatures()
        else:
            vetores = camada.getFeatures()
        for vet in vetores:
            if (vet[self.h.readValueFromProject("BEG_LINE_COORD_E")] == trecho[self.h.readValueFromProject("FIN_LINE_COORD_E")]) and (vet[self.h.readValueFromProject("BEG_LINE_COORD_N")] == trecho[self.h.readValueFromProject("FIN_LINE_COORD_N")]):
                return vet
        return None

    def percorre_jusante(self, camada, trecho, apenas_selecionados):
        #print("Percorre Jusante Trecho: {}".format(trecho["ID_TRM_(N)"]))
        trecho2 = self.no_jusante(camada, trecho, apenas_selecionados)
        if trecho2 == None:
            return trecho
        else:
            return self.percorre_jusante(camada, trecho2, apenas_selecionados)

    def trecho_final(self, camada, apenas_selecionados):
        if apenas_selecionados:
            vetores = camada.selectedFeatures()
            trecho = vetores[0]
        else:
            vetores = camada.getFeatures()
            trecho = next(vetores)
        
        trecho2 = self.percorre_jusante(camada, trecho, apenas_selecionados)
        if trecho2 == None:
            return trecho
        else:
            return trecho2

    def getCota(self, nos, trecho, jusante = True):
        #print("getCota: {}".format(trecho["ID_TRM_(N)"]))
        nos_dict = {f.id(): f for f in nos.getFeatures()}
        indice_espacial = QgsSpatialIndex(nos.getFeatures())
        geom = trecho.geometry()
        geom.convertToSingleType()
        if jusante:
            pt = nos_dict[indice_espacial.nearestNeighbor(geom.asPolyline()[-1],1)[0]]
        else:
            pt = nos_dict[indice_espacial.nearestNeighbor(geom.asPolyline()[0],1)[0]]
        return pt["CT_(N)"]

    def calcula_cota(self, camada, nos, trecho, recobrimento_minimo, diametro, declividade, profundidade, apenas_selecionados):
        #print("Calcula Cota Trecho: {}".format(trecho["ID_TRM_(N)"]))
        cotapto = self.getCota(nos, trecho,False)
        cota_min = cotapto - recobrimento_minimo - diametro
        i = 0
        for trecho_montante in self.nos_montante(camada, trecho, apenas_selecionados):
            i = i +1
            cota = self.calcula_cota(camada, nos, trecho_montante, recobrimento_minimo, diametro, declividade, profundidade, apenas_selecionados)
            cota = cota - (trecho_montante[self.h.readValueFromProject("EXT_FIELD_NAME")] * declividade)
            if cota < cota_min:
                cota_min = cota
        #print("Trecho: {}\tCota Fundo Montante: {}".format(trecho["ID_TRM_(N)"], cota_min))
        if (i == 0) and (cota_min > (cotapto-profundidade)):
            self.gravarCota(camada, nos, trecho, cotapto-profundidade, False)
            return (cotapto-profundidade)
        else:
            self.gravarCota(camada, nos, trecho, cota_min, False)
            return cota_min
        

    def calcula_cota_rede(self, iface, camada, nos, recobrimento_minimo, diametro, declividade, profundidade, apenas_selecionados):
        tf = self.trecho_final(camada, apenas_selecionados)
        if tf == None:
            iface.messageBar().pushMessage(self.h.tr("Error"), self.h.tr("End patch not found"), level=Qgis.Critical, duration=3)
        else:
            cota_montante = self.calcula_cota(camada, nos, tf, recobrimento_minimo, diametro, declividade, profundidade, apenas_selecionados)
            cota_jus_min = self.getCota(nos, tf,True) - (recobrimento_minimo+diametro)
            cota_jus = cota_montante - (tf[self.h.readValueFromProject("EXT_FIELD_NAME")]*declividade)
            if (cota_jus_min < cota_jus):
                cota_jus = cota_jus_min
            self.gravarCota(camada, nos, tf, cota_jus, True)
            self.gravarCota(camada, nos, tf, cota_montante, False)
            #print("Trecho Final: {}\tCota Fundo Montante: {}\tCota Fundo Jusante:{}".format(tf["ID_TRM_(N)"], cota_montante, cota_jus))

    def gravarCota(self, camada, nos, trecho, cota_fundo, jusante=True):
        nos_dict = {f.id(): f for f in nos.getFeatures()}
        indice_espacial = QgsSpatialIndex(nos.getFeatures())
        geom = trecho.geometry()
        geom.convertToSingleType()
        if jusante:
            fId = indice_espacial.nearestNeighbor(geom.asPolyline()[-1],1)[0]
            pt = nos_dict[fId]
            #print("pto: {}".format(pt["Id_NODO_(n"]))
        else:
            fId = indice_espacial.nearestNeighbor(geom.asPolyline()[0],1)[0]
            pt = nos_dict[fId]
            #print("pto: {}".format(pt["Id_NODO_(n"]))

        pt["CF_NODO_2"] = cota_fundo
        hnt = pt["CT_(N)"] - cota_fundo
        nos.startEditing()
        nos.beginEditCommand("Trecho Multiplo")
        nos.changeAttributeValue(fId, nos.fields().lookupField("CF_NODO_2"), cota_fundo)
        nos.changeAttributeValue(fId, nos.fields().lookupField("h_NODO_TP2"), hnt)
        nos.endEditCommand()
        



