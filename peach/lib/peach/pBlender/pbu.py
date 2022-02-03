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
import addon_utils
import bpy
from peach import pImp, pLog
pImp.reload(pLog)


def _pb_addons():
    """
    [ pBlender::Util -> pbu ] Internal
    Import all the addons in this function.
    vvv
    @return: (tuple of modules)
    """
    from peach.pBlender.addons import (bAsset,)
    return (bAsset, )


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
            m.register()
        except Exception as e:
            pLog.error("[ {} ] Module Install Failed".format(m.__name__),
                       fn=unregister_addons, cls="pbu")
            raise e
        finally:
            pLog.message("[ {} ] Module Successfully Installed".format(m.__name__),
                         fn=unregister_addons, cls="pbu")
            unregistered_count += 1
    return unregistered_count


def reload_addons():
    unregister_addons()
    pImp.reload(*_pb_addons())
    register_addons()


def r_cls(*classes):
    for cls in classes:
        if isinstance(cls, type):
            bpy.utils.register_class(cls)


def u_cls(*classes):
    for cls in classes:
        if isinstance(cls, type):
            bpy.utils.unregister_class(cls)
