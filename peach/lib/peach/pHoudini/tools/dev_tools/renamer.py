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
#   < RenamerUI > for Dev Tool UI Creation toDO: fix the styling issue. maybe not using the dict
#
# ---------------------------------------------------------------------
import hou
from peach.pQt.qHotel import QtWidgets, QtCore, QtGui
from peach import pImp, pGlob, pLog, pDir, pIco
from peach.pQt import img, style
from peach.pHoudini import hNode, wm
pImp.reload(hNode, wm, pGlob, img, style, pLog, pDir, pIco)


_types = {
    "IN": [(1.000, 1.000, 1.0000), (0, 0), "input"],
    "OUT": [(1.000, 0.572, 0.019), (1, 0), "output"],
    "REF": [(0.560, 0.780, 0.745), (2, 0), "reference"],
    "CTR": [(0.945, 0.164, 0.152), (0, 1), "control"],
    "DRV": [(0.031, 0.478, 0.749), (1, 1), "driven"],
    "PRC": [(0.478, 0.478, 0.478), (2, 1), "procedural"]
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
        self.setObjectName("pHoudini_tools_devtools_RenamerUI_widget")

        # /.Set Window Title, Icon
        self.setWindowTitle('Renamer - PeachPy v{0}'.format(pGlob.PEACH_PY_VERSION))
        self.setWindowIcon(QtGui.QIcon(img.getPixmap("peach_dev")))

        # /.Data Containers
        self.uis_lbl = dict()
        self.uis_lbl_style = dict()
        self.uis_bnt = dict()
        self.uis_bnt_style = dict()
        self.uis_txt = dict()
        self.uis_txt_style = dict()

        # /. Build UI Functions
        self.create_widgets()
        self.create_style()
        self.create_layouts()
        self.create_connections()
        self.populate_menu()

        # /. Register Callback
        hou.ui.addSelectionCallback(self.selectionCallback)

    def create_widgets(self):
        """[ RenamerUI ] UI Define Widgets """
        self.lbl_icon = QtWidgets.QLabel()
        logo = img.getPixmap(pIco.DP.white256())
        self.lbl_icon.setPixmap(logo.scaledToHeight(70, QtCore.Qt.SmoothTransformation))
        self.lbl_node_name = QtWidgets.QLabel("No Node Selected")
        for tp, dt in _types.items():
            self.uis_bnt[tp] = QtWidgets.QPushButton(dt[2])

        self.txt_in = QtWidgets.QLineEdit("subject")

    def create_layouts(self):
        """[ RenamerUI ] UI Construct Layout """
        layout_main = QtWidgets.QVBoxLayout()
        layout_main.addWidget(self.lbl_icon)
        layout_main.addWidget(self.lbl_node_name)
        layout_main.addWidget(self.txt_in)
        wgt_layout_buttons = QtWidgets.QWidget()
        layout_buttons = QtWidgets.QGridLayout()

        for tp, bnt in self.uis_bnt.items():
            layout_buttons.addWidget(bnt, *_types[tp][1])

        wgt_layout_buttons.setLayout(layout_buttons)
        layout_main.addWidget(wgt_layout_buttons)
        layout_main.addStretch()
        self.setLayout(layout_main)

    def create_style(self):
        """[ RenamerUI ] UI Configure Styles """
        for tp, dt in _types.items():
            s_sheet = style.Sheet(cat=style.C.bnt)
            s_sheet.newState()
            s_sheet.setTextColor(0.9, 0, 0)
            s_sheet.setBorderStyle()
            s_sheet.setBorderWidth(3)
            s_sheet.setBackgroundColor(*dt[0])
            self.uis_bnt_style[tp] = s_sheet
            self.uis_bnt[tp].setStyleSheet(s_sheet.get())

        # todo: set self style sheet
        s_sheet = style.Sheet(self)
        s_sheet.newState()
        s_sheet.setBackgroundColor(5, 5, 100)
        self.setStyleSheet(s_sheet.get())

    def create_connections(self):
        # self.button.clicked.connect(self._rename_sel)
        """[ RenamerUI ] UI Connections """
        for key, bnt in self.uis_bnt.items():
            bnt.clicked.connect(lambda: self._rename())

    def populate_menu(self):
        """[ RenamerUI ] UI Populate Menus """
        print("----")
        pLog.debug(self.uis_bnt["OUT"].styleSheet())
        pass

    def selectionCallback(self, selection):
        if selection:
            if isinstance(selection[0], hou.Node):
                self.selected = selection
                self.lbl_node_name.setText(self.selected[0].name() + " -> " + hNode.getTypeStr(self.selected[0]))
        else:
            self.lbl_node_name.setText("No Node Selected")
            self.selected = None

    def closeEvent(self, event):
        hou.ui.removeAllSelectionCallbacks()

    def _rename(self):
        if self.selected:
            prefix = ""
            for tp, bnt in self.uis_bnt.items():
                if bnt.clicked():
                    prefix = tp
                    break
            self.selected[0].setName(prefix + "_" + self.txt_in.text() + "_" + hNode.getTypeStr(self.selected[0]))
            self.selected[0].setColor(hou.Color(*_types[prefix][0]))
            if prefix in ("IN", "OUT", "REF"):
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
