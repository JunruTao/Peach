#set( $MyName = "Junru Tao" )
#set( $Company = "Digital Peach Studio" )
#set( $Emails = "<junrtao.uk@gmail.com | junrutao@qq.com>" )
#set( $Website = "digital-peach.company.site" )
#set( $Instagram = "digital.peach.studio" )
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright (c) ${YEAR} ${Company} - ${MyName}
# This code is licensed under MIT license (see LICENSE.txt for details)
#                            *   *   *   *
# [ Info ] - ${Company}
# - Authors: ${MyName}
# - Contact: ${Emails}
# - Website: ${Website}
# - Instagram: @${Instagram}
# ---------------------------------------------------------------------
# [ File Name ] ${FILE_NAME}@python
# [ File Description ] - ${YEAR}.${MONTH}.${DAY} (Y.M.D) - ${TIME}
#                            *   *   *   *
#
#   [Peach-pQt-Dependent]This script contains Qt-UI Class of 
#   < $CLASSNAME > for "..."
#
# ---------------------------------------------------------------------
from peach.pQt.qHotel import QtWidgets, QtCore


class $CLASSNAME(QtWidgets.QWidget):
    def __init__(self, parent=None):
        """[ $CLASSNAME ] UI Class Constructor """
        super($CLASSNAME, self).__init__(parent)
        
        self.create_widgets()
        self.create_layouts()
        self.create_style()
        self.create_connections()
        self.populate_menu()

    def create_widgets(self):
        """[ $CLASSNAME ] UI Define Widgets """
        pass

    def create_layouts(self):
        """[ $CLASSNAME ] UI Construct Layout """
        layout_main = QtWidgets.QVBoxLayout()
        # TODO:Add Widgets to Layout here
        # ..
        self.setLayout(layout_main)

    def create_style(self):
        """[ $CLASSNAME ] UI Configure Styles """
        pass

    def create_connections(self):
        """[ $CLASSNAME ] UI Connections """
        pass

    def populate_menu(self):
        """[ $CLASSNAME ] UI Populate Menus """
        pass