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
# [ File Name ] __init__.py@python
# [ File Description ] - 2022.02.05 (Y.M.D) - 21:32
#                            *   *   *   *
#
#   This script contains
#
# ---------------------------------------------------------------------
import bpy
from peach import pImp
from peach.pBlender import pbu
from . import (peach_top_bar_ui,
               )

pImp.reload(peach_top_bar_ui,
            )

classes = (
    peach_top_bar_ui.TOPBAR_MT_peach_menu,
)


bl_info = {
    "name": "bAsset",
    "blender": (3, 0, 0),
    "author": "Digital Peach Studio",
    "version": (1, 0),
    "category": "User Interface",
}


def register():
    pbu.r_cls(*classes)
    bpy.types.TOPBAR_MT_editor_menus.append(peach_top_bar_ui.TOPBAR_MT_peach_menu.menu_draw)


def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(peach_top_bar_ui.TOPBAR_MT_peach_menu.menu_draw)
    pbu.u_cls(*classes)
