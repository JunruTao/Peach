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
import re
from peach.pQt.qHotel import QtWidgets, QtCore, QtGui
from peach import pImp, pGlob, pLog, pDir, pIco
from peach.pQt import img, style, wgt
from peach.pHoudini import hNode, wm
pImp.reload(hNode, wm, pGlob, img, style, pLog, pDir, pIco, wgt)


_types = {
    "input": ["IN", (1.000, 1.000, 1.0000)],
    "output": ["OUT", (1.000, 0.572, 0.019)],
    "reference": ["REF", (0.560, 0.780, 0.745)],
    "control": ["CTR", (0.945, 0.164, 0.152)],
    "driven": ["DRV", (0.031, 0.478, 0.749)],
    "procedural": ["PRC", (0.478, 0.478, 0.478)]
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
        self.setWindowIcon(QtGui.QIcon(img.getPixmap("devtool_renamer")))

        # /. Build UI Functions
        self.create_widgets()
        self.create_style()
        self.create_layouts()
        self.create_connections()

        self.prefix_checks = []
        for key, lst in _types.items():
            self.prefix_checks.append(lst[0])
            self.prefix_checks += ["OPT"]  # append any extra prefixes

        # /. Register Callback
        self.selectionCallback(hNode.listSelected())
        hou.ui.addSelectionCallback(self.selectionCallback)

    def create_widgets(self):
        """[ RenamerUI ] UI Define Widgets """
        # /.title
        ttl = "DevTool: Sop Renamer"
        self.lbl_icon = wgt.getHeaderTemplateWidget(type="dev_tool",
                                                    title=ttl,
                                                    height=70,
                                                    font_size=23)

        # /.node name
        self.txt_node_name = QtWidgets.QLineEdit("No Node Selected")

        # /.subject name
        self.txt_in_cached = ""
        self.txt_in = QtWidgets.QLineEdit("subject")

        # /.renamer buttons
        self.bnt_in = QtWidgets.QPushButton("input")
        self.bnt_out = QtWidgets.QPushButton("output")
        self.bnt_ref = QtWidgets.QPushButton("reference")
        self.bnt_ctr = QtWidgets.QPushButton("control")
        self.bnt_drv = QtWidgets.QPushButton("driven")
        self.bnt_prc = QtWidgets.QPushButton("procedural")

        self.buttons = [self.bnt_in,
                        self.bnt_out,
                        self.bnt_ref,
                        self.bnt_ctr,
                        self.bnt_drv,
                        self.bnt_prc]

    def create_layouts(self):
        """[ RenamerUI ] UI Construct Layout """
        layout_main = QtWidgets.QVBoxLayout()
        # /. header icon.
        layout_main.addWidget(self.lbl_icon)
        # /. node name section
        layout_main.addWidget(self.txt_node_name)
        layout_main.addWidget(self.txt_in)
        # /.Buttons Section
        wgt_layout_buttons = QtWidgets.QWidget()
        layout_buttons = QtWidgets.QGridLayout()
        # /.. adding buttons to a grid
        layout_buttons.addWidget(self.bnt_in, 0, 0)
        layout_buttons.addWidget(self.bnt_out, 1, 0)
        layout_buttons.addWidget(self.bnt_ref, 2, 0)
        layout_buttons.addWidget(self.bnt_ctr, 0, 1)
        layout_buttons.addWidget(self.bnt_prc, 1, 1)
        layout_buttons.addWidget(self.bnt_drv, 2, 1)
        wgt_layout_buttons.setLayout(layout_buttons)
        layout_main.addWidget(wgt_layout_buttons)
        # /.wrap up main layout
        layout_main.addStretch()
        self.setLayout(layout_main)

    def create_style(self):
        """[ RenamerUI ] UI Configure Styles """

        # /. create basic button styles:
        s_sheet = style.Sheet(cat=style.BUTTON)
        s_sheet.setTextColor(0.9)
        s_sheet.setBorderStyle()
        s_sheet.setBorderWidth(0)
        s_sheet.setBorderRadius(5)
        s_sheet.setBackgroundColor(0.3)
        s_sheet.setFont(style.fnt_Arial, 16, i=True, b=True)
        # /. set style sheet
        sheet = s_sheet.get()
        for b in self.buttons:
            b.setStyleSheet(sheet)
            b.setFixedHeight(28)

        # /.main background
        s_sheet.newState()
        s_sheet.setObject(self)
        s_sheet.setBackgroundColor(62, 9, 35)
        s_sheet.assign(self)

    def create_connections(self):
        """[ RenamerUI ] UI Connections """
        self.bnt_in.clicked.connect(lambda: self._rename(self.bnt_in.text()))
        self.bnt_out.clicked.connect(lambda: self._rename(self.bnt_out.text()))
        self.bnt_ref.clicked.connect(lambda: self._rename(self.bnt_ref.text()))
        self.bnt_ctr.clicked.connect(lambda: self._rename(self.bnt_ctr.text()))
        self.bnt_drv.clicked.connect(lambda: self._rename(self.bnt_drv.text()))
        self.bnt_prc.clicked.connect(lambda: self._rename(self.bnt_prc.text()))

    def selectionCallback(self, selection):
        """[ RenamerUI ] Callback"""
        if selection:
            self.selected = selection
            if len(selection) == 1:
                sl = selection[0]
                if isinstance(sl, hou.Node) and not isinstance(sl, hou.NetworkDot):
                    # /.if user already renamed this node to something, this should be changed.
                    if hNode.getTypeStr(sl) not in sl.name():
                        _name = str(sl.name())
                        for k in self.prefix_checks:
                            if k in _name:
                                _name = _name.replace(k + "_", "")
                        self.txt_in_cached = self.txt_in.text()
                        self.txt_in.setText(_name)
                    elif self.txt_in_cached:
                        self.txt_in.setText(self.txt_in_cached)
                    else:
                        self.txt_in_cached = self.txt_in.text()
                    self.txt_node_name.setText(hNode.getTypeStr(sl))
                    self.txt_node_name.setEnabled(True)
            else:
                self.selected = []
                for sl in selection:
                    if isinstance(selection[0], hou.Node):
                        self.selected.append(sl)
                self.txt_node_name.setText(" ... ")
                self.txt_node_name.setDisabled(True)
        else:
            self.txt_node_name.setText("No Node Selected")
            self.txt_node_name.setDisabled(True)
            self.selected = None

    def closeEvent(self, event):
        hou.ui.removeAllSelectionCallbacks()

    def _rename(self, name=""):
        if self.selected:
            prefix = _types[name][0]
            color = _types[name][1]
            suffix = self.txt_node_name.text()
            subject = self.txt_in.text()
            # subject_formatting
            if " " in subject:
                subjects = subject.split(" ")
                subject = ""
                for i in range(len(subjects)):
                    if i > 0:
                        subjects[i] = subjects[i].capitalize()
                        subject = "{}.{}".format(subject, subjects[i])
                    else:
                        subject = subjects[i]
            subject = re.sub(r"\W\.-", '_', subject)
            # /. foreach node
            for sl in self.selected:
                # /..specific namings:
                if "switch" in hNode.getTypeStr(sl):
                    prefix = "OPT"
                    color = hNode.Colors.Bl1
                # /..change suffix to each nodeType if multiple
                if len(self.selected) != 1:
                    suffix = hNode.getTypeStr(sl)
                # /..avoid super long names
                if "_" in subject:
                    suffix = ""
                else:
                    suffix = "_" + suffix
                with hou.undos.group("Renamer-Rename Nodes"):
                    # /..change name and color
                    sl.setName(prefix + "_" + subject + suffix, unique_name=True)
                    sl.setColor(hou.Color(*color))
                    # /..setting node shape
                    sl.clearUserDataDict()
                    if name in ("input", "output", "reference"):
                        sl.setUserData('nodeshape', "null")


# [ GLOBAL HWND ]
RenamerUI_instance = None


# [ SHOW WINDOW FUNCTION ]
def show():
    global RenamerUI_instance
    if RenamerUI_instance:
        RenamerUI_instance.close()
    RenamerUI_instance = RenamerUI()
    RenamerUI_instance.show()
