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
# [ File Name ] hNode.py@python
# [ File Description ] - 2022.01.13 (Y.M.D) - 22:18
#                            *   *   *   *
#
#   This script handles hou.Node related functions
#
# ---------------------------------------------------------------------
import hou
from peach import pImp, pLog, pUtil
pImp.reload(pLog, pUtil)


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


def getTypeStr(node=None):
    """
    [ Node ] Get Name of the node.Type
    @param node: (hou.Node) houdini node
    @return: (str) node type name
    """
    if isinstance(node, hou.Node):
        # for nodes that has HDA versions, should remove "::"
        return str(node.type().name()).split("::")[0]
    else:
        return ""


def getCatStr(node=None):
    """
    [ Node ] Get Category Name of the Node
    @param node: (hou.Node) houdini node
    @return: (str) node category name
    """
    if isinstance(node, hou.Node):
        # for nodes that has HDA versions, should remove "::"
        return node.type().category().name()
    else:
        return ""
