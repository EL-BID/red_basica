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

from qgis.PyQt import QtGui, uic, QtWidgets
from .helper_functions import HelperFunctions
from qgis.core import *

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__),'resources', 'recobrimento_dialog.ui'))


class CalcularProfundidadeDialog(QtWidgets.QDialog, FORM_CLASS):
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

    def SetIface(self,iface):
        global h
        h = HelperFunctions(iface)

    def _accept(self):
        h.ShowMessage("Iniciado o procedimento de cálculo!")
        #h.ShowError("Aceitou Formulário")
