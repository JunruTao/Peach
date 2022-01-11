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
from peach.pQt.qHotel import QtWidgets
from peach.pQt import pq_ico


class PeachMain(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PeachMain, self).__init__(parent)

        # widget layout functions:
        self.create_widgets()
        self.create_layouts()
        self.create_style()
        self.create_connections()
        self.populate_menu()

    def create_widgets(self):
        self.lbl_hello_world = QtWidgets.QLabel("Hello World")
        self.bnt_test = QtWidgets.QPushButton("Peach Button")

    def create_layouts(self):
        layout_master = QtWidgets.QVBoxLayout()
        layout_master.addWidget(self.lbl_hello_world)
        layout_master.addWidget(self.bnt_test)
        self.setLayout(layout_master)

    def create_style(self):
        self.bnt_test.setIcon(pq_ico.getPixmap("peach_dev", "x50"))

    def create_connections(self):
        pass

    def populate_menu(self):
        pass
