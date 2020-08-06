from PyQt5.QtSql import QSqlRelationalDelegate


class WaterLevelAdjDelegate(QSqlRelationalDelegate):
    """ delegate WaterLevelAdj Table"""    

    def editorEvent(self, event, model, option, index):
        """ Returns True for readOnly columns """
        return True