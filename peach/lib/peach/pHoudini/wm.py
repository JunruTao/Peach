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
# [ File Name ] wm.py@python
# [ File Description ] - 2022.01.15 (Y.M.D) - 05:15
#                            *   *   *   *
#
#   This script contains Window Management functions
#
# ---------------------------------------------------------------------
import hou
from peach import pImp, pDir
pImp.reload(pDir)


def getMainWindow():
    """
    [ Houdini-Qt ] get Main window widget
    @return: QtWidgets.QWidget
    """
    return hou.qt.mainWindow()


def getMainWindowRect():
    """
    [ Houdini-Qt ] get Main window widget Rectangle
    @return: QtCore.QRect
    """
    return getMainWindow().geometry()


def getMainWindowCenter():
    """[ Houdini-Qt ] get Main window widget center point
    @return: QtCore.QPoint
    """
    return getMainWindowRect().center()


def getCurrentEditor():
    """[ Houdini ] get Current working Network
    @return: (hou.Pane)
    """
    return hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)


def save_file(filepath, file_name):
    """
    [ Houdini ] Save Houdini file
    @param filepath: (str) path to folder/or filepath
    @param file_name: (str) filename (no extension)
    """
    file = filepath
    if file_name:
        file = pDir.join(filepath, file_name + ".hip")
    hou.hipFile.save(file)
