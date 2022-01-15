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
from peach.pQt.qHotel import QtWidgets


class RenamerUI(QtWidgets.QDialog):
    def __init__(self, parent=None):
        """[ RenamerUI ] UI Class Constructor """
        super(RenamerUI, self).__init__(parent)

        self.create_widgets()
        self.create_layouts()
        self.create_style()
        self.create_connections()
        self.populate_menu()

    def create_widgets(self):
        """[ RenamerUI ] UI Define Widgets """
        self.lbl_test = QtWidgets.QLabel("hello world")
        pass

    def create_layouts(self):
        """[ RenamerUI ] UI Construct Layout """
        layout_main = QtWidgets.QVBoxLayout()
        layout_main.addWidget(self.lbl_test)
        self.setLayout(layout_main)

    def create_style(self):
        """[ RenamerUI ] UI Configure Styles """
        pass

    def create_connections(self):
        """[ RenamerUI ] UI Connections """
        pass

    def populate_menu(self):
        """[ RenamerUI ] UI Populate Menus """
        pass
