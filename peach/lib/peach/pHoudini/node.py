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
# [ File Name ] node.py@python
# [ File Description ] - 2022.01.13 (Y.M.D) - 22:18
#                            *   *   *   *
#
#   This script contains
#
# ---------------------------------------------------------------------
import hou
from peach import pImp
from peach import pLog
pImp.reload(pLog)


def select(node=None):
    """
    [ Node ] Select Node
    @param node: node to select
    """
    if node:
        node.setSelected(True, clear_all_selected=True)


def deselect(node=None):
    """
    [ Node ] Deselect Node,
    If no node is provided, all the selected nodes will be cleared out.
    @param node: node to deselect
    """
    if node:
        node.setSelected(False, clear_all_selected=True)
    else:
        hou.clearAllSelected()


def listSelected(item=False, connection=False, bundle=False):
    """
    [ Node/Item ] List selected
    @param item: (bool) if list selected items
    @param connection: (bool) if list selected connections
    @param bundle: (bool) if list selected bundle
    @return: tuple of hou items
    """
    if item:
        return hou.selectedItems()
    elif connection:
        return hou.selectedConnections()
    elif bundle:
        return hou.selectedNodeBundles()
    return hou.selectedNodes()


def rename(node=None, name="", sel=False):
    """
    [ Node ] Rename Houdini Node
    @param node: (hou.Node) houdini node
    @param name: (str)target name to rename to
    @param sel: (bool) if query selected
    """
    if sel:
        node = hou.selectedNodes()[0]
    if not node:
        return
    node.setName(name, unique_name=True)



