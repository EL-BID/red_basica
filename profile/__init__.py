from . import pyqtgraph as pg

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')


class Profile(pg.PlotWidget):

    def __init__(self, **kargs):
        super(Profile, self).__init__(**kargs)
        x = [0, 1, 2, 3, 4, 6, 7, 8, 9]
        y = [1, 0.5, 0.7, 0.4, 1, 0.8, 1, 0.3, 1 ]
        height = [1, 0.5, 0.7, 0.4, 1, 0.8, 1, 0.3, 1 ]
        bg = pg.BarGraphItem(x=x, y=y, height=height, width=0.5, brush='r')
        self.addItem(bg)
        self.plot(x, y, pen=pg.mkPen( color='r',  width=2) , name = 'xxx')


