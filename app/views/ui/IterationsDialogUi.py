# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iterations.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_iterations(object):
    def setupUi(self, iterations):
        iterations.setObjectName("iterations")
        iterations.setWindowModality(QtCore.Qt.ApplicationModal)
        iterations.resize(261, 141)
        self.formLayout_2 = QtWidgets.QFormLayout(iterations)
        self.formLayout_2.setObjectName("formLayout_2")
        self.iterationsEdit = QtWidgets.QSpinBox(iterations)
        self.iterationsEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.iterationsEdit.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.iterationsEdit.setMinimum(1)
        self.iterationsEdit.setProperty("value", 12)
        self.iterationsEdit.setObjectName("iterationsEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.iterationsEdit)
        self.label = QtWidgets.QLabel(iterations)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(iterations)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)

        self.retranslateUi(iterations)
        self.buttonBox.accepted.connect(iterations.accept)
        self.buttonBox.rejected.connect(iterations.reject)
        QtCore.QMetaObject.connectSlotsByName(iterations)

    def retranslateUi(self, iterations):
        _translate = QtCore.QCoreApplication.translate
        iterations.setWindowTitle(_translate("iterations", "Iterations"))
        self.label.setText(_translate("iterations", "Max. number of iterations"))
