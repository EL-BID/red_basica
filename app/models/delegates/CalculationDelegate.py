
from PyQt5.QtSql import QSqlRelationalDelegate
from PyQt5.QtWidgets import QStyle, QItemDelegate, QDoubleSpinBox
from PyQt5.QtGui import QPalette, QColor, QBrush, QPen
from PyQt5.QtCore import QEvent, QSize, Qt, QVariant
from ..Criteria import Criteria

class NumberFormatDelegate(QItemDelegate):
    def __init__(self, parent=None):
        QItemDelegate.__init__(self, parent)
        self.colors = {
            'editable': QColor(255,255,204),
            'orange_light': QColor(255,192,144)
        }


    def editorEvent(self, event, model, option, index):
        """ Returns True for readOnly columns """        
        return False

    def paint(self, painter, option, index):
        model = index.model()
        col = index.column()
        row = index.row()
        slopesMinModified = model.record(row).value('slopes_min_modified')
        if slopesMinModified:
            painter.fillRect(option.rect,self.colors['orange_light'])
        else:
            painter.fillRect(option.rect,self.colors['editable'])
        super().paint(painter, option, index)

    def createEditor(self, parent, option, index):
        editor = QDoubleSpinBox(parent)
        editor.setMaximum(10**10)
        editor.setDecimals(4)
        return editor

class CalculationDelegate(QSqlRelationalDelegate):
    """ delegate Calculations Table"""    
    
    def __init__(self, parent=None):
        QSqlRelationalDelegate.__init__(self, parent)
        self.colors = {
            'editable': QColor(255,255,204),
            'orange_light': QColor(255,192,144),
            'orange_dark': QColor(255, 153, 102),
            'pink_light': QColor(242, 220, 219),
            'pink_dark': QColor(230, 185, 184),
            'pipe_end_warning': QColor(255, 153, 204)
        }
        self.editables = [ 'col_pipe_position', 
                           'aux_prof_i', 
                           'force_depth_up' , 
                           'force_depth_down', 
                           'slopes_min_accepted_col', 
                           'adopted_diameter']

    def paint(self, painter, option, index):
        
        model = index.model()
        col = index.column()
        text = index.data()
        row = index.row()
        color = False

        #$RedBasica.$E and $RedBasica.$V
        if not color:
            if col in [model.fieldIndex('col_seg'), model.fieldIndex('depth_up')]:                  
                initialSeg = model.record(row).value('initial_segment')                               
                if initialSeg:
                    color = self.colors['orange_dark']
        
        #$RedBasica.$V and $RedBasica.$W
        if not color:
            if col in [model.fieldIndex('depth_up'), model.fieldIndex('depth_down')]:                
                if text and text != '':
                    if 2 <= text <3:
                        color = self.colors['pink_light']
                    if text >= 3:
                        color = self.colors['pink_dark']

            if col in [model.fieldIndex('adopted_diameter')]:
                adoptedDiameter = model.record(row).value('adopted_diameter')
                suggestedDiameter = model.record(row).value('suggested_diameter')
                if suggestedDiameter != adoptedDiameter:
                    color = self.colors['orange_light']

        #Editable fields
        if  col in [model.fieldIndex(x) for x in self.editables]:
            # $RedBasica.$R and $RedBasica.$X
            if col in [model.fieldIndex('force_depth_up'), model.fieldIndex('force_depth_down')]:                    
                if text:
                    color = self.colors['orange_light']
            if not color:                    
                color = self.colors['editable']

        if col in [model.fieldIndex('water_level_pipe_end')]:
            limit = Criteria().getValueBy('max_water_level')
            if text >= limit:
                color = self.colors['pipe_end_warning']

        if color:
            painter.fillRect(option.rect,color)

        super().paint(painter, option, index)

    def sizeHint(self, option, index):
        """ Returns the size needed to display the item in a QSize object. """
        return QSqlRelationalDelegate.sizeHint(self, option, index) + QSize(1, 1)

    def editorEvent(self, event, model, option, index):
        """ Returns True for readOnly columns """        
        return index.column() not in [model.fieldIndex(x) for x in self.editables]
    