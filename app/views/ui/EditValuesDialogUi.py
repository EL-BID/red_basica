# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_values_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_editDialog(object):
    def setupUi(self, editDialog):
        editDialog.setObjectName("editDialog")
        editDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        editDialog.resize(261, 141)
        self.formLayout_2 = QtWidgets.QFormLayout(editDialog)
        self.formLayout_2.setObjectName("formLayout_2")
        self.editValueEdit = QtWidgets.QDoubleSpinBox(editDialog)
        self.editValueEdit.setDecimals(6)
        self.editValueEdit.setMaximum(99999999999.0)
        self.editValueEdit.setObjectName("editValueEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.editValueEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(editDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.buttonBox)
        self.label = QtWidgets.QLabel(editDialog)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)

        self.retranslateUi(editDialog)
        self.buttonBox.accepted.connect(editDialog.accept)
        self.buttonBox.rejected.connect(editDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(editDialog)

    def retranslateUi(self, editDialog):
        _translate = QtCore.QCoreApplication.translate
        editDialog.setWindowTitle(_translate("editDialog", "Edit Values"))
        self.label.setText(_translate("editDialog", "New number to update"))
