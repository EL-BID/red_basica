# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginQDialog(object):
    def setupUi(self, loginQDialog):
        loginQDialog.setObjectName("loginQDialog")
        loginQDialog.resize(377, 116)
        self.formLayout = QtWidgets.QFormLayout(loginQDialog)
        self.formLayout.setObjectName("formLayout")
        self.userText = QtWidgets.QLineEdit(loginQDialog)
        self.userText.setObjectName("userText")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.userText)
        self.passLabel = QtWidgets.QLabel(loginQDialog)
        self.passLabel.setObjectName("passLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passLabel)
        self.passText = QtWidgets.QLineEdit(loginQDialog)
        self.passText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passText.setObjectName("passText")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passText)
        self.buttonBox = QtWidgets.QDialogButtonBox(loginQDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)
        self.userLabel = QtWidgets.QLabel(loginQDialog)
        self.userLabel.setObjectName("userLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.userLabel)

        self.retranslateUi(loginQDialog)
        self.buttonBox.accepted.connect(loginQDialog.accept)
        self.buttonBox.rejected.connect(loginQDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(loginQDialog)

    def retranslateUi(self, loginQDialog):
        _translate = QtCore.QCoreApplication.translate
        loginQDialog.setWindowTitle(_translate("loginQDialog", "Login"))
        self.passLabel.setText(_translate("loginQDialog", "Password"))
        self.userLabel.setText(_translate("loginQDialog", "User"))
