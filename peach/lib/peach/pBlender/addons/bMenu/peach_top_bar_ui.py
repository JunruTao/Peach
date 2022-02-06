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
# [ File Name ] peach_top_bar_ui.py@python
# [ File Description ] - 2022.02.05 (Y.M.D) - 21:34
#                            *   *   *   *
#
#   This script contains
#
# ---------------------------------------------------------------------
import bpy
from peach.pBlender.addons.bAsset.asset_ops_import_layout import PbOpImportLayout


class TOPBAR_MT_peach_menu(bpy.types.Menu):
    bl_label = "Peach"

    def draw(self, context):
        layout = self.layout
        layout.operator(PbOpImportLayout.bl_idname)

    def menu_draw(self, context):
        self.layout.menu(TOPBAR_MT_peach_menu.__name__)
