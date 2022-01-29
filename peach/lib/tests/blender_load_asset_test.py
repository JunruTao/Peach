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
# [ File Name ] blender_load_asset_test.py@python
# [ File Description ] - 2022.01.29 (Y.M.D) - 14:26
#                            *   *   *   *
#
#   This script contains tests(backup scrips)
#
# ---------------------------------------------------------------------
import json
import bpy
import mathutils
from peach import pDir, pUtil, pImp
pImp.reload(pUtil)

files = []
with open('E:/test.json') as json_file:
    data = json.load(json_file)
    for items in data:
        file = items['file']
        if file not in files:
            files.append(file)
            print(file)


grp_name = "instance_geo_GRP"
grp = bpy.data.collections.new(grp_name)
box_ins = None
co_data = None
bpy.context.scene.collection.children.link(grp)
for f in files:
    blend_file = pDir.pathSlashConvert(f + ".blend")
    if pDir.exists(blend_file):
        bpy.ops.wm.link(
                filepath=pDir.fileName(blend_file),
                directory=blend_file + "\\Collection\\",
                filename="box")
        co_data = bpy.data.collections['box']
        box_ins = co_data
        bpy.context.scene.collection.objects.unlink(bpy.data.objects['box'])
        grp.children.link(co_data)
        print(blend_file)

layout = bpy.data.collections.new('layout_grp')
bpy.context.scene.collection.children.link(layout)
bpy.context.layer_collection.children[grp_name].exclude = True
counter = 0


import math

mst = bpy.data.objects.new( "empty", None )
mst.name = "Master_transform"
layout.objects.link( mst )

for items in data:
    counter += 1
    o = bpy.data.objects.new( "empty", None )
    o.name = "INS_{0}_id{1:03d}".format(items['asset'], counter)
    layout.objects.link( o )
    t = list(items['t'])
    r = list(items['r'])
    s = list(items['s'])

    c = 0
    r[0] -= 90
    r[2] -= 180
    s = pUtil.y_to_z_up_s(*s)
    for rv in r:
        r[c] = math.radians(rv)
        c += 1

    o.location = mathutils.Vector(tuple(t))
    o.rotation_euler = mathutils.Euler(tuple(r), 'XYZ')
    o.scale = mathutils.Vector(tuple(s))
    o.instance_type = 'COLLECTION'
    o.instance_collection = co_data

    o.parent = mst
    o.matrix_parent_inverse = mst.matrix_world.inverted()

mst.rotation_euler = mathutils.Euler((math.pi/2, 0, math.pi), 'XYZ')
