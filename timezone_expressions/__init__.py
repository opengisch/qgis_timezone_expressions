# -*- coding: utf-8 -*-
"""
/***************************************************************************
                                 A QGIS plugin
 print multiple print composer views
                             -------------------
        begin                : 2021-07-19
        copyright            : (C) 2021 by Matthias Kuhn
        email                : matthias@opengis.ch
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""


def classFactory(iface):
    # load multiPrint class from file multiPrint
    from .timezone_expressions import TimezoneExpressions

    return TimezoneExpressions(iface)


def serverClassFactory(server_iface):
    from .timezone_expressions import TimezoneExpressions

    TimezoneExpressions.registerExpressions()
