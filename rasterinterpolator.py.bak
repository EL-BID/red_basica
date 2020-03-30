from qgis.core import QgsRaster, QgsRectangle

try:
    from scipy import interpolate
    from numpy import asscalar
    ScipyAvailable = True
except ImportError:
    ScipyAvailable = False


def isin(value, array2d):
    return bool([x for x in array2d if value in x])


class RasterInterpolator():
    def __init__(self, rasterLayer, interpolMethod, band):
        self.dataProv = rasterLayer.dataProvider()
        self.interpolMethod = interpolMethod
        self.band = band
        if self.dataProv.srcNoDataValue(band):
            self.noDataValue = self.dataProv.srcNoDataValue(band)
        else:
            self.noDataValue = None
        self.myExtent = self.dataProv.extent()
        self.theWidth = self.dataProv.xSize()
        self.theHeight = self.dataProv.ySize()
        
        if interpolMethod == 0:
            self.interpolate = lambda(thePoint): self.nearestNeighbor(thePoint)
        elif interpolMethod == 1:
            self.interpolate = lambda(thePoint): self.linear(thePoint)
        elif interpolMethod == 2:
            self.interpolate = lambda(thePoint): self.bicubic(thePoint)

    def nearestNeighbor(self, thePoint):
        ident = self.dataProv.identify(thePoint, QgsRaster.IdentifyFormatValue)
        value = None
        if ident is not None:  # and ident.has_key(choosenBand+1):
            try:
                value = float(ident.results()[self.band])
            except TypeError:
                value = None
        if value == self.noDataValue:
            return None
        return value

    def linear(self, thePoint):
        # see the implementation of raster data provider, identify method
        # https://github.com/qgis/Quantum-GIS/blob/master/src/core/raster/qgsrasterdataprovider.cpp#L268
        x = thePoint.x()
        y = thePoint.y()
        xres = self.myExtent.width() / self.theWidth
        yres = self.myExtent.height() / self.theHeight
        col = round((x - self.myExtent.xMinimum()) / xres)
        row = round((self.myExtent.yMaximum() - y) / yres)
        xMin = self.myExtent.xMinimum() + (col-1) * xres
        xMax = xMin + 2*xres
        yMax = self.myExtent.yMaximum() - (row-1) * yres
        yMin = yMax - 2*yres
        pixelExtent = QgsRectangle(xMin, yMin, xMax, yMax)
        myBlock = self.dataProv.block(self.band, pixelExtent, 2, 2)
        # http://en.wikipedia.org/wiki/Bilinear_interpolation#Algorithm
        v12 = myBlock.value(0, 0)
        v22 = myBlock.value(0, 1)
        v11 = myBlock.value(1, 0)
        v21 = myBlock.value(1, 1)
        if self.noDataValue in (v12, v22, v11, v21):
            return None
        x1 = xMin+xres/2
        x2 = xMax-xres/2
        y1 = yMin+yres/2
        y2 = yMax-yres/2
        value = (v11*(x2 - x)*(y2 - y)
               + v21*(x - x1)*(y2 - y)
               + v12*(x2 - x)*(y - y1)
               + v22*(x - x1)*(y - y1)
               )/((x2 - x1)*(y2 - y1))
        if value is not None and value == self.noDataValue:
            return None
        return value

    def bicubic(self, thePoint):
        # see the implementation of raster data provider, identify method
        # https://github.com/qgis/Quantum-GIS/blob/master/src/core/raster/qgsrasterdataprovider.cpp#L268
        x = thePoint.x()
        y = thePoint.y()
        xres = self.myExtent.width() / self.theWidth
        yres = self.myExtent.height() / self.theHeight
        col = round((x - self.myExtent.xMinimum()) / xres)
        row = round((self.myExtent.yMaximum() - y) / yres)
        xMin = self.myExtent.xMinimum() + (col-2) * xres
        xMax = xMin + 4*xres
        yMax = self.myExtent.yMaximum() - (row-2) * yres
        yMin = yMax - 4*yres
        pixelExtent = QgsRectangle(xMin, yMin, xMax, yMax)
        myBlock = self.dataProv.block(self.band, pixelExtent, 4, 4)
        # http://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp2d.html
        vx = [xMin+.5*xres, xMin+1.5*xres, xMin+2.5*xres, xMin+3.5*xres]
        vy = [yMin+.5*yres, yMin+1.5*yres, yMin+2.5*yres, yMin+3.5*yres]
        vz = [[myBlock.value(3, 0), myBlock.value(3, 1), myBlock.value(3, 2), myBlock.value(3, 3)],
              [myBlock.value(2, 0), myBlock.value(2, 1), myBlock.value(2, 2), myBlock.value(2, 3)],
              [myBlock.value(1, 0), myBlock.value(1, 1), myBlock.value(1, 2), myBlock.value(1, 3)],
              [myBlock.value(0, 0), myBlock.value(0, 1), myBlock.value(0, 2), myBlock.value(0, 3)]]
        if myBlock.hasNoDataValue()and isin(self.noDataValue, vz):
            return None
        fz = interpolate.interp2d(vx, vy, vz, kind='cubic')
        value = asscalar(fz(x, y)[0])
        if value is not None and value == self.noDataValue:
            return None
        return value
