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
from peach import pImp, pAst, pDir, pLog
from peach.pBlender import pbu
pImp.reload(pAst, pDir, pLog)


_SELECTED_VARIANT = 'A'


def resolve():
    if bpy.data.filepath:
        wd = pDir.parent(bpy.data.filepath)
        pAst.reset()
        try:
            pAst.resolve(wd)
        finally:
            pass
        if pAst.current_lib():
            return True
    pLog.error("File is not saved, Please make sure save the file under asset/dev",
               fn=resolve, cls=pDir.fileNameBare(__file__))
    return False


def get_resolved_name():
    if resolve():
        if pAst.cwl() == pAst.__AST__:
            ast_ = pAst.current_asset()
            vrt_s = ast_.children_dict()
            vrt_ = vrt_s.get(_SELECTED_VARIANT)
            if vrt_:
                return vrt_.form_new_object_name_mdl()
    return "__NOT_IN_ASSET_DEV__"


def publish_new_version():
    if resolve():
        if pAst.cwl() == pAst.__AST__:
            ast_ = pAst.current_asset()
            vrt_s = ast_.children_dict()
            vrt_ = vrt_s.get(_SELECTED_VARIANT)
            if vrt_:
                assert isinstance(vrt_, pAst.Vrt)
                f_name_bare = vrt_.form_new_filename_mdl_mE()
                base_path = pDir.join(vrt_.path(), f_name_bare)
                fp_blend = base_path + ".blend"
                fp_fbx = base_path + ".fbx"
                name = vrt_.form_new_object_name_mdl()
                col = bpy.data.collections.get(name)
                if col:
                    for obj_ in col.objects:
                        obj_.select_set(True)
                    pbu.export_fbx(fp_fbx, sl=True)
                    pbu.export_as_blend(fp_blend)
                else:
                    pLog.warning("There's no PeachAsset format collections",
                                 fn=publish_new_version, cls=pDir.fileNameBare(__file__))


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
        publish_new_version()
        return {"FINISHED"}
