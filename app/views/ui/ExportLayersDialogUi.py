# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export_layers_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExportLayersDialog(object):
    def setupUi(self, ExportLayersDialog):
        ExportLayersDialog.setObjectName("ExportLayersDialog")
        ExportLayersDialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(ExportLayersDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.overrideRadioButton = QtWidgets.QRadioButton(ExportLayersDialog)
        self.overrideRadioButton.setGeometry(QtCore.QRect(40, 30, 271, 23))
        self.overrideRadioButton.setObjectName("overrideRadioButton")
        self.createRadioButton = QtWidgets.QRadioButton(ExportLayersDialog)
        self.createRadioButton.setGeometry(QtCore.QRect(40, 70, 251, 23))
        self.createRadioButton.setChecked(True)
        self.createRadioButton.setObjectName("createRadioButton")
        self.nodesEdit = QtWidgets.QLineEdit(ExportLayersDialog)
        self.nodesEdit.setGeometry(QtCore.QRect(140, 130, 211, 25))
        self.nodesEdit.setObjectName("nodesEdit")
        self.segmentsEdit = QtWidgets.QLineEdit(ExportLayersDialog)
        self.segmentsEdit.setGeometry(QtCore.QRect(140, 180, 211, 25))
        self.segmentsEdit.setObjectName("segmentsEdit")
        self.nodesLabel = QtWidgets.QLabel(ExportLayersDialog)
        self.nodesLabel.setGeometry(QtCore.QRect(60, 140, 62, 17))
        self.nodesLabel.setObjectName("nodesLabel")
        self.segmentsLabel = QtWidgets.QLabel(ExportLayersDialog)
        self.segmentsLabel.setGeometry(QtCore.QRect(50, 190, 71, 17))
        self.segmentsLabel.setObjectName("segmentsLabel")

        self.retranslateUi(ExportLayersDialog)
        self.buttonBox.accepted.connect(ExportLayersDialog.accept)
        self.buttonBox.rejected.connect(ExportLayersDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ExportLayersDialog)

    def retranslateUi(self, ExportLayersDialog):
        _translate = QtCore.QCoreApplication.translate
        ExportLayersDialog.setWindowTitle(_translate("ExportLayersDialog", "Dialog"))
        self.overrideRadioButton.setText(_translate("ExportLayersDialog", "Override current layers"))
        self.createRadioButton.setText(_translate("ExportLayersDialog", "Create new layers"))
        self.nodesLabel.setText(_translate("ExportLayersDialog", "NODES"))
        self.segmentsLabel.setText(_translate("ExportLayersDialog", "SEGMENTS"))
