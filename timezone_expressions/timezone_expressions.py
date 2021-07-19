# -*- coding: utf-8 -*-
"""
/***************************************************************************
ReferenceFunctions
                                 A QGIS plugin
 Provide field calculator function for Reference to other layers/features
 based on Nathan Woodrow work:
 http://nathanw.net/2012/11/10/user-defined-expression-functions-for-qgis/
                              -------------------
        begin                : 2014-09-20
        copyright            : (C) 2014 by enrico ferreguti
        email                : enricofer@gmail.com
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

from PyQt5.QtCore import QTimeZone
from qgis.core import QgsExpression, qgsfunction


class TimezoneExpressions:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        QgsExpression.registerFunction(set_timezone)
        QgsExpression.registerFunction(to_timezone)

    def unload(self):
        QgsExpression.unregisterFunction("set_timezone")
        QgsExpression.unregisterFunction("to_timezone")


@qgsfunction(args=2, group="Time", register=False, usesgeometry=False)
def set_timezone(values, feature, parent):
    """
    Sets the timezone of the provided date time value. This does not perform
    any conversion of the value, it just overwrites the timezone part of it.

    <h4>Syntax</h4>
    <p>set_timezone("datetime", 'Europe/Zurich')</p>
    <h4>Arguments</h4>
    <dl>
      <dn>datetime</dn><dd>A datetime value</dd>
      <dn>timezone</dn><dd>Name of the target timezone</dd>
    </dl>

    """

    time = values[0]
    timezone_name = values[1]

    time.setTimeZone(QTimeZone(timezone_name.encode("ascii")))
    return time


@qgsfunction(args=2, group="Time", register=False, usesgeometry=False)
def to_timezone(values, feature, parent):
    """
    Sets the timezone of the provided date time value. This does not perform
    any conversion of the value, it just overwrites the timezone part of it.

    <h4>Syntax</h4>
    <p>set_timezone("datetime", 'Europe/Zurich')</p>
    <h4>Arguments</h4>
    <dl>
      <dn>datetime</dn><dd>A datetime value</dd>
      <dn>timezone</dn><dd>Name of the target timezone</dd>
    </dl>

    """

    time = values[0]
    timezone_name = values[1]

    return time.toTimeZone(QTimeZone(timezone_name.encode("ascii")))
