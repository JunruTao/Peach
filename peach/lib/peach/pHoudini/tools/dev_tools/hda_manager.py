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
# [ File Name ] hda_manager.py@python
# [ File Description ] - 2022.01.24 (Y.M.D) - 18:46
#                            *   *   *   *
#
#   [Peach-pQt-Dependent]This script contains Qt-UI Class of 
#   < HdaManagerUI > for "Peach Dev HDA Manager"
#
# ---------------------------------------------------------------------
import hou
import re
from peach.pQt.qHotel import QtWidgets, QtGui, QtCore
from peach.pQt import img, wgt
from peach import pImp, pGlob, pDir
from peach.pHoudini import wm, hNode
pImp.reload(img, pGlob, wm, hNode)


_look_up_sheet = {"PeachModel": ["peachM", "Peach[Model]", "hNode.Colors.Pk1", "peach_mdl"],
                  "PeachAsset": ["peachA", "Peach[Asset]", "hNode.Colors.Bl1", "peach_ast"],
                  "PeachUltraUrban": ["pUU", "Peach[UU]", "hNode.Colors.Pk1", "peach_uu"]}

_look_up_cats = {"PeachModel": ["Architecture",
                                "Utility",
                                "Generators",
                                "Mechanical",
                                "Nature",
                                "Panel"
                                ],
                 "PeachAsset": ["Utility",
                                "Material",
                                "IO",
                                "Instance",
                                "Scatter"
                                ],
                 "PeachUltraUrban": ["Building",
                                     "Road",
                                     "Scatter",
                                     ]}

_hda_shelf_def_str = """<?xml version="1.0" encoding="UTF-8"?>
<shelfDocument>
  <!-- This file contains definitions of shelves, toolbars, and tools.
 It should not be hand-edited when it is being used by the application.
 Note, that two definitions of the same element are not allowed in
 a single file. -->

  <tool name="$HDA_DEFAULT_TOOL" label="$HDA_LABEL" icon="$HDA_ICON">
    <toolMenuContext name="viewer">
      <contextNetType>SOP</contextNetType>
    </toolMenuContext>
    <toolMenuContext name="network">
      <contextOpType>$HDA_TABLE_AND_NAME</contextOpType>
    </toolMenuContext>
    <toolSubmenu>{}/{}</toolSubmenu>
    <script scriptType="python"><![CDATA[import soptoolutils
soptoolutils.genericTool(kwargs, '$HDA_NAME')]]></script>
  </tool>
</shelfDocument>
"""

_hda_OnCreated_str = """from peach.pHoudini import hNode
from peach import pIco

node_ = kwargs['node']
node_.setColor(hou.Color(*{col}))
img_path = pIco.getHouImg("{img}")
hNode.linkNetworkImage(node_, img_path, -0.8, -0.7, 0.9, 0.9)
"""

_hda_OnDeleted_str = """from peach.pHoudini import hNode

node_ = kwargs['node']
hNode.unlinkNetworkImage(node_)
"""

_hda_OnNameChanged_str = """from peach.pHoudini import hNode

node_ = kwargs['node']
old_name = kwargs['old_name']
old_path = "/".join([node_.parent().path(), old_name])
hNode.updateNetworkImage(node_, old_path)
"""


class HdaManagerUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        """[ HdaManagerUI ] UI Class Constructor """
        super(HdaManagerUI, self).__init__(parent, QtCore.Qt.WindowStaysOnTopHint)

        # /.Set UI init Position
        p = wm.getMainWindowCenter()
        self.setGeometry(p.x()-350, p.y()-130, 700, 260)
        self.setObjectName("pHoudini_tools_devtools_HdaManagerUI_widget")

        # /.Set Window Title, Icon
        self.setWindowTitle('Hda Manager - PeachPy v{0}'.format(pGlob.PEACH_PY_VERSION))
        self.setWindowIcon(QtGui.QIcon(img.getPixmap("devtool_hda_manager")))

        # /.Data Containers
        self._pkg_path = hou.getenv("PEACH_PACKAGES_PATH")
        self._hda_menu_entry = ""
        self._hda_label_name = ""
        self._hda_op_name = ""
        self._hda_file_name = ""
        self.selected = None

        self.create_widgets()
        self.create_layouts()
        self.create_style()
        self.create_connections()
        self.populate_menu()
        self.update_path()

        self.selectionCallback(hNode.listSelected())
        hou.ui.addSelectionCallback(self.selectionCallback)

    def create_widgets(self):
        """[ HdaManagerUI ] UI Define Widgets """

        ttl = "DevTool: HDA Manager"
        self.lbl_icon = wgt.getHeaderTemplateWidget(type="dev_tool",
                                                    title=ttl,
                                                    height=60,
                                                    font_size=23)
        self.lbl_package = QtWidgets.QLabel("package: ")
        self.cmb_packages = QtWidgets.QComboBox()

        self.txt_full_path = QtWidgets.QLineEdit("path")
        self.txt_full_path.setEnabled(False)
        self.lbl_menu_entry_1 = QtWidgets.QLabel("entry")
        self.cmb_menu_entries = QtWidgets.QComboBox()
        self.txt_hda_final_name = QtWidgets.QLineEdit("name")
        self.txt_hda_final_name.setEnabled(False)
        self.txt_hda_type_name = QtWidgets.QLineEdit("name")
        self.txt_hda_type_name.setEnabled(False)

        self.cmb_hda_v_major = QtWidgets.QComboBox()
        self.cmb_hda_v_minor = QtWidgets.QComboBox()
        self.txt_hda_name = QtWidgets.QLineEdit("hda name")

        self.bnt_new_hda = QtWidgets.QPushButton("Dump!!!!")
        self.bnt_new_hda.setFixedHeight(50)
        self.bnt_temp = QtWidgets.QPushButton("temp")

    def create_layouts(self):
        """[ HdaManagerUI ] UI Construct Layout """
        layout_main = QtWidgets.QVBoxLayout()
        layout_main.addWidget(self.lbl_icon)
        # /..Package Info
        lyt_pkg = QtWidgets.QHBoxLayout()
        lyt_pkg.addWidget(self.lbl_package)
        lyt_pkg.addWidget(self.cmb_packages)
        lyt_pkg.addWidget(self.lbl_menu_entry_1)
        lyt_pkg.addWidget(self.cmb_menu_entries)
        layout_main.addLayout(lyt_pkg, 1)

        # /..Hda Info
        lyt_hda_info = QtWidgets.QHBoxLayout()
        lyt_hda_info.addWidget(QtWidgets.QLabel("Version  major:"))
        lyt_hda_info.addWidget(self.cmb_hda_v_major)
        lyt_hda_info.addWidget(QtWidgets.QLabel("minor:"))
        lyt_hda_info.addWidget(self.cmb_hda_v_minor)
        lyt_hda_info.addWidget(QtWidgets.QLabel("name:"))
        lyt_hda_info.addWidget(self.txt_hda_name)
        layout_main.addLayout(lyt_hda_info)

        # /..FullPath
        layout_main.addWidget(self.txt_full_path)

        # /..Names
        lyt_hda_names = QtWidgets.QHBoxLayout()
        lyt_hda_names.addWidget(QtWidgets.QLabel("Name: "))
        lyt_hda_names.addWidget(self.txt_hda_final_name)
        lyt_hda_names.addWidget(QtWidgets.QLabel("Type Name: "))
        lyt_hda_names.addWidget(self.txt_hda_type_name)

        # /..Final Layout
        layout_main.addLayout(lyt_hda_names)
        layout_main.addWidget(self.bnt_new_hda)
        layout_main.addWidget(self.bnt_temp)
        layout_main.addStretch()
        self.setLayout(layout_main)

    def create_style(self):
        """[ HdaManagerUI ] UI Configure Styles """
        self.lbl_menu_entry_1.setAlignment(QtCore.Qt.AlignRight)
        pass

    def create_connections(self):
        """[ HdaManagerUI ] UI Connections """
        self.cmb_packages.currentTextChanged.connect(self.update_path)
        self.cmb_hda_v_major.currentTextChanged.connect(self.update_path)
        self.cmb_hda_v_minor.currentTextChanged.connect(self.update_path)
        self.txt_hda_name.textChanged.connect(self.update_path)
        self.bnt_new_hda.clicked.connect(self.create_hda_and_dump)
        self.bnt_temp.clicked.connect(self.add_definitions_temp)

    def populate_menu(self):
        """[ HdaManagerUI ] UI Populate Menus """
        # /. list packages:
        packages_names = pDir.listdir(hou.getenv("PEACH_PACKAGES_PATH"), n=True)
        packages_names.remove("PeachPy")
        self.cmb_packages.addItems(packages_names)

        # /.versions:
        self.cmb_hda_v_major.addItems([str(i) for i in range(1, 10)])
        self.cmb_hda_v_minor.addItems([str(i) for i in range(1, 10)])

    def update_path(self):
        # /.Hda Tab-Submenu Entry
        self._hda_menu_entry = _look_up_sheet[self.cmb_packages.currentText()][1] + "/"
        self.lbl_menu_entry_1.setText(self._hda_menu_entry)

        # /.Configure name
        op_cat = "sop"
        if self.selected:
            # /..Get Node Context: sop, lop, dop...
            op_cat = str(hNode.getCatStr(self.selected)).lower()
        name_ = re.sub(r"\W", '_', str(self.txt_hda_name.text()).lower())
        # /.Configure Prefix
        prefix = _look_up_sheet[self.cmb_packages.currentText()][0]
        # /.HDA filename
        self._hda_file_name = "{op}_{prf}_{n}.{vmj}.{vmn}.hdalc".format(op=op_cat,
                                                                        prf=prefix,
                                                                        n=name_,
                                                                        vmj=self.cmb_hda_v_major.currentText(),
                                                                        vmn=self.cmb_hda_v_minor.currentText())
        # /.HDA File Full path Compile
        _full_path = pDir.join(self._pkg_path, self.cmb_packages.currentText(), "wip/hda")
        _full_path = pDir.join(_full_path, self._hda_file_name)
        self.txt_full_path.setText(_full_path)
        self._hda_op_name = "{prf}_{n}::{vmj}.{vmn}".format(prf=prefix,
                                                            n=name_,
                                                            vmj=self.cmb_hda_v_major.currentText(),
                                                            vmn=self.cmb_hda_v_minor.currentText())
        # /.Type Name UI
        self.txt_hda_type_name.setText(self._hda_op_name)
        # /.HDA Label Name configure
        self._hda_label_name = prefix + " " + re.sub(r"\W", ' ', str(self.txt_hda_name.text()))
        self.txt_hda_final_name.setText(self._hda_label_name)
        # /.Repopulate menu
        self.cmb_menu_entries.clear()
        self.cmb_menu_entries.addItems(_look_up_cats[self.cmb_packages.currentText()])

    def create_hda_and_dump(self):
        if isinstance(self.selected, hou.Node):
            # /.Create HDA
            hda_node = self.selected.createDigitalAsset(name=self._hda_op_name,
                                                        hda_file_name=self.txt_full_path.text(),
                                                        description=self.txt_hda_final_name.text(),
                                                        min_num_inputs=len(self.selected.inputs()),
                                                        max_num_inputs=0,
                                                        )
            _sheet = _look_up_sheet[self.cmb_packages.currentText()]

            # /.Unlock Node
            hda_node.allowEditingOfContents()
            # /.Get HDA definition
            hda_def = hda_node.type().definition()
            # /.Write Extra Information
            hda_def.addSection("Tools.shelf", _hda_shelf_def_str.format(self._hda_menu_entry,
                                                                        self.cmb_menu_entries.currentText()))
            hda_def.addSection("OnCreated", _hda_OnCreated_str.format(col=_sheet[2],
                                                                      img=_sheet[3]))
            hda_def.addSection("OnDeleted", _hda_OnDeleted_str)
            hda_def.addSection("OnNameChanged", _hda_OnNameChanged_str)
            for sec in ("OnCreated", "OnDeleted", "OnNameChanged"):
                hda_def.setExtraFileOption("{}/IsPython".format(sec), True)
                hda_def.setExtraFileOption("{}/IsScript".format(sec), True)
            # /.Save definition
            hda_def.save(hda_def.libraryFilePath(), hda_node)

            # /.try create a new node:
            last_pos = hda_node.position()
            parent = hda_node.parent()
            hda_node.destroy()
            new_node = parent.createNode(self._hda_op_name)
            new_node.setPosition(last_pos)
            new_node.allowEditingOfContents()

    @staticmethod
    def add_definitions_temp():
        node_ = hNode.listSelected()[0]
        hda_def = node_.type().definition()
        _sheet = _look_up_sheet["PeachModel"]
        # /.Write Extra Information
        hda_def.addSection("OnCreated", _hda_OnCreated_str.format(col=_sheet[2],
                                                                  img=_sheet[3]))
        hda_def.addSection("OnDeleted", _hda_OnDeleted_str)
        hda_def.addSection("OnNameChanged", _hda_OnNameChanged_str)
        for sec in ("OnCreated", "OnDeleted", "OnNameChanged"):
            hda_def.setExtraFileOption("{}/IsPython".format(sec), True)
            hda_def.setExtraFileOption("{}/IsScript".format(sec), True)
        # /.Save definition
        hda_def.save(hda_def.libraryFilePath(), node_)

    def selectionCallback(self, selection):
        """[ RenamerUI ] Callback"""
        if selection and len(selection) == 1:
            self.selected = selection[0]
            if isinstance(self.selected, hou.Node):
                if self.selected.canCreateDigitalAsset():
                    self.cmb_packages.setEnabled(True)
                    self.cmb_hda_v_major.setEnabled(True)
                    self.cmb_hda_v_minor.setEnabled(True)
                    self.txt_hda_name.setEnabled(True)
                    self.bnt_new_hda.setEnabled(True)
                    self.txt_hda_name.setText(str(self.selected.name()).replace("_", " "))
                    return

        self.cmb_packages.setEnabled(False)
        self.cmb_hda_v_major.setEnabled(False)
        self.cmb_hda_v_minor.setEnabled(False)
        self.txt_hda_name.setEnabled(False)
        self.bnt_new_hda.setEnabled(False)
        self.selected = None

    def closeEvent(self, event):
        hou.ui.removeAllSelectionCallbacks()


# [ GLOBAL HWND ]
HdaManagerUI_instance = None


# [ SHOW WINDOW FUNCTION ]
def show():
    global HdaManagerUI_instance
    if HdaManagerUI_instance:
        HdaManagerUI_instance.close()
    HdaManagerUI_instance = HdaManagerUI()
    HdaManagerUI_instance.show()
