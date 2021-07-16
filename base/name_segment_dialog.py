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
from __future__ import print_function
from __future__ import absolute_import

from builtins import str
from builtins import range
import os

from qgis.PyQt import uic, QtWidgets
from .helper_functions import HelperFunctions

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'resources', 'name_segment_dialog_base.ui'))


class NameSegmentDialog(QtWidgets.QDialog, FORM_CLASS):
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

        self.nVertices = 0

    def SetIface(self,iface):
        global h
        h = HelperFunctions(iface)

    def SetNVertices(self,_nVertices):
        self.nVertices = _nVertices

    def _accept(self):
        
        if self.txtSegmentName.text() != "":
            fut_names = []
            init = int(self.txtInitialCount.text())

            nVertices = self.nVertices + init - 1
            
            for i in range(init,nVertices):
                fut_names.append(self.txtSegmentName.text() + "-" + str(i).zfill(3))

            # fix_print_with_import
            print("futuros",fut_names)
            
            seg_name_c = h.readValueFromProject("SEG_NAME_C")

            found = False
            w_fnd = ""

            # fix_print_with_import
            print("nao pode ser:",fut_names)
            trechos = [f for f in h.GetLayer().getFeatures()]
            for n in fut_names:
                for f in trechos:
                    name = f[seg_name_c]
                    if name == n:
                        found = True
                        w_fnd = name
                        break

                if found == True:
                    break
            print("nao pode ser:")
            if found:
                reply = QtWidgets.QMessageBox.question(h.iface.mainWindow(), 'Continuar?', 
                 'Existe trecho com o mesmo nome: '+ w_fnd + '. Deseja Continuar?', QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
                if reply == QtWidgets.QMessageBox.Yes:
                    self.accept()
                else:
                    h.ShowError("Theres already features with the name " + w_fnd)
                    self.reject()
            else:
                self.accept()
        else:
            h.ShowError("The name must be a non empty string")
            self.reject()
