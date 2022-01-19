#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright (c) 2022 Digital Peach Studio - Junru Tao
# This code is licensed under MIT license (see LICENSE.txt for details)
#                            *   *   *   *
# [ Info ] - Digital Peach Studio
# - Authors: Junru Tao
# - Contact: <junrtao.uk@gmail.com | junrutao@qq.com>
# - Website: digital-peach.company.site
# - Instagram: @digital.peach.studio
# ---------------------------------------------------------------------
# [ File Name ] sty.py@python
# [ File Description ] - 2022.01.19 (Y.M.D) - 20:29
#                            *   *   *   *
#
#   This script contains Styling functions for Qt
#
# ---------------------------------------------------------------------
from peach.pQt.qHotel import QtCore
from datetime import datetime
import re

_line = "    {param}: {value};\n"
_header = "{category}#{object} {{\n"
_close = "}\n\n"


def unique_object_str(obj=None):
    """
    [ Style ] Get Unique String for StyleSheet.
    <br> In order to make each widget more unique and customized,
    The unique name is required to customize. In the <code>Sheet
    </code> Class, the format of the sheet will be following:
    <br> <code>[Category]#[ObjectName] { ... }</code> Style.

    @param obj: (str/QObject/None) Anything
    @return: (str) unique name based on time
    """
    if isinstance(obj, str):
        # is a defined string
        return obj
    elif isinstance(obj, QtCore.QObject):
        # is a Qt Object Instance
        if obj.objectName() == "":
            name_str = obj.__class__.__name__
            name_str += datetime.now().strftime('Id%YP%mO%dP%HO%MP%SI')
            return name_str
        else:
            return obj.objectName()
    else:
        # get a generic id
        return datetime.now().strftime('ObjectId%YP%mO%dP%HO%MP%SI')


class C(object):
    """[ Qt Style Category ]"""
    wgt = "QWidget"
    dlg = "QDialog"
    lbl = "QLabel"
    bnt = "QPushButton"
    cbx = "QCheckBox"
    ldt = "QLineEdit"
    msb = "QMessageBox"
    mnu = "QMenu"
    ttp = "QToolTip"
    tbb = "QTabBar"
    # Append the list if needed


class Sheet(object):
    def __init__(self, cat=C.wgt, obj=None):
        """[ Sheet ] constructor"""
        self._object = unique_object_str(obj)
        self._header = _header.format(category=cat, object=self._object)
        self._current_state = ""
        self._states = dict()

    def new(self, state="default"):
        """
        [ Sheet ] setter
        <br> Create a new state to store styles
        @param state: (str) state name, i.g. "warning", "selected"
        """

        if not self._current_state:
            # Empty
            self._current_state = state
        elif state == self._current_state:
            # Is current State
            digit = re.search(r"\d+$", state)
            if digit is not None:
                digit = int(digit.group()) + 1
            else:
                digit = 1
            self._current_state += digit
        else:
            self._current_state = state

    def get(self, state=""):
        """[ Sheet ] getter
        @return (str) Constructed Style Sheet.
        """
        r_str = self._header
        # todo
        r_str += _close
        pass

