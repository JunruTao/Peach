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
import nodegraphutils
from peach import pImp, pLog, pUtil
from peach.pHoudini import wm
pImp.reload(pLog, pUtil, wm)


class Colors(object):
    Pk1 = (0.98, 0.784, 1)
    Bl1 = (0.616, 0.871, 0.769)


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
    return list(hou.selectedNodes())


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


def linkNetworkImage(node=None, filepath="", x=0.0, y=0.0, w=0.7, h=0.7):
    """
    [ Node ] Create a hou.NetworkImage object and link to the Node.
    <br> - when node deleted, this image will be removed.
    <br> - when by-pass the node, image should change transparency
    @param node: (hou.Node) node object
    @param filepath: (str) image file path
    @param x: (float) x position
    @param y: (float) y position
    @param w: (float) width
    @param h: (float) height
    """
    if not isinstance(node, hou.Node):
        # /.not houdini node object
        return

    editor = wm.getCurrentEditor()
    image = hou.NetworkImage()
    image.setPath(filepath)
    image.setRect(hou.BoundingRect(x, y, x + w, y + h))
    image.setRelativeToPath(node.path())
    images = list(editor.backgroundImages())
    images.append(image)
    try:
        editor.setBackgroundImages(images)
        nodegraphutils.saveBackgroundImages(node.parent(), images)
    finally:
        pass


def unlinkNetworkImage(node=None):
    """
    [ Node ] Unlink all Network Images attached to this node.
    @param node: (hou.Node) node object
    """
    editor = wm.getCurrentEditor()
    images = list(editor.backgroundImages())
    img_culled = []
    for i in images:
        if node.path() != i.relativeToPath():
            img_culled.append(i)
    try:
        editor.setBackgroundImages(img_culled)
        nodegraphutils.saveBackgroundImages(node.parent(), img_culled)
    finally:
        pass


def updateNetworkImage(new_node=None, old_path=""):
    """
    [ Node ] Update Network Images - Transfer image from old to new node
    @param new_node: (hou.Node) node object to.
    @param old_path: (str) old node path
    """
    editor = wm.getCurrentEditor()
    images = list(editor.backgroundImages())
    img_culled = []
    found = False
    for i in images:
        if old_path == i.relativeToPath():
            i.setRelativeToPath(new_node.path())
            found = True
        img_culled.append(i)
    if not found:
        return
    try:
        editor.setBackgroundImages(img_culled)
        nodegraphutils.saveBackgroundImages(new_node.parent(), images)
    finally:
        pass
