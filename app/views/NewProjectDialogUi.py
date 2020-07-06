# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_project_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewProjectDialog(object):
    def setupUi(self, NewProjectDialog):
        NewProjectDialog.setObjectName("NewProjectDialog")
        NewProjectDialog.resize(624, 450)
        self.dialogButtonBox = QtWidgets.QDialogButtonBox(NewProjectDialog)
        self.dialogButtonBox.setGeometry(QtCore.QRect(250, 400, 341, 32))
        self.dialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialogButtonBox.setObjectName("dialogButtonBox")
        self.label = QtWidgets.QLabel(NewProjectDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 17))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.parametersLabel = QtWidgets.QLabel(NewProjectDialog)
        self.parametersLabel.setGeometry(QtCore.QRect(10, 50, 121, 17))
        self.parametersLabel.setObjectName("parametersLabel")
        self.parametersList = QtWidgets.QComboBox(NewProjectDialog)
        self.parametersList.setGeometry(QtCore.QRect(160, 50, 431, 25))
        self.parametersList.setObjectName("parametersList")
        self.projectNameLabel = QtWidgets.QLabel(NewProjectDialog)
        self.projectNameLabel.setGeometry(QtCore.QRect(10, 100, 131, 17))
        self.projectNameLabel.setObjectName("projectNameLabel")
        self.nameEdit = QtWidgets.QLineEdit(NewProjectDialog)
        self.nameEdit.setGeometry(QtCore.QRect(160, 100, 431, 25))
        self.nameEdit.setObjectName("nameEdit")
        self.cityLabel = QtWidgets.QLabel(NewProjectDialog)
        self.cityLabel.setGeometry(QtCore.QRect(10, 150, 131, 17))
        self.cityLabel.setObjectName("cityLabel")
        self.cityEdit = QtWidgets.QLineEdit(NewProjectDialog)
        self.cityEdit.setGeometry(QtCore.QRect(160, 150, 431, 25))
        self.cityEdit.setObjectName("cityEdit")
        self.dateLabel = QtWidgets.QLabel(NewProjectDialog)
        self.dateLabel.setGeometry(QtCore.QRect(10, 300, 131, 17))
        self.dateLabel.setObjectName("dateLabel")
        self.dateEdit = QtWidgets.QDateEdit(NewProjectDialog)
        self.dateEdit.setGeometry(QtCore.QRect(160, 300, 431, 26))
        self.dateEdit.setObjectName("dateEdit")
        self.microsystemLabel = QtWidgets.QLabel(NewProjectDialog)
        self.microsystemLabel.setGeometry(QtCore.QRect(10, 200, 131, 17))
        self.microsystemLabel.setObjectName("microsystemLabel")
        self.microsystemEdit = QtWidgets.QLineEdit(NewProjectDialog)
        self.microsystemEdit.setGeometry(QtCore.QRect(160, 200, 431, 25))
        self.microsystemEdit.setObjectName("microsystemEdit")
        self.authorLabel = QtWidgets.QLabel(NewProjectDialog)
        self.authorLabel.setGeometry(QtCore.QRect(10, 250, 131, 17))
        self.authorLabel.setObjectName("authorLabel")
        self.authorEdit = QtWidgets.QLineEdit(NewProjectDialog)
        self.authorEdit.setGeometry(QtCore.QRect(160, 250, 431, 25))
        self.authorEdit.setObjectName("authorEdit")

        self.retranslateUi(NewProjectDialog)
        self.dialogButtonBox.accepted.connect(NewProjectDialog.accept)
        self.dialogButtonBox.rejected.connect(NewProjectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewProjectDialog)

    def retranslateUi(self, NewProjectDialog):
        _translate = QtCore.QCoreApplication.translate
        NewProjectDialog.setWindowTitle(_translate("NewProjectDialog", "SANIBIDapp"))
        self.label.setText(_translate("NewProjectDialog", "Crear Nuevo Proyecto"))
        self.parametersLabel.setText(_translate("NewProjectDialog", "Parámetros"))
        self.projectNameLabel.setText(_translate("NewProjectDialog", "Nombre Proyecto"))
        self.cityLabel.setText(_translate("NewProjectDialog", "Ciudad"))
        self.dateLabel.setText(_translate("NewProjectDialog", "Fecha"))
        self.microsystemLabel.setText(_translate("NewProjectDialog", "Subcuenca"))
        self.authorLabel.setText(_translate("NewProjectDialog", "Autor"))

