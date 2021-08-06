from . import pyqtgraph as pg
from ..app.models.Calculation import Calculation
import random
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')


class Profile(pg.PlotWidget):

    def __init__(self, **kargs):
        super(Profile, self).__init__(**kargs)
        segments = self.getSegments()
        for n in segments.keys():
            # puntos
            x = [col['x'] for col in segments[n]]
            y = [col['y'] for col in segments[n]]
            self.plot(x, y, pen=pg.mkPen( color=random.choices(range(256), k=3),  width=2) , name = n)

            #cajas
            x = [col['x'] for col in segments[n]]
            y = [(col['y']/2) for col in segments[n]]
            height = [(col['y'] * -1) for col in segments[n] ]
            bg = pg.BarGraphItem(x=x, y=y, height=height, width=2, brush='r')
            self.addItem(bg)


    def getSegments(self):
        data  = Calculation.getActiveProfileData()
        return data
    