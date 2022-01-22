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
# TODO: Doc String
#
# ---------------------------------------------------------------------
from peach.pQt.qHotel import QtCore, QtGui
from peach import pImp, pUtil, pLog, pDir
from datetime import datetime
import re
pImp.reload(pUtil, pUtil, pLog, pDir)

_line = "    {param}: {value};\n"
_header = "{category}#{object} {{\n"
_headSn = "{category} {{\n"
_close = "}\n\n"
_counter = 0

# [ Qt Style Category ]
WIDGET = "QWidget"
DIALOG = "QDialog"
LABEL = "QLabel"
BUTTON = "QPushButton"
CHECKBOX = "QCheckBox"
LINE_EDIT = "QLineEdit"
MSGBOX = "QMessageBox"
MENU = "QMenu"
TOOLTIP = "QToolTip"
TAB_BAR = "QTabBar"

# [ Fonts ]
fnt_Arial = "Arial"
fnt_Helvetica = "Helvetica"
fnt_TimesNewRoman = "Times New Roman"
fnt_STHupo = "STHupo"


# [ Log-in Fonts ]
def load_all_custom_fonts():
    """[ Style-Font ] load all the fonts under peach/font folder
    """
    _fonts_path = pDir.listfiles(pDir.getPeachFontsDir())
    for _f in _fonts_path:
        if str(_f).endswith("TTF") or str(_f).endswith("ttf"):
            pLog.debug("Loading from ./fonts: {}".format(pDir.fileNameBare(_f)), cls="LoadFont")
            QtGui.QFontDatabase.addApplicationFont(_f)


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
            name_str += datetime.now().strftime('I%mO%dP%HO%MP%SI')
            # /. add in counter
            global _counter
            name_str += str(_counter)
            _counter += 1
            # ! [ setting object name here]
            obj.setObjectName(name_str)
            return name_str
        else:
            return obj.objectName()
    else:
        # /.get nothing
        return ""


class Sheet(object):
    def __init__(self, obj=None, cat=None, state="default"):
        """
        [ Sheet ] constructor
        @param obj: (str/QCore.QObject) any
        @param cat: (str/None) None Auto detect. str; i.g. "QWidget" or use sty.C.wgt
        """
        self._object = obj
        self._object_id = ""
        self._cat = cat
        self._header = ""
        self._current_state = ""
        self._states = dict()

        # /.create the header
        self._config_header()
        self.newState(state)

    def _config_header(self):
        """[ Internal ]"""
        if self._cat is None:
            if isinstance(self._object, QtCore.QObject):
                self._cat = self._object.__class__.__name__
            else:
                # _____THROWING_ERROR_____
                pLog.error("If Category of object is not specified, you must pass a QObject.",
                           cls=self, fn="Constructor", e=RuntimeError)
        if self._object:
            self._object_id = unique_object_str(self._object)
            self._header = _header.format(category=self._cat, object=self._object_id)
        else:
            self._header = _headSn.format(category=self._cat)

    def _config_unique_state_name(self, state="default"):
        """[ Internal ]"""
        if state in self._states.keys():
            # /.Found in states
            digit = re.search(r"\d+$", state)
            if digit is not None:
                while state in self._states.keys():
                    state = state.replace(str(digit), "")
                    digit = int(digit.group()) + 1
                    state += str(digit)
            else:
                self._current_state += "1"
        else:
            # /.New Name, don't have states.
            self._current_state = state

    def _the_state_dict(self):
        """[ Internal ]"""
        return self._states[self._current_state]

    def newState(self, state="default"):
        """
        [ Sheet ] setter (set current_state)
        <br> Create a new state to store styles. This function should
        be called first before adding any style.
        @param state: (str) state name, i.g. "warning", "selected"
        @return (str) state name
        """
        self._config_unique_state_name(state)
        # /.create empty state value (dict)
        state_values = dict()
        self._states[self._current_state] = state_values
        # /.return the name
        return self._current_state

    def newStateCopy(self, state="default"):
        """
        [ Sheet ] setter (set current_state)
        <br> Create a new state to store styles, this function will
        copy all the style values in previous(current) state, then
        set the current state the new one.
        @param state: (str) state name, i.g. "warning", "selected"
        @return: (str) state name
        """
        # /.make copy first
        state_values = self._states[self._current_state].copy()
        self._config_unique_state_name(state)
        # /.return the name
        self._states[self._current_state] = state_values
        return self._current_state

    def get(self, state=""):
        """[ Sheet ] getter
        @param state: (str) Specific State to get.
        @return (str) Constructed Style Sheet.
        """
        # /.setting current state to the specified state
        if state and state in self._states.keys():
            self._current_state = state
        # /.else just using the current state.

        if len(self._the_state_dict()):
            r_str = self._header
            for key, value in self._the_state_dict().items():
                r_str += _line.format(param=key, value=value)
            r_str += _close
            return r_str
        else:
            return ""

    def getStates(self):
        """[ Sheet ] getter
        @return: (list of str) states
        """
        return list(self._states.keys())

    def getObjectName(self):
        """
        [ Sheet ] getter
        @return: (str) object name
        """
        return self._object_id

    def setObject(self, obj=None, cat=None):
        """[ Sheet ] setter: update sheet object
        @param obj: (str/QCore.QObject) any
        @param cat: (str/None) None Auto detect. str; i.g. "QWidget" or use sty.C.wgt
        """
        self._object = obj
        self._cat = cat
        self._config_header()

    def setTextColor(self, *args):
        """[ Sheet ] setter. config text color
        @param args: (int/float) f/sRGB
        """
        self._the_state_dict()["color"] = "rgb({0}, {1}, {2})".format(*pUtil.sRGB(*args))

    def setBackgroundColor(self, *args):
        """[ Sheet ] setter. config background color
        @param args: (int/float) f/sRGB
        """
        self._the_state_dict()["background-color"] = "rgb({0}, {1}, {2})".format(*pUtil.sRGB(*args))

    def setBorderColor(self, *args):
        """[ Sheet ] setter. config border color
        @param args: (int/float) f/sRGB
        """
        self._the_state_dict()["border-color"] = "rgb({0}, {1}, {2})".format(*pUtil.sRGB(*args))

    def setBorderStyle(self, style="solid"):
        """[ Sheet ] setter. border style border-style
        @param style: (str) i.g. style
        """
        self._the_state_dict()["border-style"] = style

    def setBorderWidth(self, width=0, unit="px"):
        """[ Sheet ] setter. set border width(thickness)
        @param width: (int)
        @param unit: (str) unit, i.g. "px", "pt", "em"...
        """
        self._the_state_dict()["border-width"] = "{0}{1}".format(width, unit)

    def setBorderRadius(self, radius=0, unit="px"):
        """[ Sheet ] setter. set border radius(roundness)
        @param radius: (int)
        @param unit: (str) unit, i.g. "px", "pt", "em"...
        """
        self._the_state_dict()["border-radius"] = "{0}{1}".format(radius, unit)

    def setFont(self, font="", size=-1, unit="px", i=False, b=False, large=False):
        """[ Sheet ] setter. set font /style and size
        @param font: (str) font name, "" using application default
        @param size: (int) font size,`-1` doesn't change
        @param unit: (str)  i.g. "px", "pt", "em"...
        @param i: (bool) italic
        @param b: (bool) bold
        @param large: (bool) large
        """
        self._the_state_dict()["font"] = ""
        if i:
            self._the_state_dict()["font"] += " italic"
        if b:
            self._the_state_dict()["font"] += " bold"
        if large:
            self._the_state_dict()["font"] += " large"
        if size > 0:
            self._the_state_dict()["font"] += " {0}{1}".format(size, unit)
        if font:
            self._the_state_dict()["font"] += " \"{0}\"".format(font)

    def setFontSize(self, size=-1):
        """[ Sheet ] setter. only set font size
        @param size: (int) size
        """
        self.setFont(size=size)

    def assign(self, *args):
        """[ Sheet ] modifier. Assign this style to one/multiple objects
        @param args: (QObjects) object to assign style sheet
        """
        for item in args:
            if self._object:
                self.setObject(obj=item)
            item.setStyleSheet(self.get())
