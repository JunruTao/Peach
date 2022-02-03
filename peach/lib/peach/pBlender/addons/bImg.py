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
# [ File Name ] bImg.py@python
# [ File Description ] - 2022.02.03 (Y.M.D) - 20:28
#                            *   *   *   *
#
#   This script contains Blender Image/Icon Loading Functions
#
# ---------------------------------------------------------------------
import bpy
from peach import pImp, pIco
pImp.reload(pIco)
ICM = pIco.IconTank()

icon_collections = dict()
icon_names = ICM.getNames()


def get_id(name="peach"):
    if name in icon_names:
        p_coll = icon_collections["peach"]
        _ico = p_coll[name]
        return _ico.icon_id


def register():
    import bpy.utils.previews
    p_coll = bpy.utils.previews.new()
    for n in icon_names:
        ico_dir = str(ICM.get(n).getPath("x25"))
        p_coll.load(n, ico_dir, 'IMAGE')
    icon_collections["peach"] = p_coll


def unregister():
    for p_coll in icon_collections.values():
        bpy.utils.previews.remove(p_coll)
    icon_collections.clear()
