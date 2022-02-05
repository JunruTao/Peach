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
import math

from peach import pDir, pUtil, pImp, pLog
pImp.reload(pUtil)


# loading json
json_file_dir = 'C:/Users/1/Desktop/layout.json'
json_file_name = pDir.fileNameBare(json_file_dir)
with open(json_file_dir) as json_file:
    layout_data = json.load(json_file)
    if not layout_data:
        json_file.close()
        pLog.error("json data is not loaded", e=RuntimeError)
    json_file.close()

# /.Add Layout group to the scene
layout_name = "LAY_{}_GRP".format(json_file_name)
layout = None
if bpy.data.collections.find(layout_name) < 0:
    layout = bpy.data.collections.new(layout_name)
    bpy.context.scene.collection.children.link(layout)
else:
    layout = bpy.data.collections.get(layout_name)
    for obj_ in layout.all_objects.items():
        bpy.data.objects.remove(obj_[1])

# /.set to scene collections as active collection
layer_collection = bpy.context.view_layer.layer_collection
bpy.context.view_layer.active_layer_collection = layer_collection

# /.Adding A master transform.
mst_name = "MASTER_TRANSFROM_{}_EPT".format(json_file_name)
mst = bpy.data.objects.new( "empty", None )
mst.name = mst_name
layout.objects.link(mst)

# /.Create the main group for file instancs
grp_name = "instance_geo_GRP"
grp = None

if bpy.data.collections.find(grp_name) < 0:
    # /..the group does not exist
    grp = bpy.data.collections.new(grp_name)
    bpy.context.scene.collection.children.link(grp)
    # /..make the instance group inviable from render
    bpy.context.layer_collection.children[grp_name].exclude = True
else:
    # /..the group has been created
    grp = bpy.data.collections.get(grp_name)


for key, data in layout_data.items():
    f = data["path"]
    f_name = pDir.fileName(f)
    to_link = True
    co_data = None
    if pDir.exists(f):
        # /. Found Existing Collections in Data
        if grp.children.find(key) != -1:
            for lib_item in bpy.data.libraries.items():
                file_bare = f_name.split(".")[0]
                if file_bare in lib_item[0]:
                    if f_name != lib_item[0]:
                        # /.in the scene has an older version
                        to_link = True
                        bpy.data.collections.remove(bpy.data.collections.get(key))
                        pLog.message(lib_item[0], fn="Remove Other Versions", cls="Peach.pBlender")
                        bpy.data.libraries.remove(lib_item[1])
                    else:
                        # /.in the scene and latest.
                        to_link = False
                        pLog.message(lib_item[0], fn="ReloadLib", cls="Peach.pBlender")
                        lib_item[1].reload()
                    break

        if to_link:
            # /..link files
            bpy.ops.wm.link(
                    filepath=f,
                    directory=f + "\\Collection\\",  # this is hard coded blender standard
                    filename=key)
            pLog.message(f_name, fn="LinkFile", cls="Peach.pBlender")

            # /..remove linked from scene
            if bpy.context.scene.collection.objects.find(key) >= 0:
                # /..this is the first create.
                bpy.context.scene.collection.objects.unlink(bpy.data.objects[key])

            co_data = bpy.data.collections[key]
            grp.children.link(co_data)
        else:
            co_data = grp.children.get(key)

        counter = 0
        for items in data["instances"]:
            counter += 1
            o = bpy.data.objects.new( "empty", None )
            o.name = "INS_{0}_id{1:03d}".format(key, counter)
            layout.objects.link( o )
            t = list(items['t'])
            r = list(items['r'])
            s = list(items['s'])

            r[0] -= 90
            s = pUtil.y_to_z_up_s(*s)
            c = 0
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

# /.Rotate the master transform to get the right axis.
mst.rotation_euler = mathutils.Euler((math.pi/2, 0,0), 'XYZ')

