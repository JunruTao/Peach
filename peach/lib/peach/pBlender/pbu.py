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
# [ File Name ] pbu.py@python
# [ File Description ] - 2022.01.28 (Y.M.D) - 22:24
#                            *   *   *   *
#
#   This script contains util functions for blender
#
# ---------------------------------------------------------------------
import bpy
from peach import pImp, pLog, pDir
pImp.reload(pLog, pDir)


def _pb_addons():
    """
    [ pBlender::Util -> pbu ] Internal
    Import all the addons in this function.
    vvv
    @return: (tuple of modules)
    """
    from peach.pBlender.addons import (bImg,
                                       bAsset,
                                       bMenu
                                       )
    return (bImg,
            bAsset,
            bMenu
            )


def purge_scene():
    """
    [ pBlender Util ] Delete Everything/Data in Blender file.
    """
    # /.delete objects
    for obj in bpy.context.selectable_objects:
        bpy.data.objects.remove(obj)
    # /.delete collections
    for cln in bpy.data.collections:
        bpy.data.collections.remove(cln)
    # /.delete mesh, and camera:
    for ms in bpy.data.meshes:
        bpy.data.meshes.remove(ms)
    for cm in bpy.data.cameras:
        bpy.data.cameras.remove(cm)


def register_addons():
    registered_count = 0
    for m in _pb_addons():
        try:
            m.register()
        except Exception as e:
            pLog.error("[ {} ] Module Install Failed".format(m.__name__),
                       fn=register_addons, cls="pbu")
            raise e
        finally:
            pLog.message("[ {} ] Module Successfully Installed".format(m.__name__),
                         fn=register_addons, cls="pbu")
            registered_count += 1
    return registered_count


def unregister_addons():
    unregistered_count = 0
    for m in _pb_addons():
        try:
            m.unregister()
        except Exception as e:
            pLog.error("[ {} ] Module Uninstall Failed".format(m.__name__),
                       fn=unregister_addons, cls="pbu")
            raise e
        finally:
            pLog.message("[ {} ] Module Successfully Uninstalled".format(m.__name__),
                         fn=unregister_addons, cls="pbu")
            unregistered_count += 1
    return unregistered_count


def reload_addons_modules():
    pImp.reload(*_pb_addons())


def reload_addons():
    reload_addons_modules()
    register_addons()


def r_cls(*classes):
    for cls in classes:
        if isinstance(cls, type):
            bpy.utils.register_class(cls)


def u_cls(*classes):
    for cls in classes:
        if isinstance(cls, type):
            bpy.utils.unregister_class(cls)


def save_blend_as(filepath=""):
    if pDir.exists(pDir.parent(filepath)):
        bpy.ops.wm.save_as_mainfile(filepath=filepath)


def save_blend():
    cf = bpy.data.filepath
    if cf:
        bpy.ops.wm.save_mainfile(filepath=cf)


def export_as_blend(filepath=""):
    if pDir.exists(pDir.parent(filepath)):
        cf = bpy.data.filepath
        if cf:
            save_blend()
            bpy.ops.wm.save_as_mainfile(filepath=filepath)
            bpy.ops.wm.open_mainfile(filepath=cf)


def export_fbx(filepath="", sl=True):
    if pDir.exists(pDir.parent(filepath)):
        bpy.ops.export_scene.fbx(filepath=filepath, use_selection=sl)


def deselect_all():
    for obj in bpy.context.selected_objects:
        obj.select_set(False)


def select(obj_):
    obj_.select_set(True)


def apt_R():
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)


def apt_T():
    bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)


def apt_S():
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)


def apt_A():
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

