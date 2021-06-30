# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AutomaticGeometricAttributesDialog
                                 A QGIS plugin
 This plugin fill automaticaly the geometric attributes of a line
                             -------------------
        begin                : 2016-07-20
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Infinisoft
        email                : frogerio@infinisoft.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from __future__ import absolute_import

import os

from qgis.PyQt import uic, QtWidgets
from .helper_functions import HelperFunctions
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import *

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__),'resources', 'create_pointLayer_importRaster_dialog.ui'))


class CreatePointLayerImportRaster(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super().__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        self.buttonBox.accepted.connect(self._accept)
        self.buttonBox.rejected.connect(self.reject)
        self.progressBar.hide()

    def SetIface(self,iface):
        global h
        h = HelperFunctions(iface)

    def _accept(self):
        
        if self.txtNodeLayertName.text() != "":
            h.GetLayer().selectByIds([])
            nodeLayerName = self.txtNodeLayertName.text()
            rasterLayerName = self.cboRasterLayer.currentText()

            mult = 1
            if rasterLayerName != h.tr("None"):
                mult = 2

            self.buttonBox.hide()
            self.progressBar.setMinimum(0)
            self.progressBar.setMaximum(h.GetLayer().featureCount() * mult)
            self.progressBar.setValue(0)
            self.progressBar.show()
            QCoreApplication.processEvents()
            
            destL = h.CreateNodeLayerFromVectorLayer(h.GetLayer(),nodeLayerName,self.progressBar)
            if rasterLayerName != h.tr("None"):
                rasterL = QgsProject.instance().mapLayersByName( rasterLayerName )[0]
                interpol = 1
                h.GetRasterValueToVector(rasterL,1,interpol,destL,h.readValueFromProject("COTA"),self.progressBar)        
            
            self.buttonBox.show()
            self.progressBar.setValue(0)
            self.progressBar.hide()
            self.accept()
        else:
            h.ShowError("The name must be a non empty string")
