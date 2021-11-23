from qgis.PyQt.QtCore import *
from qgis.core import QgsVectorLayer, QgsFeature, QgsGeometry, QgsProject, QgsPoint, QgsPointXY, QgsField
import math

class vLayer(object):
    '''creation of a virtual layer'''
    def __init__(self, nom, type):
        self.type=type
        self.name = nom
        self.layer = QgsVectorLayer(self.type, self.name , "memory")
        crs = QgsProject.instance().crs()
        self.layer.setCrs(crs, True)
        self.pr =self.layer.dataProvider()
        self.seg = None
        self.pr.addAttributes([QgsField("col_seg",  QVariant.String)])
        self.pr.addAttributes([QgsField("x_axis",  QVariant.String)])
        self.pr.addAttributes([QgsField("y_axis",  QVariant.String)])
        self.pr.addAttributes([QgsField("x",  QVariant.String)])
        self.pr.addAttributes([QgsField("y",  QVariant.String)])
        self.pr.addAttributes([QgsField("h",  QVariant.String)])
        self.layer.updateFields()

    def createPoint(self, geometry, attributes):
         # add point to the layer
        self.seg = QgsFeature()
        self.seg.setGeometry(QgsGeometry.fromPointXY(geometry))
        self.seg.setAttributes([attributes[i] for i in attributes.keys()])
        self.pr.addFeatures([self.seg])
        self.layer.addFeatures([self.seg])
        self.layer.updateExtents()

    def pairs(self, list):
        # list pairs iteration
        for i in range(1, len(list)):
            yield list[i-1], list[i]

    def mag(self, point):
        # magnitude of a vector
        return math.sqrt(point.x()**2 + point.y()**2)

    def diff(self, point2, point1):
        # substraction betwen two vector
        return QgsPoint(point2.x()-point1.x(), point2.y() - point1.y())

    def length(self,point1,point2):
        # length of the segment
        point1 = QgsPointXY(point1.x(), point1.y())
        point2 = QgsPointXY(point2.x(), point2.y())
        return math.sqrt(point1.sqrDist(point2))

    def dirCos(self, point):
        # direction cosines of the segment
        cosa = point.x() / self.mag(point)
        cosb = point.y() / self.mag(point)
        return cosa,cosb

    def clear(self):
        self.pr.truncate()       

    def getFeatures(self):
        return self.layer.getFeatures()
    
    def setVisibility(self, visible):
        node = QgsProject.instance().layerTreeRoot().findLayer(self.layer)
        if node:
            node.setItemVisibilityChecked(visible)
        else:
            QgsProject.instance().addMapLayers([self.layer])