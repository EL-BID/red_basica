# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProjectDialog(object):
    def setupUi(self, ProjectDialog):
        ProjectDialog.setObjectName("ProjectDialog")
        ProjectDialog.resize(610, 248)
        ProjectDialog.setModal(True)
        self.dialogButtonBox = QtWidgets.QDialogButtonBox(ProjectDialog)
        self.dialogButtonBox.setGeometry(QtCore.QRect(250, 190, 341, 32))
        self.dialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialogButtonBox.setObjectName("dialogButtonBox")
        self.newProjectButton = QtWidgets.QPushButton(ProjectDialog)
        self.newProjectButton.setGeometry(QtCore.QRect(30, 190, 121, 25))
        self.newProjectButton.setObjectName("newProjectButton")
        self.selectProjectBox = QtWidgets.QComboBox(ProjectDialog)
        self.selectProjectBox.setGeometry(QtCore.QRect(50, 90, 481, 25))
        self.selectProjectBox.setObjectName("selectProjectBox")
        self.label = QtWidgets.QLabel(ProjectDialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 461, 17))
        self.label.setObjectName("label")

        self.retranslateUi(ProjectDialog)
        self.dialogButtonBox.accepted.connect(ProjectDialog.accept)
        self.dialogButtonBox.rejected.connect(ProjectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ProjectDialog)

    def retranslateUi(self, ProjectDialog):
        _translate = QtCore.QCoreApplication.translate
        ProjectDialog.setWindowTitle(_translate("ProjectDialog", "SANIBIDapp"))
        self.newProjectButton.setText(_translate("ProjectDialog", "Nuevo Proyecto"))
        self.label.setText(_translate("ProjectDialog", "Seleccione el proyecto"))

