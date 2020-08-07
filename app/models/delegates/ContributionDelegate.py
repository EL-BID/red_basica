from PyQt5.QtSql import QSqlRelationalDelegate
from PyQt5.QtWidgets import QStyle
from PyQt5.QtGui import QPalette, QColor, QBrush, QPen
from PyQt5.QtCore import QEvent, QSize, Qt

class ContributionDelegate(QSqlRelationalDelegate):
    """ delegate Contribution Table"""    

    def paint(self, painter, option, index):
        painter.save()

        # set background color
        if option.state & QStyle.State_Selected:
            painter.setBrush(QBrush(Qt.white))
        else:
            painter.setBrush(QBrush(Qt.red))
        painter.drawRect(option.rect)

        # set text color
        if option.state & QStyle.State_Selected:
            painter.setPen(QPen(Qt.red))
        else:
            painter.setPen(QPen(Qt.white))

        val = index.data()
        
        painter.drawText(option.rect, Qt.AlignLeft | Qt.AlignCenter, str(val))           
            
        painter.restore()

    def editorEvent(self, event, model, option, index):
        """ Returns True for readOnly columns """
        return True