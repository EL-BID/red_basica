from PyQt5.QtWidgets import QLineEdit, QItemDelegate
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp


class PipesDecimalsDelegate(QItemDelegate):
    def __init__(self, parent=None):
        QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        """This delagate is custom made for manning_suggested,manning_adopted fields in order to avoid comma issues"""
        editor = QLineEdit(parent)
        regex = QRegExp("[0-9]+(\.[0-9][0-9][0-9]?)?")
        input_validator = QRegExpValidator(regex, editor)
        editor.setValidator(input_validator)
        return editor
