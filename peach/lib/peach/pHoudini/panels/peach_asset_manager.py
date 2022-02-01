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
# [ File Name ] peach_asset_manager.py@python
# [ File Description ] - 2022.02.01 (Y.M.D) - 16:36
#                            *   *   *   *
#
#   [Peach-pQt-Dependent]This script contains Qt-UI Class of 
#   < AssetManagerUI > for "..."
#
# ---------------------------------------------------------------------
from peach.pQt.qHotel import QtWidgets, QtCore


class AssetManagerUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        """[ AssetManagerUI ] UI Class Constructor """
        super(AssetManagerUI, self).__init__(parent)

        self.create_widgets()
        self.create_layouts()
        self.create_style()
        self.create_connections()
        self.populate_menu()

    def create_widgets(self):
        """[ AssetManagerUI ] UI Define Widgets """
        pass

    def create_layouts(self):
        """[ AssetManagerUI ] UI Construct Layout """
        layout_main = QtWidgets.QVBoxLayout()
        # TODO:Add Widgets to Layout here
        # ..
        self.setLayout(layout_main)

    def create_style(self):
        """[ AssetManagerUI ] UI Configure Styles """
        pass

    def create_connections(self):
        """[ AssetManagerUI ] UI Connections """
        pass

    def populate_menu(self):
        """[ AssetManagerUI ] UI Populate Menus """
        pass
