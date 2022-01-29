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
