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
# [ File Name ] PeachMain.py@python
# [ File Description ] - 2022.01.11 (Y.M.D) - 22:12
#                            *   *   *   *
#
#   This script contains peach main's pypanel widget class
#
# ---------------------------------------------------------------------
from peach.pQt.qHotel import QtWidgets, QtCore
from peach.pQt import img

im = img.IconManager()
im.stash("peach", "peach_dev")


class PeachMainUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PeachMainUI, self).__init__(parent)

        # widget layout functions:
        self.create_widgets()
        self.create_layouts()
        self.create_style()
        self.create_connections()
        self.populate_menu()

    def create_widgets(self):
        self.lbl_hello_world = QtWidgets.QLabel("Hello World")
        self.bnt_test = QtWidgets.QPushButton("Peach Button")
        self.bnt_test2 = QtWidgets.QPushButton("Peach Button2")

    def create_layouts(self):
        layout_master = QtWidgets.QVBoxLayout()
        layout_master.addWidget(self.lbl_hello_world)
        layout_master.addWidget(self.bnt_test)
        layout_master.addWidget(self.bnt_test2)
        self.setLayout(layout_master)

    def create_style(self):
        self.bnt_test.setIcon(im.get("peach_dev"))
        self.bnt_test.setMinimumHeight(50)
        self.bnt_test2.setIcon(im.get("peach"))
        self.bnt_test2.setIconSize(QtCore.QSize(30, 30))
        self.bnt_test2.setMinimumHeight(50)

    def create_connections(self):
        pass

    def populate_menu(self):
        pass
