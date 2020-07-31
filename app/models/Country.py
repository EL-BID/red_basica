from PyQt5.QtCore import pyqtSignal, QModelIndex, QLocale
from PyQt5.QtSql import QSqlTableModel, QSqlQuery
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import Qt

class Country(QSqlTableModel):
    
    def __init__(self, *args, **kwargs):        
        super(Country, self).__init__(*args, **kwargs)
        self.setTable("countries")
        self.locale = QLocale().name()
        self.language = self.locale[0:2] if self.locale[0:2] in ('en','es','pt') else 'en' 
        self.nameFieldIndex = self.fieldIndex('name_{}'.format(self.language))
        self.index = self.fieldIndex('id')
        self.setSort(self.nameFieldIndex, Qt.AscendingOrder)        
        self.select()

    def getList(self):
        countryModel = QSqlTableModel(self)
        countryModel.setTable("countries")
        countryModel.select()
        countries_list = []
        for i in range(countryModel.rowCount()):
            _id = countryModel.record(i).value("id")
            name = countryModel.record(i).value("name_" + self.language)
            countries_list.append((_id, name))
        return countries_list

    def getDisplayColumn(self):
        return self.nameFieldIndex