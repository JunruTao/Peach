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
# [ File Name ] asset_ops_prep_name.py@python
# [ File Description ] - 2022.02.03 (Y.M.D) - 16:31
#                            *   *   *   *
#
#   This script contains asset operations
#
# ---------------------------------------------------------------------
import bpy
from peach import pImp, pAst, pDir
from peach.pBlender import pbu
pImp.reload(pAst, pDir)


def resolve():
    if bpy.data.filepath:
        wd = pDir.parent(bpy.data.filepath)
    else:
        import os
        wd = os.getcwd()
    pAst.reset()
    try:
        pAst.resolve(wd)
    finally:
        pass
    if pAst.current_lib():
        return True
    return False


def get_resolved_name():
    if resolve():
        if pAst.cwl() == pAst.__AST__:
            ast_ = pAst.current_asset()
            vrt_s = ast_.children()
            if len(vrt_s):
                vrt_ = vrt_s[0]
                return vrt_.form_new_object_name_mdl()
    return "__NOT_RESOLVED__"


class PbOpAssetPrepName(bpy.types.Operator):
    """
    Add Lights to the scene.
    """

    bl_idname = "peach.asset_prep_name"
    bl_label = "Peach Asset Prep Name"
    bl_option = {"REGISTER", "UNDO"}
    bl_context = "collection"

    def execute(self, context):
        current_coll = context.collection
        current_coll.name = get_resolved_name()
        return {"FINISHED"}


class PbOpPublishNewVersion(bpy.types.Operator):
    bl_idname = "peach.asset_publish_nv"
    bl_label = "Peach Publish New Version"
    bl_option = {"REGISTER", "UNDO"}
    bl_context = "collection"

    def execute(self, context):
        current_coll = context.collection
        current_coll.name = get_resolved_name()
        return {"FINISHED"}
