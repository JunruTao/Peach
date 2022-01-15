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
# [ File Name ] renamer.py@python
# [ File Description ] - 2022.01.15 (Y.M.D) - 04:17
#                            *   *   *   *
#
#   [Peach-pQt-Dependent]This script contains Qt-UI Class of 
#   < RenamerUI > for Dev Tool UI Creation
#
# ---------------------------------------------------------------------
from peach import pImp
from peach.pQt.qHotel import QtWidgets, QtCore
from peach.pHoudini import node, wm
pImp.reload(node, wm)

RenamerUI_instance = None


class RenamerUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        """[ RenamerUI ] UI Class Constructor """
        QtWidgets.QWidget.__init__(self, parent, QtCore.Qt.WindowStaysOnTopHint)
        p = wm.getMainWindowCenter()
        self.setGeometry(p.x(), p.y(), 250, 110)
        self.setWindowTitle('Font Demo')

        self.create_widgets()
        self.create_layouts()
        self.create_style()
        self.create_connections()
        self.populate_menu()

    def create_widgets(self):
        """[ RenamerUI ] UI Define Widgets """
        self.lbl_test = QtWidgets.QLabel("hello world")
        self.button = QtWidgets.QPushButton('Change Font', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20, 20)
        pass

    def create_layouts(self):
        """[ RenamerUI ] UI Construct Layout """
        layout_main = QtWidgets.QVBoxLayout()
        layout_main.addWidget(self.lbl_test)
        layout_main.addWidget(self.button)
        self.setLayout(layout_main)

    def create_style(self):
        """[ RenamerUI ] UI Configure Styles """
        pass

    def create_connections(self):
        self.button.clicked.connect(self._rename_sel)
        """[ RenamerUI ] UI Connections """
        pass

    def populate_menu(self):
        """[ RenamerUI ] UI Populate Menus """
        pass

    def _rename_sel(self):
        selNode = node.listSelected()
        if selNode:
            node.rename(selNode[0], "something")


def show():
    global RenamerUI_instance
    if RenamerUI_instance:
        RenamerUI_instance.close()
    RenamerUI_instance = RenamerUI()
    RenamerUI_instance.show()
