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
import hou
from peach import pImp, pGlob
from peach.pQt.qHotel import QtWidgets, QtCore, QtGui
from peach.pQt import img
from peach.pHoudini import hNode, wm
pImp.reload(hNode, wm, pGlob, img)


style_label = """
QLabel{ 
    background-color: rgb(22, 59, 85);
    color: rgb(239, 243, 246);
    border-color: rgb(18,55,80);
    border-radius: 10;
    border-width: 2;
    border-style: solid;
}
"""

colors = {
    "__IN__": (1.0, 1.0, 1.0),
    "REF_": (0.560, 0.780, 0.745),
    "OUT_": (1, 0.572, 0.019),
    "CTR_": (0.945, 0.164, 0.152),
    "DRV_": (0.031, 0.478, 0.749),
    "PRC_": (0.478, 0.478, 0.478)
}


class RenamerUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        """[ RenamerUI ] UI Class Constructor """
        QtWidgets.QWidget.__init__(self, parent, QtCore.Qt.WindowStaysOnTopHint)
        # [ CONTAINERS ]
        self.selected = []

        # /.Set UI init Position
        p = wm.getMainWindowCenter()
        self.setGeometry(p.x(), p.y(), 500, 260)
        # /.Set Window Title
        self.setWindowTitle('Renamer - PeachPy v%s' % pGlob.PEACH_PY_VERSION)
        icon = QtGui.QIcon(img.getPixmap("peach_dev"))
        self.setWindowIcon(icon)
        # /. Build UI Functions
        self.create_widgets()
        self.create_layouts()
        self.create_style()
        self.create_connections()
        self.populate_menu()

        # /. Register Callback
        hou.ui.addSelectionCallback(self.selectionCallback)

    def create_widgets(self):
        """[ RenamerUI ] UI Define Widgets """
        self.lbl_node_name = QtWidgets.QLabel("No Node Selected")

        self.txt_in = QtWidgets.QLineEdit("subject")
        self.bnt_IN = QtWidgets.QPushButton("__IN__")
        self.bnt_REF = QtWidgets.QPushButton("REF_")
        self.bnt_OUT = QtWidgets.QPushButton("OUT_")
        self.bnt_CTR = QtWidgets.QPushButton("CTR_")
        self.bnt_DRV = QtWidgets.QPushButton("DRV_")
        self.bnt_PRC = QtWidgets.QPushButton("PRC_")

    def create_layouts(self):
        """[ RenamerUI ] UI Construct Layout """
        layout_main = QtWidgets.QVBoxLayout()
        layout_main.addWidget(self.lbl_node_name)
        layout_main.addWidget(self.txt_in)
        wgt_layout_buttons = QtWidgets.QWidget()
        layout_buttons = QtWidgets.QGridLayout()
        layout_buttons.addWidget(self.bnt_IN, 0, 0)
        layout_buttons.addWidget(self.bnt_REF, 1, 0)
        layout_buttons.addWidget(self.bnt_OUT, 2, 0)
        layout_buttons.addWidget(self.bnt_CTR, 0, 1)
        layout_buttons.addWidget(self.bnt_DRV, 1, 1)
        layout_buttons.addWidget(self.bnt_PRC, 2, 1)
        wgt_layout_buttons.setLayout(layout_buttons)
        layout_main.addWidget(wgt_layout_buttons)
        layout_main.addStretch()
        self.setLayout(layout_main)

    def create_style(self):
        """[ RenamerUI ] UI Configure Styles """
        self.lbl_node_name.setStyleSheet(style_label)
        self.setStyleSheet("QWidget{background-color: rgb(5, 5, 5);}")
        pass

    def create_connections(self):
        # self.button.clicked.connect(self._rename_sel)
        """[ RenamerUI ] UI Connections """

        self.bnt_IN.clicked.connect(lambda: self._rename(self.bnt_IN.text()))
        self.bnt_REF.clicked.connect(lambda: self._rename(self.bnt_REF.text()))
        self.bnt_OUT.clicked.connect(lambda: self._rename(self.bnt_OUT.text()))
        self.bnt_CTR.clicked.connect(lambda: self._rename(self.bnt_CTR.text()))
        self.bnt_DRV.clicked.connect(lambda: self._rename(self.bnt_DRV.text()))
        self.bnt_PRC.clicked.connect(lambda: self._rename(self.bnt_PRC.text()))

    def populate_menu(self):
        """[ RenamerUI ] UI Populate Menus """
        pass

    def selectionCallback(self, selection):
        if selection:
            if isinstance(selection[0], hou.Node):
                self.selected = selection
                self.lbl_node_name.setText(self.selected[0].name() + "->" + self.selected[0].type().name())
        else:
            self.lbl_node_name.setText("No Node Selected")

    def closeEvent(self, event):
        hou.ui.removeAllSelectionCallbacks()

    def _rename(self, prefix=""):
        if self.selected:
            self.selected[0].setName(prefix + self.txt_in.text() + "_" + self.selected[0].type().name().split("::")[0])
            self.selected[0].setColor(hou.Color(colors[prefix]))
            if prefix in ("__IN__", "OUT_", "REF_"):
                self.selected[0].setUserData('nodeshape', "null")
            else:
                self.selected[0].clearUserDataDict()


# [ GLOBAL HWND ]
RenamerUI_instance = None


# [ SHOW WINDOW FUNCTION ]
def show():
    global RenamerUI_instance
    if RenamerUI_instance:
        RenamerUI_instance.close()
    RenamerUI_instance = RenamerUI()
    RenamerUI_instance.show()
