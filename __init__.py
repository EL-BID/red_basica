# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AutomaticGeometricAttributes
                                 A QGIS plugin
 This plugin fill automaticaly the geometric attributes of a line
                             -------------------
        begin                : 2016-07-20
        copyright            : (C) 2016 by Infinisoft
        email                : frogerio@infinisoft.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load AutomaticGeometricAttributes class from file AutomaticGeometricAttributes.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .core.red_basica import RedBasica
    return RedBasica(iface)
