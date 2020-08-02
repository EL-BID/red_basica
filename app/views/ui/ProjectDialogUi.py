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
        ProjectDialog.resize(581, 382)
        ProjectDialog.setModal(True)
        self.dialogButtonBox = QtWidgets.QDialogButtonBox(ProjectDialog)
        self.dialogButtonBox.setGeometry(QtCore.QRect(210, 330, 341, 32))
        self.dialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.dialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.dialogButtonBox.setObjectName("dialogButtonBox")
        self.newProjectButton = QtWidgets.QPushButton(ProjectDialog)
        self.newProjectButton.setGeometry(QtCore.QRect(30, 330, 121, 31))
        self.newProjectButton.setObjectName("newProjectButton")
        self.selectProjectBox = QtWidgets.QComboBox(ProjectDialog)
        self.selectProjectBox.setGeometry(QtCore.QRect(30, 40, 521, 31))
        self.selectProjectBox.setObjectName("selectProjectBox")
        self.selectProjectLabel = QtWidgets.QLabel(ProjectDialog)
        self.selectProjectLabel.setGeometry(QtCore.QRect(30, 20, 461, 17))
        self.selectProjectLabel.setObjectName("selectProjectLabel")
        self.frame = QtWidgets.QFrame(ProjectDialog)
        self.frame.setGeometry(QtCore.QRect(30, 90, 521, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(270, 80, 60, 17))
        self.cityLabel.setObjectName("cityLabel")
        self.projectNameEdit = QtWidgets.QLineEdit(self.frame)
        self.projectNameEdit.setGeometry(QtCore.QRect(10, 30, 481, 33))
        self.projectNameEdit.setObjectName("projectNameEdit")
        self.microsystemLabel = QtWidgets.QLabel(self.frame)
        self.microsystemLabel.setGeometry(QtCore.QRect(10, 150, 81, 17))
        self.microsystemLabel.setObjectName("microsystemLabel")
        self.dateLabel = QtWidgets.QLabel(self.frame)
        self.dateLabel.setGeometry(QtCore.QRect(360, 150, 60, 17))
        self.dateLabel.setObjectName("dateLabel")
        self.microsystemEdit = QtWidgets.QLineEdit(self.frame)
        self.microsystemEdit.setGeometry(QtCore.QRect(10, 170, 141, 33))
        self.microsystemEdit.setObjectName("microsystemEdit")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(357, 170, 131, 33))
        self.dateEdit.setObjectName("dateEdit")
        self.authorLabel = QtWidgets.QLabel(self.frame)
        self.authorLabel.setGeometry(QtCore.QRect(180, 150, 60, 17))
        self.authorLabel.setObjectName("authorLabel")
        self.projectNameLabel = QtWidgets.QLabel(self.frame)
        self.projectNameLabel.setGeometry(QtCore.QRect(10, 10, 121, 17))
        self.projectNameLabel.setObjectName("projectNameLabel")
        self.countryLabel = QtWidgets.QLabel(self.frame)
        self.countryLabel.setGeometry(QtCore.QRect(10, 80, 60, 17))
        self.countryLabel.setObjectName("countryLabel")
        self.countryBox = QtWidgets.QComboBox(self.frame)
        self.countryBox.setGeometry(QtCore.QRect(10, 100, 231, 33))
        self.countryBox.setObjectName("countryBox")
        self.authorEdit = QtWidgets.QLineEdit(self.frame)
        self.authorEdit.setGeometry(QtCore.QRect(180, 170, 151, 33))
        self.authorEdit.setObjectName("authorEdit")
        self.cityEdit = QtWidgets.QLineEdit(self.frame)
        self.cityEdit.setGeometry(QtCore.QRect(270, 100, 221, 33))
        self.cityEdit.setObjectName("cityEdit")

        self.retranslateUi(ProjectDialog)
        self.dialogButtonBox.accepted.connect(ProjectDialog.accept)
        self.dialogButtonBox.rejected.connect(ProjectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ProjectDialog)

    def retranslateUi(self, ProjectDialog):
        _translate = QtCore.QCoreApplication.translate
        ProjectDialog.setWindowTitle(_translate("ProjectDialog", "SANIBIDapp"))
        self.newProjectButton.setText(_translate("ProjectDialog", "Nuevo Proyecto"))
        self.selectProjectLabel.setText(_translate("ProjectDialog", "Seleccione el proyecto"))
        self.cityLabel.setText(_translate("ProjectDialog", "Ciudad"))
        self.microsystemLabel.setText(_translate("ProjectDialog", "Subcuenca"))
        self.dateLabel.setText(_translate("ProjectDialog", "Fecha"))
        self.authorLabel.setText(_translate("ProjectDialog", "Autor"))
        self.projectNameLabel.setText(_translate("ProjectDialog", "Nombre Proyecto"))
        self.countryLabel.setText(_translate("ProjectDialog", "Pais"))

