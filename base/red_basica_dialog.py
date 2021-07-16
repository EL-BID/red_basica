# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os

from qgis.PyQt import uic, QtWidgets
from .helper_functions import HelperFunctions

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__),'resources', 'red_basica_dialog_base.ui'))


class RedBasicaDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super().__init__(parent)

        self.setupUi(self)

        self.grpNewLayer.setVisible(False)
        self.rbExistingLayer.toggled.connect(self.ToogleVisibleGroup)
        self.rbNewLayer.toggled.connect(self.ToogleVisibleGroup)
        self.buttonBox.accepted.connect(self._accept)
        self.buttonBox.rejected.connect(self.reject)


    def ToogleVisibleGroup(self, _b):
        if self.rbExistingLayer.isChecked():
            self.grpExistingLayer.setVisible(True)
            self.grpNewLayer.setVisible(False)
        if self.rbNewLayer.isChecked():
            self.grpNewLayer.setVisible(True)
            self.grpExistingLayer.setVisible(False)

    def SetIface(self,iface):
        global h
        h = HelperFunctions(iface)

    def _accept(self):
        canAccept = True
        if self.rbNewLayer.isChecked():
            if self.txtLayerName.text() == "":
                canAccept = False
                h.ShowError("The name must be a non empty string")                
            
        if canAccept == True:
            self.accept()
