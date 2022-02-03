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
# [ File Name ] asset_ops_prep_ui.py@python
# [ File Description ] - 2022.02.03 (Y.M.D) - 13:34
#                            *   *   *   *
#
#   This script contains bAsset ui.
#
# ---------------------------------------------------------------------
import bpy
from peach import pGlob
from .asset_ops_prep_name import PbOpAssetPrepName


class PbUiAssetPrep(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Peach Asset Collection"
    bl_idname = "OBJECT_PT_PEACH_AST_COLL"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "collection"

    def draw(self, context):
        layout = self.layout
        coll = context.collection
        row = layout.row()
        row.label(text="Peach Version {}".format(pGlob.PEACH_VERSION), icon='WORLD_DATA')
        row = layout.row()
        row.label(text="Active Collection is: " + coll.name)
        row = layout.row()
        row.prop(data=coll, property="name")
        row = layout.row()
        row.operator(PbOpAssetPrepName.bl_idname)
