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
from peach.pQt.qHotel import QtWidgets, QtCore, QtGui
from peach import pImp, pGlob, pLog, pDir, pAst
from peach.pQt import img, style, wgt
from peach.pHoudini import hNode, wm
pImp.reload(pGlob, pLog, pDir, img, style, wgt, hNode, wm, pAst)
import hou


# [ TYPEDEF ]
Itm = QtGui.QStandardItem


# noinspection PyTypeChecker
class AssetManagerUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        """[ AssetManagerUI ] UI Class Constructor """
        super(AssetManagerUI, self).__init__(parent)
        # /.Set UI init Position
        self.setObjectName("pHoudini_pAsset_AssetManager_widget")

        # /.data
        self._lib = None
        self._selected = None
        self._ui_expand_dict = dict()
        self._refresh_lib()
        if self._lib:
            # /.init library
            self.create_widgets()
            self.populate_menu()
            self.create_style()
            self.create_layouts()
            self.create_connections()
        else:
            self.create_unresolved_msg()

    def create_unresolved_msg(self):
        _layout = QtWidgets.QVBoxLayout()
        _layout.addWidget(QtWidgets.QLabel("<b>Unable To Resolve Asset Library</b><br>" +
                                           "Please Make Sure set the correct working dir(\"$HIP\")"))
        self.setLayout(_layout)

    def create_widgets(self):
        """[ AssetManagerUI ] UI Define Widgets """
        # /.title
        ttl = "Peach Asset Manager v1.0"
        self.lbl_icon = wgt.getHeaderTemplateWidget(type="dev_tool",
                                                    title=ttl,
                                                    height=70,
                                                    font_size=23)

        # /.data tree init:
        self.tw_structure = QtWidgets.QTreeView()
        self.tw_structure.setHeaderHidden(True)
        self.tw_structure.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tw_structure.customContextMenuRequested.connect(self._open_menu)
        self.tree_mdl = None
        self.bnt_refresh = QtWidgets.QPushButton("Refresh")

    def create_layouts(self):
        """[ AssetManagerUI ] UI Construct Layout """
        layout_main = QtWidgets.QVBoxLayout()
        # /.add header
        layout_main.addWidget(self.lbl_icon)
        # /.add asset view
        layout_main.addWidget(self.tw_structure)
        # /.button layout
        layout_bnt = QtWidgets.QHBoxLayout()
        layout_bnt.addWidget(self.bnt_refresh)
        layout_main.addLayout(layout_bnt)
        # /.final layout
        self.setLayout(layout_main)

    def create_style(self):
        """[ AssetManagerUI ] UI Configure Styles """
        pass

    def create_connections(self):
        """[ AssetManagerUI ] UI Connections """
        self._connect_tw_mdl_to_selection_mdl()
        self.bnt_refresh.clicked.connect(self._A_refresh)

    def _connect_tw_mdl_to_selection_mdl(self):
        # /. selection callback connection (pyqt4)
        QtCore.QObject.connect(self.tw_structure.selectionModel(),
                               QtCore.SIGNAL('selectionChanged(QItemSelection, QItemSelection)'),
                               self.selection_change)

    def populate_menu(self):
        """[ AssetManagerUI ] UI Populate Menus """
        self.tree_mdl = QtGui.QStandardItemModel()
        rootNode = self.tree_mdl.invisibleRootItem()

        i_lib = Itm()
        i_lib.setData(self._lib.name(), QtCore.Qt.DisplayRole)
        i_lib.setData(self._lib, QtCore.Qt.UserRole)
        i_lib.setIcon(img.getPixmap("peachFolder_library"))
        for n_cat, cat in self._lib.children_dict().items():
            i_cat = Itm()
            if cat.name() in ["lib_materials", "lib_textures"]:
                i_cat.setIcon(img.getPixmap("peachFolder_design"))
            else:
                i_cat.setIcon(img.getPixmap("peachFolder"))
            i_cat.setData(n_cat, QtCore.Qt.DisplayRole)
            i_cat.setData(cat, QtCore.Qt.UserRole)
            for n_typ, typ in cat.children_dict().items():
                i_typ = Itm()
                i_typ.setData(n_typ, QtCore.Qt.DisplayRole)
                i_typ.setData(typ, QtCore.Qt.UserRole)
                i_typ.setIcon(img.getPixmap("peachFolder_dev"))
                for n_ast, ast in typ.children_dict().items():
                    i_ast = Itm()
                    i_ast.setData(n_ast, QtCore.Qt.DisplayRole)
                    i_ast.setData(ast, QtCore.Qt.UserRole)
                    i_ast.setIcon(img.getPixmap("peachFolder_doc"))
                    for n_stv, stv in ast.children_dict().items():
                        i_stv = Itm()
                        i_stv.setData(n_stv, QtCore.Qt.DisplayRole)
                        i_stv.setData(stv, QtCore.Qt.UserRole)
                        i_stv.setIcon(img.getPixmap("peach_fwhite"))
                        i_ast.appendRow(i_stv)
                    i_typ.appendRow(i_ast)
                i_cat.appendRow(i_typ)
            i_lib.appendRow(i_cat)
        rootNode.appendRow(i_lib)
        self.tw_structure.setModel(self.tree_mdl)
        self.tw_structure.expandRecursively(self.tree_mdl.index(0, 0), 2)
        # /. set Non Editable
        self.tw_structure.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    @QtCore.Slot("QItemSelection, QItemSelection")
    def selection_change(self, *args):
        # print(args[0].indexes()[0].data(QtCore.Qt.DisplayRole))
        self._selected = args[0].indexes()[0].data(QtCore.Qt.UserRole)

    def _refresh_lib(self):
        pAst.reset()
        value = pAst.resolve(hou.getenv('HIP'))
        if value != -2:
            self._lib = pAst.current_lib()

    def _A_refresh(self):
        self._selected = None
        self._refresh_lib()
        if self.tree_mdl:
            self.tree_mdl.deleteLater()
        self.populate_menu()
        self._connect_tw_mdl_to_selection_mdl()

    def _open_menu(self, position):
        indexes = self.tw_structure.selectedIndexes()
        if len(indexes) > 0:
            level = 0
            index = indexes[0]
            while index.parent().isValid():
                index = index.parent()
                level += 1
            menu = QtWidgets.QMenu()

            if level == 0:
                # /..Lib Lvl
                _action_0 = QtWidgets.QAction("Add New Category")
                _action_0.triggered.connect(self._MA_new_cat)
                menu.addAction(_action_0)

            elif level == 1:
                # /..Category Lvl
                _action_0 = QtWidgets.QAction("Add New Type")
                _action_0.triggered.connect(self._MA_new_type)
                menu.addAction(_action_0)

            elif level == 2:
                # /..Type Lvl
                _action_0 = QtWidgets.QAction("Add New Asset")
                _action_0.triggered.connect(self._MA_new_asset)
                menu.addAction(_action_0)

            elif level == 3:
                # /..Asset Lvl
                _action_0 = QtWidgets.QAction("Add New Step Variant")
                _action_0.triggered.connect(self._MA_new_step_variant)
                menu.addAction(_action_0)

                _action_1 = QtWidgets.QAction("Create New Asset Variant")
                _action_1.triggered.connect(self._MA_new_asset_variant)
                menu.addAction(_action_1)

            if level != 0:
                _action_h = QtWidgets.QAction("Save Dev File")
                _action_h.triggered.connect(self._MA_save_dev_file)
                menu.addAction(_action_h)

                _action_d = QtWidgets.QAction("Delete")
                _action_d.triggered.connect(self._MA_delete)
                menu.addAction(_action_d)

            menu.exec_(self.tw_structure.viewport().mapToGlobal(position))

    def _menu_action_t(self, u_title="", **kwargs):
        dialog = DiaUI(title=u_title,
                       subject=self._selected.name(),
                       fields=kwargs)
        if dialog.exec_():
            return dialog.GetValue()
        return None

    def _MA_new_cat(self):
        if isinstance(self._selected, pAst.Lib):
            u_title = "New Category"
            k_name = "Category Name"
            k_opt = "Nickname(Code)"
            data = {k_name: "",
                    k_opt: ""}
            result = self._menu_action_t(u_title, **data)
            if result:
                self._selected.new_cat(result[k_name], result[k_opt])
                self._A_refresh()

    def _MA_new_type(self):
        if isinstance(self._selected, pAst.Cat):
            u_title = "New Type"
            k_name = "Type Name"
            data = {k_name: ""}
            result = self._menu_action_t(u_title, **data)
            if result:
                self._selected.new_type(result[k_name])
                self._A_refresh()

    def _MA_new_asset(self):
        if isinstance(self._selected, pAst.Typ):
            u_title = "New Asset"
            k_name = "Asset Name"
            data = {k_name: ""}
            result = self._menu_action_t(u_title, **data)
            if result:
                self._selected.new_asset(result[k_name])
                self._A_refresh()

    def _MA_new_step_variant(self):
        if isinstance(self._selected, pAst.Ast):
            self._selected.new_step_variant()
            self._A_refresh()

    def _MA_new_asset_variant(self):
        if isinstance(self._selected, pAst.Ast):
            self._selected.new_asset_variant()
            self._A_refresh()

    def _MA_delete(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("pAst Delete Entity")
        msg_box.setWindowIcon(img.getPixmap("peach_dev"))
        msg_box.move(QtGui.QCursor.pos() - QtCore.QPoint(180, 100))
        msg_box.setFixedSize(360, 200)
        if isinstance(self._selected, pAst.Struct):
            if self._selected.deletable():
                msg_box.setIcon(QtWidgets.QMessageBox.Question)
                msg_box.setInformativeText("Delete<br><b>{}</b> ?".format(self._selected.name()))
                msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
                if msg_box.exec_() == QtWidgets.QMessageBox.Yes:
                    if self._selected.delete():
                        self._A_refresh()
                        return
                    else:
                        msg_box = QtWidgets.QMessageBox()
                        msg_box.setWindowTitle("pAst Delete Entity")
                        msg_box.setWindowIcon(img.getPixmap("peach_dev"))
                        msg_box.move(QtGui.QCursor.pos() - QtCore.QPoint(180, 100))
                        msg_box.setFixedSize(360, 200)
                        msg_box.setInformativeText("<b>{}</b><br>Unable to delete Item".format(self._selected.name()))
                        msg_box.setStandardButtons(QtWidgets.QMessageBox.Discard)
                        msg_box.setIcon(QtWidgets.QMessageBox.Warning)
                        return msg_box.exec_()
                else:
                    return
            msg_box.setInformativeText("<b>{}</b><br>Is not Deletable".format(self._selected.name()))
            msg_box.setIcon(QtWidgets.QMessageBox.Warning)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Discard)
            return msg_box.exec_()

    def _MA_save_dev_file(self):
        if isinstance(self._selected, pAst.Typ) or isinstance(self._selected, pAst.Ast):
            path_ = pDir.join(self._selected.path(), "dev")
            name_ = self._selected.name()
            if not pDir.exists(path_):
                pDir.mkdir(path_)
            existing_files = [f for f in pDir.listfiles(path_, n=True) if name_ in f]
            versions_ = [1]
            if existing_files:
                for f in existing_files:
                    versions_.append(int(pDir.remove_ext(f).split(".v")[-1]))
            wm.save_file(path_, "{0}.v{1:03d}".format(name_, max(versions_)))


class DiaUI(QtWidgets.QDialog):
    def __init__(self, title="", subject="", fields=None, parent=None):
        QtWidgets.QDialog.__init__(self, parent, QtCore.Qt.WindowStaysOnTopHint)

        # /.Set UI init Position
        p = wm.getMainWindowCenter()
        self.setGeometry(p.x(), p.y(), 500, 260)
        # self.setObjectName("pHoudini_dialog_popup_{}".format(title))

        # /.Set Window Title, Icon
        self.setWindowTitle('{0} - PeachPy v{1}'.format(title, pGlob.PEACH_PY_VERSION))
        self.setWindowIcon(QtGui.QIcon(img.getPixmap("peach_dev")))

        # /.UI - layout
        _layout = QtWidgets.QVBoxLayout()
        _layout.addWidget(QtWidgets.QLabel("<i>{0}</i> -> <b>{1}</b>".format(subject, title)))
        # /.data:
        self.result = dict()
        self.txt_ins = dict()
        if isinstance(fields, dict):
            for name, val in fields.items():
                _lay_line = QtWidgets.QHBoxLayout()
                self.result[name] = val
                edit_ = QtWidgets.QLineEdit(val)
                edit_.setFixedWidth(250)
                self.txt_ins[name] = edit_
                lbl_name_ = QtWidgets.QLabel("{}: ".format(name))
                lbl_name_.setFixedWidth(140)
                _lay_line.addWidget(lbl_name_)
                _lay_line.addWidget(self.txt_ins[name])
                _layout.addLayout(_lay_line)

        # /.UI - Buttons
        _lay_line = QtWidgets.QHBoxLayout()
        self.but_ok = QtWidgets.QPushButton("OK")
        self.but_ok.clicked.connect(self.OnOk)
        self.but_cancel = QtWidgets.QPushButton("Cancel")
        self.but_cancel.clicked.connect(self.OnCancel)

        # /.UI - Add to Main
        _lay_line.addWidget(self.but_ok)
        _lay_line.addWidget(self.but_cancel)
        _layout.addLayout(_lay_line)
        _layout.addStretch()
        self.setLayout(_layout)
        self.adjustSize()
        self.setFixedSize(self.size())

    def OnCancel(self):
        self.done(0)

    def OnOk(self):
        hit = 0
        for k, v in self.txt_ins.items():
            if v.text():
                hit += 1
            self.result[k] = v.text()
        if not bool(hit):
            self.done(0)
            return
        self.done(1)
        return self.result

    def GetValue(self):
        return self.result
